from bd import obtener_conexion
## ALGORTIMO GENETICO 

def get_curso_ambiente():
    conexion = obtener_conexion()
    cursos_ambiente = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM curso_ambiente ")
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            cursos_ambiente_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            cursos_ambiente.append(cursos_ambiente_dict)

    conexion.close()
    return cursos_ambiente