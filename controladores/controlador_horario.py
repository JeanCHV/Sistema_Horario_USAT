from bd import obtener_conexion
from datetime import *

def obtener_horarios_por_docenteId_semestre(id_docente,semestre):
    conexion = obtener_conexion()
    Horarios = []
    with conexion.cursor() as cursor:
        cursor.execute(
        """
        SELECT idhorario AS codigo, amb.nombre AS ambiente,cur.nombre AS curso,dia AS dia,CAST(horainicio AS CHAR) AS horainicio,
        CAST(horafin AS CHAR) AS horafin,h_virtual,h_presencial,
        CASE 
        WHEN cur.tipo_curso = 0 THEN 'Presencial'
        WHEN cur.tipo_curso = 1 THEN 'Virtual'
        END AS tipo
        ,gru.nombre AS grupo,cur.ciclo AS ciclo,esc.abreviatura AS escuela 
        FROM horario hor 
                    INNER JOIN ambiente amb ON amb.idambiente = hor.idambiente
                    INNER JOIN persona per ON hor.idpersona = per.idpersona
                    INNER JOIN grupo gru ON gru.id_grupo = hor.id_grupo
                    INNER JOIN curso cur ON cur.idcurso = gru.idcurso
                    INNER JOIN semestre_academico sem ON sem.idsemestre = gru.idsemestre
                    INNER JOIN plan_estudio pla ON pla.id_plan_estudio = cur.id_plan_estudio
                    INNER JOIN escuela esc ON esc.id_escuela = pla.id_escuela
                    WHERE per.tipopersona = 'D' AND 
                    per.idpersona = %s AND sem.descripcion = %s""",(id_docente,semestre))
        Horarios = cursor.fetchall()
    conexion.close()
    return Horarios

#*********CABALLERO CAMBIA TU CONSULTA QUE EN LA BD ACTUALIZADA YA NO HAY SEMESTRE EN HORARIO***********

# def obtener_horarios_por_docenteId_semestre(id_docente,semestre):
#     conexion = obtener_conexion()
#     Horarios = None
#     with conexion.cursor() as cursor:
#         cursor.execute(
#             """SELECT idhorario, amb.nombre, dia, horainicio, horafin, h_virtual, h_presencial, sem.descripcion, hor.idpersona, id_grupo FROM horario hor 
# INNER JOIN ambiente amb ON amb.idambiente = hor.idambiente
# INNER JOIN persona per ON hor.idpersona = per.idpersona
# INNER JOIN semestre_academico sem ON sem.idsemestre = hor.idsemestre 
# WHERE per.idpersona = ""+%s+"" AND sem.descripcion = %s""", (id_docente,semestre))
#         Horarios = cursor.fetchone()
#     conexion.close()
#     return Horarios

# def obtener_horarios_por_docenteNombre_semestre(nombre_docente,semestre):
#     conexion = obtener_conexion()
#     Horarios = None
#     with conexion.cursor() as cursor:
#         cursor.execute(
#             """SELECT idhorario, amb.nombre, dia, horainicio, horafin, h_virtual, h_presencial, sem.descripcion, hor.idpersona, id_grupo FROM horario hor 
# INNER JOIN ambiente amb ON amb.idambiente = hor.idambiente
# INNER JOIN persona per ON hor.idpersona = per.idpersona
# INNER JOIN semestre_academico sem ON sem.idsemestre = hor.idsemestre 
# WHERE per.apellidos||' '||per.nombres = ""+%s+"" AND sem.descripcion = %s""", (nombre_docente,semestre))
#         Horarios = cursor.fetchone()
#     conexion.close()
#     return Horarios






######HORARIO POR AMBIENTE

def obtener_horarios_por_ambiente(idambiente,idsemestre):
    conexion = obtener_conexion()
    horarios = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT h.idhorario, h.dia, h.horainicio, h.horafin, h.h_virtual, h.h_presencial, h.idpersona, h.id_grupo, g.idsemestre, CONCAT(c.nombre, ' - ', g.nombre) AS 
                           nombre_curso FROM horario h INNER JOIN grupo g ON g.id_grupo = h.id_grupo INNER JOIN curso c ON c.idcurso = g.idcurso WHERE h.idambiente = %s and g.idsemestre= %s
            """, (idambiente,idsemestre))
            rows = cursor.fetchall()
            if rows:
                columnas = [desc[0] for desc in cursor.description]
                for row in rows:
                    horario_dict = dict(zip(columnas, row))
                    # Convertir los campos de tiempo a cadenas de texto
                    horario_dict['horainicio'] = str(horario_dict['horainicio'])
                    horario_dict['horafin'] = str(horario_dict['horafin'])
                    horarios.append(horario_dict)
                print("Horarios obtenidos:", horarios)  # Depuración
                return horarios
            else:
                return []
    except Exception as e:
        print(f"Error al obtener los horarios: {e}")
        return {"error": str(e)}
    finally:
        conexion.close()


def insertar_horarios_ia(horarios):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Preparar la consulta de inserción
            consulta_insert = """
            INSERT INTO horario (idambiente, dia, horainicio, horafin, h_virtual, h_presencial, idpersona, id_grupo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Insertar cada horario en la base de datos
            for horario in horarios:
                cursor.execute(consulta_insert, (
                    horario['idambiente'],
                    horario['dia'],
                    datetime.strptime(horario['horainicio'], '%H:%M:%S').time(),
                    datetime.strptime(horario['horafin'], '%H:%M:%S').time(),
                    horario['h_virtual'],
                    horario['h_presencial'],
                    horario['idpersona'],
                    horario['id_grupo']
                ))
        conexion.commit()  # Confirmar los cambios
        return {"message": "Horarios insertados correctamente"}
    except Exception as e:
        conexion.rollback()  # Revertir los cambios en caso de error
        print(f"Error al insertar los horarios: {e}")
        return {"error": str(e)}
    finally:
        conexion.close()    