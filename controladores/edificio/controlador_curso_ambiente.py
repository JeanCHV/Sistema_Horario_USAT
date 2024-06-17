from bd import obtener_conexion


def obtener_edificios():
    conexion = obtener_conexion()
    edificios = []

    with conexion.cursor() as cursor:
        cursor.callproc('sp_Edificio_Gestion', [0, None, None, None])
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        for row in rows:
            edificio_dict = dict(zip(column_names, row))
            edificios.append(edificio_dict)

    conexion.close()
    return edificios
