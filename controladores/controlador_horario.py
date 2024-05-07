from bd import obtener_conexion

def obtener_horarios():
    conexion = obtener_conexion()
    Horarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idpersona,nombres,apellidos,n_documento,telefono,correo,tipopersona,cantHoras,tiempo_ref,foto FROM persona")
        Horarios = cursor.fetchall()
    conexion.close()
    return Horarios

def obtener_horarios_por_docenteId_semestre(id_docente,semestre):
    conexion = obtener_conexion()
    Horarios = None
    with conexion.cursor() as cursor:
        cursor.execute(
            """SELECT idhorario, amb.nombre, dia, horainicio, horafin, h_virtual, h_presencial, sem.descripcion, hor.idpersona, id_grupo FROM horario hor 
INNER JOIN ambiente amb ON amb.idambiente = hor.idambiente
INNER JOIN persona per ON hor.idpersona = per.idpersona
INNER JOIN semestre_academico sem ON sem.idsemestre = hor.idsemestre 
WHERE per.idpersona = ""+%s+"" AND sem.descripcion = %s""", (id_docente,semestre))
        Horarios = cursor.fetchone()
    conexion.close()
    return Horarios

def obtener_horarios_por_docenteNombre_semestre(nombre_docente,semestre):
    conexion = obtener_conexion()
    Horarios = None
    with conexion.cursor() as cursor:
        cursor.execute(
            """SELECT idhorario, amb.nombre, dia, horainicio, horafin, h_virtual, h_presencial, sem.descripcion, hor.idpersona, id_grupo FROM horario hor 
INNER JOIN ambiente amb ON amb.idambiente = hor.idambiente
INNER JOIN persona per ON hor.idpersona = per.idpersona
INNER JOIN semestre_academico sem ON sem.idsemestre = hor.idsemestre 
WHERE per.apellidos||' '||per.nombres = ""+%s+"" AND sem.descripcion = %s""", (nombre_docente,semestre))
        Horarios = cursor.fetchone()
    conexion.close()
    return Horarios
