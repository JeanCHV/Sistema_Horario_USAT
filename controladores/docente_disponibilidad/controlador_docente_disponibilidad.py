from bd import obtener_conexion
#Querys Algoritmo Genetico
def get_disponibilidad():
    conexion = obtener_conexion()
    disponibilidad = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT dia,TIME_FORMAT(hora_inicio,'%H:%i') AS hora_inicio,TIME_FORMAT(hora_fin,'%H:%i') AS hora_fin,idpersona FROM docente_disponibilidad;")
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        for row in rows:
            disponibilidad_dict = dict(zip(column_names, row))
            disponibilidad.append(disponibilidad_dict)

    conexion.close()
    return disponibilidad