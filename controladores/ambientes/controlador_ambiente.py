from bd import obtener_conexion
#OPERACIONES CRUD
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
        conexion.commit()
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
        conexion.commit()
        return {"error": str(e)}
    finally:
        conexion.close()

def dar_baja_ambiente(idambiente):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE ambiente SET estado = 'I' WHERE idambiente= %s ", (idambiente,))
            conexion.commit()
            return {"mensaje": "Ambiente dado de baja correctamente"}
    except Exception as e:
        conexion.commit()
        return {"error": str(e)}
    finally:
        conexion.close()

### CAMBIO ESTADOS

def cambiar_estado_ambiente(idambiente, nuevo_estado):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE ambiente SET estado = %s WHERE idambiente = %s", (nuevo_estado, idambiente))
            conexion.commit()
            return {"mensaje": "Estado del ambiente actualizado correctamente"}
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
        conexion.commit()
        return {"error": str(e)}
    finally:
        conexion.close()

#OTRAS OPERACIONES
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
def obtener_ambiente_semestre(nombre):
    conexion = obtener_conexion()
    ambientes = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT ambiente.nombre FROM semestre_academico INNER JOIN grupo ON semestre_academico.idsemestre=grupo.idsemestre INNER JOIN curso ON grupo.idcurso=curso.idcurso INNER JOIN ambiente INNER JOIN curso_ambiente ON ambiente.idambiente=curso_ambiente.idambiente AND curso.idcurso=curso_ambiente.idcurso WHERE semestre_academico.descripcion= %s", (nombre,))
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        for row in rows:
            ambiente_dict = dict(zip(column_names, row))
            ambientes.append(ambiente_dict)

    conexion.close()
    return ambientes
##AmbientesPorEdificio

def ambientes_por_edificio(idedificio):
    conexion = obtener_conexion()
    ambientes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idambiente,nombre  FROM ambiente WHERE idedificio = %s AND estado = 'A'", (idedificio,))
            for ambiente in cursor.fetchall():
                ambientes.append({'idambiente': ambiente[0], 'nombre': ambiente[1]})
    finally:
        conexion.close()
    return ambientes
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

#DASHBOARD
def get_ambientes_disponibles():
    conexion = obtener_conexion()
    ambientes_disponibles = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS ambientes_disponibles FROM ambiente WHERE estado = 'A'")
            column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
            row = cursor.fetchone()

            if row:
                ambiente_dict = dict(zip(column_names, row))  # Convertir la fila en un diccionario
                ambientes_disponibles.append(ambiente_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return ambientes_disponibles


def get_ambientes_capacidad_ocupacion():
    conexion = obtener_conexion()
    ambientes = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT nombre AS nombre,aforo AS capacidad,CASE WHEN estado='A' THEN 'Activo' WHEN estado='I' THEN 'Inactivo' ELSE 'Desconocido' END AS estado FROM ambiente ORDER BY capacidad DESC;")
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        for row in rows:
            ambiente_dict = dict(zip(column_names, row))
            ambientes.append(ambiente_dict)

    conexion.close()
    return ambientes



