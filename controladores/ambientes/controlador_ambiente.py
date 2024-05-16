from bd import obtener_conexion
from flask import request, jsonify

def obtener_ambientes():
    conexion = obtener_conexion()
    ambientes = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT idambiente, nombre, aforo, estado, idedificio, idambientetipo FROM ambiente")
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            ambiente_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            ambientes.append(ambiente_dict)

    conexion.close()
    return ambientes

def agregar_ambiente(nombre, aforo, estado, idedificio, idambientetipo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO ambiente (nombre, aforo, estado, idedificio, idambientetipo) VALUES (%s, %s, %s, %s, %s)",
                           (nombre, aforo, estado, idedificio, idambientetipo))
            conexion.commit()
            return {"mensaje": "Ambiente agregado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()


def eliminar_ambiente(idambiente):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Ambiente_Gestion', [4, idambiente, None, None, None, None, None])
            conexion.commit()
            return {"mensaje": "Ambiente eliminado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def dar_baja_ambiente(idambiente):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Ambiente_Gestion', [3, idambiente, None, None, None, None, None])
            conexion.commit()
            return {"mensaje": "Ambiente dado de baja correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def modificar_ambiente(idambiente, nombre, aforo, estado, idedificio, idambientetipo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Ambiente_Gestion', [2, idambiente, nombre, aforo, estado, idedificio, idambientetipo])
            conexion.commit()
            return {"mensaje": "Ambiente modificado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
