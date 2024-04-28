from bd import obtenerConexion

def obtener_personas():
    conexion = obtenerConexion()
    personas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idpersona,nombres,apellidos,n_documento,telefono,correo,tipopersona,cantHoras,tiempo_ref,foto FROM persona")
        personas = cursor.fetchall()
    conexion.close()
    return personas


def obtener_persona_por_id(id):
    conexion = obtenerConexion()
    persona = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idpersona,nombres,apellidos,n_documento,telefono,correo,tipopersona,cantHoras,tiempo_ref,foto FROM persona WHERE idpersona = %s", (id,))
        persona = cursor.fetchone()
    conexion.close()
    return persona

def obtener_persona_por_dni(dni):
    conexion = obtenerConexion()
    persona = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idpersona,nombres,apellidos,n_documento,telefono,correo,tipopersona,cantHoras,tiempo_ref,foto FROM persona WHERE idpersona = %s", (dni,))
        persona = cursor.fetchone()
    conexion.close()
    return persona