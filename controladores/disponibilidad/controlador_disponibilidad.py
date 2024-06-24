from bd import obtener_conexion
from datetime import time
def get_disponibilidad():
    conexion = obtener_conexion()
    disponibilidad = []

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT persona.idpersona, CONCAT(persona.apellidos, ' ', persona.nombres) AS nombre_completo, dia, 
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
def eliminar_disponibilidad(idpersona):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM docente_disponibilidad WHERE idpersona = %s", (idpersona,))
            conexion.commit()
            return {"mensaje": "Disponibilidad eliminada correctamente"}
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

def obtener_disponibilidad_por_id(idpersona, dia, hora_inicio, hora_fin):
    conexion = obtener_conexion()
    disponibilidad = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT persona.idpersona, CONCAT(persona.apellidos, ' ', persona.nombres) AS nombre_completo, dia, 
                TIME_FORMAT(hora_inicio, '%%H:%%i') AS hora_inicio, 
                TIME_FORMAT(hora_fin, '%%H:%%i') AS hora_fin
                FROM docente_disponibilidad
                INNER JOIN persona ON docente_disponibilidad.idpersona = persona.idpersona
                WHERE persona.idpersona = %s AND dia = %s AND TIME_FORMAT(hora_inicio, '%%H:%%i') = %s AND TIME_FORMAT(hora_fin, '%%H:%%i') = %s
            """, (idpersona, dia, hora_inicio, hora_fin))
            disponibilidad = cursor.fetchone()
            if disponibilidad:
                columnas = [desc[0] for desc in cursor.description]
                disponibilidad_dict = dict(zip(columnas, disponibilidad))
                return disponibilidad_dict
            else:
                return {"error": "Disponibilidad no encontrada"}
    except Exception as e:
        print(f"Error: {str(e)}")  # Registro del error
        return {"error": str(e)}
    finally:
        conexion.close()

def obtener_disponibilidad():
    conexion = obtener_conexion()
    docentes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
            SELECT idpersona, CONCAT(apellidos, ' ', nombres) AS nombre_completo, correo, telefono
            FROM persona
            WHERE tipopersona = 'D'
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            for row in rows:
                docente_dict = dict(zip(column_names, row))
                docentes.append(docente_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return docentes
