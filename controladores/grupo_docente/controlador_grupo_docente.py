from bd import obtener_conexion

## ALGORTIMO GENETICO 

def get_grupo_docente():
    conexion = obtener_conexion()
    grupo_docente = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT curso_docente.idcurso,curso.nombre AS Curso,grupo.id_grupo,grupo.nombre AS Grupo,curso_docente.idpersona,persona.nombres AS Nombre,persona.apellidos AS Apellidos FROM curso INNER JOIN grupo ON curso.idcurso=grupo.idcurso INNER JOIN persona INNER JOIN curso_docente ON persona.idpersona=curso_docente.idpersona AND curso.idcurso=curso_docente.idcurso WHERE grupo.idsemestre=1 AND persona.tipopersona='D' ORDER BY curso.nombre ASC ")
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            grupo_docente_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            grupo_docente.append(grupo_docente_dict)

    conexion.close()
    return grupo_docente
