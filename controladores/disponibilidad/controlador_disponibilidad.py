from bd import obtener_conexion

def get_disponibilidad():
    conexion = obtener_conexion()
    disponibilidad = []

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT CONCAT(persona.apellidos, ' ', persona.nombres) AS nombre_completo, dia, 
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


# Función para agregar una nueva disponibilidad
def agregar_disponibilidad(idpersona, dia, hora_inicio, hora_fin):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                INSERT INTO docente_disponibilidad (idpersona, dia, hora_inicio, hora_fin)
                VALUES (%s, %s, %s, %s)
            """, (idpersona, dia, hora_inicio, hora_fin))
            conexion.commit()
            return {"mensaje": "Disponibilidad agregada correctamente"}
    except Exception as e:
        conexion.commit()
        return {"error": str(e)}
    finally:
        conexion.close()

# Función para modificar una disponibilidad existente
def modificar_disponibilidad(iddisponibilidad, idpersona, dia, hora_inicio, hora_fin):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                UPDATE docente_disponibilidad
                SET idpersona = %s, dia = %s, hora_inicio = %s, hora_fin = %s
                WHERE iddisponibilidad = %s
            """, (idpersona, dia, hora_inicio, hora_fin, iddisponibilidad))
            conexion.commit()
            return {"mensaje": "Disponibilidad modificada correctamente"}
    except Exception as e:
        conexion.commit()
        return {"error": str(e)}
    finally:
        conexion.close()

# Función para eliminar una disponibilidad
def eliminar_disponibilidad(iddisponibilidad):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM docente_disponibilidad WHERE iddisponibilidad = %s", (iddisponibilidad,))
            conexion.commit()
            return {"mensaje": "Disponibilidad eliminada correctamente"}
    except Exception as e:
        conexion.commit()
        return {"error": str(e)}
    finally:
        conexion.close()

# Función para obtener la disponibilidad por ID
def obtener_disponibilidad_por_id(iddisponibilidad):
    conexion = obtener_conexion()
    disponibilidad = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM docente_disponibilidad WHERE iddisponibilidad = %s", (iddisponibilidad,))
            disponibilidad = cursor.fetchone()
            if disponibilidad:
                columnas = [desc[0] for desc in cursor.description]  
                disponibilidad_dict = dict(zip(columnas, disponibilidad))  
                return disponibilidad_dict
            else:
                return {"error": "Disponibilidad no encontrada"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()