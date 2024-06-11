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
