from bd import obtener_conexion


def obtener_edificios():
    conexion = obtener_conexion()
    edificios = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idedificio, nombre FROM edificio")
            for edificio in cursor.fetchall():
                edificios.append(
                    {'idedificio': edificio[0], 'nombre': edificio[1]})
    finally:
        conexion.close()
    return edificios


#dashboard
def get_edificio_ambientes():
    conexion = obtener_conexion()
    cursos_tipo = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT e.nombre AS edificio,COUNT(a.idambiente) AS ambientes FROM ambiente a JOIN edificio e ON a.idedificio=e.idedificio GROUP BY e.nombre;")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                edificio_ambiente = dict(zip(column_names, row))
                cursos_tipo.append(edificio_ambiente)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return cursos_tipo