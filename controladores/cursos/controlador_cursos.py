from bd import obtener_conexion

def obtener_cursos():
    conexion = obtener_conexion()
    cursos = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM curso")
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            curso_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            cursos.append(curso_dict)

    conexion.close()
    return cursos
