from bd import obtener_conexion

def obtener_usuarios():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idusuario, username, password, estado, idpersona, token FROM usuario")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios

def obtener_usuario_con_tipopersona_por_username(username):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT usu.idusuario, usu.username, usu.password, usu.estado, usu.idpersona, usu.token, per.tipopersona FROM usuario usu INNER JOIN persona per ON per.idpersona = usu.idpersona WHERE usu.username =  %s", (username,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def obtener_usuario_por_username(username):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idusuario, username, password, estado, idpersona, token FROM usuario WHERE username = %s", (username,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def obtener_usuario_por_id(id):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idusuario, username, password, estado, idpersona, token FROM usuario WHERE idusuario = %s", (id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def actualizar_token(username,token):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET token = %s WHERE username = %s",
                       (token,username))
    conexion.commit()
    conexion.close()