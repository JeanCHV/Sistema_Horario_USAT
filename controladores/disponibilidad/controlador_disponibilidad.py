from flask import jsonify
from bd import obtener_conexion
from datetime import time

def get_disponibilidad():
    conexion = obtener_conexion()
    disponibilidad = []

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT persona.idpersona, CONCAT(persona.apellidos, ' ', persona.nombres) AS nombre_completo, dia, 
                DATE_FORMAT(hora_inicio, '%H:%i:%s') AS hora_inicio, 
                DATE_FORMAT(hora_fin, '%H:%i:%s') AS hora_fin,
                docente_disponibilidad.id_disponibilidad_docente
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
        return jsonify({"error": str(e)}), 500
    finally:
        conexion.close()

    return jsonify(disponibilidad), 200

def agregar_disponibilidad(idpersona, dia, hora_inicio, hora_fin):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO docente_disponibilidad (idpersona, dia, hora_inicio, hora_fin)
                VALUES (%s, %s, %s, %s)
                """,
                (idpersona, dia, hora_inicio, hora_fin),
            )
            conexion.commit()
            return jsonify({"mensaje": "Disponibilidad agregada correctamente"}), 201
    except Exception as e:
        conexion.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        conexion.close()

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
            return jsonify({"mensaje": "Disponibilidad modificada correctamente"}), 200
    except Exception as e:
        conexion.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        conexion.close()

def eliminar_disponibilidad(id_disponibilidad_docente):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM docente_disponibilidad WHERE id_disponibilidad_docente = %s", (id_disponibilidad_docente,))
            conexion.commit()
            return jsonify({"mensaje": "Disponibilidad eliminada correctamente"}), 200
    except Exception as e:
        conexion.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        conexion.close()

def obtener_disponibilidad_por_id(id_disponibilidad_docente):
    conexion = obtener_conexion()
    disponibilidad = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                """SELECT 
                    id_disponibilidad_docente, 
                    idpersona, 
                    dia, 
                    DATE_FORMAT(hora_inicio, '%%H:%%i') AS hora_inicio, 
                    DATE_FORMAT(hora_fin, '%%H:%%i') AS hora_fin 
                FROM 
                    docente_disponibilidad 
                WHERE 
                    id_disponibilidad_docente = %s""",
                (id_disponibilidad_docente,)
            )
            disponibilidad = cursor.fetchone()
            if disponibilidad:
                columnas = [desc[0] for desc in cursor.description]
                disponibilidad_dict = dict(zip(columnas, disponibilidad))
                return jsonify(disponibilidad_dict), 200
            else:
                return jsonify({"error": "Disponibilidad no encontrada"}), 404
    except Exception as e:
        print(f"Error: {str(e)}")  # Registro del error
        return jsonify({"error": str(e)}), 500
    finally:
        conexion.close()

def obtener_docentes():
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
        return jsonify({"error": str(e)})
    finally:
        conexion.close()

    return jsonify(docentes)

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
        return jsonify({"error": str(e)})
    finally:
        conexion.close()

    return jsonify(docentes)

def asignar_disponibilidad_docente(tipo, dia, hora_inicio, hora_fin, idpersona):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_DocenteDisponibilidad_Gestion', [1, dia, hora_inicio, hora_fin, idpersona])
            conexion.commit()
            return jsonify({"mensaje": f"Operación {tipo} realizada correctamente para el docente {idpersona} en el día {dia}"})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conexion.close()

def obtener_id_persona(nombre_docente):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idpersona FROM persona WHERE CONCAT(apellidos, ' ', nombres) = %s", (nombre_docente,))
            result = cursor.fetchone()
            return jsonify({"idpersona": result['idpersona']}) if result else jsonify({"error": "Docente no encontrado"})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conexion.close()