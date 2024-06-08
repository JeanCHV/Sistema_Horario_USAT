from bd import obtener_conexion

def obtener_horarios_por_docenteId_semestre(id_docente,semestre):
    conexion = obtener_conexion()
    Horarios = None
    with conexion.cursor() as cursor:
        cursor.execute(
        """
        SELECT idhorario AS codigo, amb.nombre AS ambiente,cur.nombre AS curso,dia AS  dia,horainicio,horafin,h_virtual,h_presencial,
        CASE 
        WHEN cur.tipo_curso = 0 THEN 'Presencial'
        WHEN cur.tipo_curso = 1 THEN 'Virtual'
        END AS tipo
        ,gru.nombre AS grupo,cur.ciclo AS ciclo,esc.nombre AS escuela 
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
