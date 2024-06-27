from bd import obtener_conexion

## ALGORTIMO GENETICO


def get_grupo_docente():
    conexion = obtener_conexion()
    grupo_docente = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT idgrupo,idpersona from grupo_docente")
        column_names = [
            desc[0] for desc in cursor.description
        ]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            grupo_docente_dict = dict(
                zip(column_names, row)
            )  # Convertir cada fila en un diccionario
            grupo_docente.append(grupo_docente_dict)

    conexion.close()
    return grupo_docente


def get_docentes_no_asignados():
    conexion = obtener_conexion()
    docente_sin_asignar = []

    with conexion.cursor() as cursor:
        cursor.execute(
            """SELECT
	p.idpersona, 
	p.nombres, 
	p.apellidos
FROM
	persona AS p
	LEFT JOIN
	grupo_docente AS gd
	ON 
		p.idpersona = gd.idpersona
WHERE
	p.tipopersona = 'D' AND
	gd.idpersona IS NULL AND
	p.estado = 1;
"""
        )
        column_names = [
            desc[0] for desc in cursor.description
        ]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            grupo_docente_dict = dict(
                zip(column_names, row)
            )  # Convertir cada fila en un diccionario
            docente_sin_asignar.append(grupo_docente_dict)

    conexion.close()
    return docente_sin_asignar
