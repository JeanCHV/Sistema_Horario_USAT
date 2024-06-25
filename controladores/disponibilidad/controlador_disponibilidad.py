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
            """
            )
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
            cursor.execute(
                """
                INSERT INTO docente_disponibilidad (id, dia, hora_inicio, hora_fin)
                VALUES (%s, %s, %s, %s)
            """,
                (idpersona, dia, hora_inicio, hora_fin),
            )
            conexion.commit()
            return {"mensaje": "Disponibilidad agregada correctamente"}
    except Exception as e:
        conexion.commit()
        return {"error": str(e)}
    finally:
        conexion.close()

# Función para modificar una disponibilidad existente
def modificar_disponibilidad(id_disponibilidad_docente, nuevo_dia, nueva_hora_inicio, nueva_hora_fin):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                UPDATE docente_disponibilidad
                SET dia = %s, hora_inicio = %s, hora_fin = %s
                WHERE id_disponibilidad_docente = %s
                """,
                (nuevo_dia, nueva_hora_inicio, nueva_hora_fin, id_disponibilidad_docente)
            )
            conexion.commit()
            return {"mensaje": "Disponibilidad modificada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

# Función para eliminar una disponibilidad
def eliminar_disponibilidad(id_disponibilidad_docente):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM docente_disponibilidad WHERE id_disponibilidad_docente = %s", (id_disponibilidad_docente,))
            conexion.commit()
            return {"mensaje": "Disponibilidad eliminada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def obtener_disponibilidad_por_id(id_disponibilidad_docente):
    conexion = obtener_conexion()
    disponibilidad = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                """ select from docente_disponibilidad where id_disponibilidad_docente=%s""",(id_disponibilidad_docente) 
            )
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

def get_docente_sin_disponibilidad():
    conexion = obtener_conexion()
    docentes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
SELECT p.idpersona, p.nombres, p.apellidos, p.correo
FROM persona p
LEFT JOIN docente_disponibilidad dd ON p.idpersona = dd.idpersona
WHERE p.tipopersona = 'D' AND dd.idpersona IS NULL;

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

def asignar_disponibilidad_docente(tipo, dia, hora_inicio, hora_fin, idpersona):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_disponibilidad_Gestion', [tipo, dia, hora_inicio, hora_fin, idpersona])
            conexion.commit()
            return {"mensaje": f"Operación {tipo} realizada correctamente para el docente {idpersona} en el día {dia}"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def obtener_id_persona(nombre_docente):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idpersona FROM docentes WHERE nombre_completo = %s", (nombre_docente,))
            result = cursor.fetchone()
            return result['idpersona'] if result else None
    except Exception as e:
        print({"error": str(e)})
    finally:
        conexion.close()

