from bd import obtener_conexion

def obtener_ambientes():
    conexion = obtener_conexion()
    ambientes = []

    with conexion.cursor() as cursor:
        cursor.callproc('sp_Ambiente_Gestion', [0, None, None, None, None, None, None])
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        for row in rows:
            ambiente_dict = dict(zip(column_names, row))
            ambientes.append(ambiente_dict)

    conexion.close()
    return ambientes

def agregar_ambiente(nombre, aforo, estado, idedificio, idambientetipo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Ambiente_Gestion', [1, None, nombre, aforo, estado, idedificio, idambientetipo])
            conexion.commit()
            return {"mensaje": "Ambiente agregado correctamente"}
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
            cursor.execute("UPDATE ambiente SET estado='I' WHERE idambiente= %s ", (idambiente,))
            conexion.commit()
            return {"mensaje": "Ambiente dado de baja correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
##OBTENER AMBIENTE POR ID

def obtener_ambiente_por_id(idambiente):
    conexion = obtener_conexion()
    ambiente = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM ambiente WHERE idambiente = %s", (idambiente,))
            ambiente = cursor.fetchone()
            if ambiente:
                columnas = [desc[0] for desc in cursor.description]  
                ambiente_dict = dict(zip(columnas, ambiente))  
                return ambiente_dict
            else:
                return {"error": "Ambiente no encontrado"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

#Querys Algoritmo Genetico
def get_ambientes():
    conexion = obtener_conexion()
    ambientes = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT ambiente.idambiente,ambiente.nombre,ambiente.aforo FROM ambiente WHERE ambiente.estado='A'")
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        for row in rows:
            ambiente_dict = dict(zip(column_names, row))
            ambientes.append(ambiente_dict)

    conexion.close()
    return ambientes