from bd import obtener_conexion
from flask import request, jsonify

def obtener_docentes():
    conexion = obtener_conexion()
    docentes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT idpersona, CONCAT(apellidos, ' ', nombres) AS nombre, correo, telefono 
                FROM persona 
                WHERE tipopersona = 'D'
            """)
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

def datos_docentes():
    conexion = obtener_conexion()
    docentes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idpersona, UPPER(CONCAT(apellidos, ' ', nombres)) AS docente, correo, telefono FROM persona WHERE tipopersona = 'D' ORDER BY docente")
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        for row in rows:
            docente_dict = dict(zip(column_names,row))
            docentes.append(docente_dict)
    conexion.close()
    return docentes

def agregar_docente(nombres, apellidos,n_documento, telefono, correo, cantHoras, tiempo_ref, estado):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Persona_Gestion', [1, None, nombres, apellidos,n_documento, telefono, correo, 'D', cantHoras, tiempo_ref, estado])
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
            cursor.callproc('sp_Persona_Gestion', [3, idpersona, None, None, None, None, None, None, None, None, None])
            conexion.commit()
            return {"mensaje": "Docente eliminado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def modificar_docente(idpersona, nombres, apellidos,n_documento, telefono, correo, cantHoras, tiempo_ref, estado):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Persona_Gestion', [2, idpersona, nombres, apellidos,n_documento, telefono, correo, 'D', cantHoras, tiempo_ref, estado])
            conexion.commit()
            return {"mensaje": "Docente modificado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

#Querys Algoritmo Genetico
def get_docentes():
    conexion = obtener_conexion()
    docentes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT persona.idpersona,persona.nombres,persona.apellidos,persona.cantHoras,persona.tiempo_ref FROM persona WHERE persona.tipopersona='D' AND persona.estado=1")
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

def get_docentes_activos():
    conexion = obtener_conexion()
    docentes_activos = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS docentes_activos FROM persona WHERE tipopersona = 'D' AND estado = 1")
            column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
            row = cursor.fetchone()

            if row:
                docente_dict = dict(zip(column_names, row))  # Convertir la fila en un diccionario
                docentes_activos.append(docente_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return docentes_activos
def docentes_validar_horas():
    conexion = obtener_conexion()
    docentes_activos = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idpersona,nombres,apellidos,cantHoras FROM persona WHERE tipopersona='D' AND cantHoras<=6;")
            column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
            row = cursor.fetchone()

            if row:
                docente_dict = dict(zip(column_names, row))  # Convertir la fila en un diccionario
                docentes_activos.append(docente_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return docentes_activos


##OBTENER DOCENTE POR ID

def obtener_docente_por_id(idpersona):
    conexion = obtener_conexion()
    persona = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM persona WHERE idpersona = %s", (idpersona,))
            persona = cursor.fetchone()
            if persona:
                columnas = [desc[0] for desc in cursor.description]  # Obtiene los nombres de las columnas
                persona_dict = dict(zip(columnas, persona))  # Convierte la tupla en un diccionario
                return persona_dict
            else:
                return {"error": "Docente no encontrado"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def obtener_docente_por_nombre(nombres):
    conexion = obtener_conexion()
    persona = None
    try:
        with conexion.cursor() as cursor:
            query = """
            SELECT * FROM persona 
            WHERE CONCAT(nombres, ' ', apellidos) = %s 
            AND tipopersona = 'D'
            """
            cursor.execute(query, (nombres,))
            persona = cursor.fetchone()
            if persona:
                columnas = [desc[0] for desc in cursor.description]  # Obtiene los nombres de las columnas
                persona_dict = dict(zip(columnas, persona))  # Convierte la tupla en un diccionario
                return persona_dict
            else:
                return {"error": "Docente no encontrado"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
        

## CARGA MASIVA CURSOS 
def asignar_docente_excel(nombres, apellidos, n_documento, telefono, correo, tipopersona, cantHoras, tiempo_ref, estado):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Persona_Gestion', [1, None, nombres, apellidos, n_documento, telefono, correo, tipopersona, cantHoras, tiempo_ref, estado])
            conexion.commit()
            return {"mensaje": "Docente agregado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()


    