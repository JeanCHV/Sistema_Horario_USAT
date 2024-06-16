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

def obtener_horarios_por_ambiente(idambiente,semestre):
    conexion = obtener_conexion()
    horarios = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT H.idhorario AS codigo, 
                H.dia AS dia, CAST(H.horainicio AS CHAR) AS horainicio, CAST(H.horafin AS CHAR) AS horafin, H.h_virtual, H.h_presencial,
                CASE WHEN C.tipo_curso = 0 then 'Presencial' WHEN C.tipo_curso = 1 then 'VIRTUAL' END AS tipoCurso,
                ED.nombre AS edificio, UPPER(CONCAT (P.nombres, ' ', P.apellidos))  AS docente, G.nombre AS grupo, C.nombre AS curso, E.abreviatura AS escuela,C.ciclo AS ciclo
                FROM horario H INNER JOIN ambiente A ON A.idambiente= H.idambiente
                INNER JOIN edificio ED ON ED.idedificio = A.idedificio
                INNER JOIN persona P ON P.idpersona = H.idpersona
                INNER JOIN grupo G ON G.id_grupo = H.id_grupo
                INNER JOIN curso C ON C.idcurso = G.idcurso
                INNER JOIN semestre_academico SA ON G.idsemestre = SA.idsemestre
                INNER JOIN plan_estudio PE ON PE.id_plan_estudio = C.id_plan_estudio
                INNER JOIN escuela E ON E.id_escuela = PE.id_escuela
                WHERE A.idambiente = %s and SA.descripcion= %s
            """, (idambiente,semestre))
            rows = cursor.fetchall()
            if rows:
                columnas = [desc[0] for desc in cursor.description]
                for row in rows:
                    horario_dict = dict(zip(columnas, row))
                    # Convertir los campos de tiempo a cadenas de texto
                    horario_dict['horainicio'] = str(horario_dict['horainicio'])
                    horario_dict['horafin'] = str(horario_dict['horafin'])
                    horarios.append(horario_dict)
                return horarios
            else:
                return []
    except Exception as e:
        print(f"Error al obtener los horarios: {e}")
        return {"error": str(e)}
    finally:
        conexion.close()

def obtener_horarios_por_ciclo(ciclo,semestre):
    conexion = obtener_conexion()
    horarios = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT H.idhorario AS codigo, 
                H.dia AS dia, CAST(H.horainicio AS CHAR) AS horainicio, CAST(H.horafin AS CHAR) AS horafin, H.h_virtual, H.h_presencial,
                CASE WHEN C.tipo_curso = 0 then 'Presencial' WHEN C.tipo_curso = 1 then 'Virtual' END AS tipoCurso,
                A.nombre as ambiente, UPPER(CONCAT (P.nombres, ' ', P.apellidos))  AS docente, G.nombre AS grupo, C.nombre AS curso, E.abreviatura AS escuela
                FROM horario H INNER JOIN ambiente A ON A.idambiente= H.idambiente
                INNER JOIN persona P ON P.idpersona = H.idpersona
                INNER JOIN grupo G ON G.id_grupo = H.id_grupo
                INNER JOIN curso C ON C.idcurso = G.idcurso
                INNER JOIN semestre_academico SA ON G.idsemestre = SA.idsemestre
                INNER JOIN plan_estudio PE ON PE.id_plan_estudio = C.id_plan_estudio
                INNER JOIN escuela E ON E.id_escuela = PE.id_escuela
                WHERE P.tipopersona = 'D' AND 
                C.ciclo = %s AND SA.descripcion = %s
            """, (ciclo,semestre))
            rows = cursor.fetchall()
            if rows:
                columnas = [desc[0] for desc in cursor.description]
                for row in rows:
                    horario_dict = dict(zip(columnas, row))
                    # Convertir los campos de tiempo a cadenas de texto
                    horario_dict['horainicio'] = str(horario_dict['horainicio'])
                    horario_dict['horafin'] = str(horario_dict['horafin'])
                    horarios.append(horario_dict)
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
            consulta_insert = """
            INSERT INTO horario (idambiente, dia, horainicio, horafin, h_virtual, h_presencial, idpersona, id_grupo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
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
        conexion.commit()
        return {"message": "Horarios insertados correctamente"}
    except Exception as e:
        conexion.rollback()
        print(f"Error al insertar los horarios: {e}")
        return {"error": str(e)}
    finally:
        conexion.close()