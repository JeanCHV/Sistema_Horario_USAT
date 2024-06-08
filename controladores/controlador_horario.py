from bd import obtener_conexion
from datetime import timedelta

def obtener_horarios_por_docenteId_semestre(id_docente,semestre):
    conexion = obtener_conexion()
    Horarios = None
    with conexion.cursor() as cursor:
        cursor.execute(
        """
        SELECT idhorario, amb.nombre, cur.nombre, dia, horainicio, horafin, h_virtual, h_presencial, gru.nombre FROM horario hor 
            INNER JOIN ambiente amb ON amb.idambiente = hor.idambiente
            INNER JOIN persona per ON hor.idpersona = per.idpersona
            INNER JOIN grupo gru ON gru.id_grupo = hor.id_grupo
            INNER JOIN curso cur ON cur.idcurso = gru.idcurso
            INNER JOIN semestre_academico sem ON sem.idsemestre = gru.idsemestre
            WHERE per.idpersona = %s AND sem.descripcion = %s""",(id_docente,semestre))
        Horarios = cursor.fetchone()
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

def obtener_horarios_por_ambiente(idambiente):
    conexion = obtener_conexion()
    horarios = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT idhorario, dia, horainicio, horafin, h_virtual, h_presencial, idpersona, id_grupo FROM horario
                WHERE idambiente = %s
            """, (idambiente,))
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



