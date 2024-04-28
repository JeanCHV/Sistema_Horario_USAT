from bd import obtenerConexion

def obtener_usuarios():
    conexion = obtenerConexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idusuario, username, password, estado, idpersona, token FROM usuario")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios

def obtener_usuario_por_username(username):
    conexion = obtenerConexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idusuario, username, password, estado, idpersona, token FROM usuario WHERE username = %s", (username,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def obtener_usuario_por_id(id):
    conexion = obtenerConexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idusuario, username, password, estado, idpersona, token FROM usuario WHERE id = %s", (id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario
