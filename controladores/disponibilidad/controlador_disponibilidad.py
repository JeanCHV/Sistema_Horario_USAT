from bd import obtener_conexion

def get_disponibilidad():
    conexion = obtener_conexion()
    disponibilidad = []

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT CONCAT(persona.nombres, ' ', persona.apellidos) AS nombre_completo, dia, 
                TIME_FORMAT(TIME(hora_inicio), '%H:%i') AS hora_inicio, 
                TIME_FORMAT(TIME(hora_fin), '%H:%i') AS hora_fin
                FROM docente_disponibilidad
                INNER JOIN persona ON docente_disponibilidad.idpersona = persona.idpersona;
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                disponibilidad_dict = dict(zip(column_names, row))
                disponibilidad.append(disponibilidad_dict)

    except Exception as e:
        print("Ocurrió un error al obtener la disponibilidad: ", e)
    finally:
        conexion.close()

    return disponibilidad

