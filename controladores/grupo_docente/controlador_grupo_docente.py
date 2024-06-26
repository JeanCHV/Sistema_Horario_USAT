from bd import obtener_conexion

## ALGORTIMO GENETICO 

def get_grupo_docente():
    conexion = obtener_conexion()
    grupo_docente = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT * from grupo_docente")
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            grupo_docente_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            grupo_docente.append(grupo_docente_dict)

    conexion.close()
    return grupo_docente
