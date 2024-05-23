from bd import obtener_conexion
from flask import request, jsonify

def obtener_docentes():
    conexion = obtener_conexion()
    docentes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idpersona, CONCAT(nombres, ' ', apellidos) AS nombre, correo FROM persona WHERE tipopersona = 'D'")
            column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
            rows = cursor.fetchall()

            for row in rows:
                docente_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
                docentes.append(docente_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return docentes

def agregar_docente(nombres, correo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "INSERT INTO persona (nombres, apellidos, correo, tipopersona) VALUES (%s, '', %s, 'D')",
                (nombres, correo)
            )
            conexion.commit()
            return {"mensaje": "Docente agregado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def eliminar_docente(idpersona):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM persona WHERE idpersona = %s AND tipopersona = 'D'", (idpersona,))
            conexion.commit()
            return {"mensaje": "Docente eliminado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def modificar_docente(idpersona, nombres, correo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                "UPDATE persona SET nombres = %s, correo = %s WHERE idpersona = %s AND tipopersona = 'D'",
                (nombres, correo, idpersona)
            )
            conexion.commit()
            return {"mensaje": "Docente modificado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

