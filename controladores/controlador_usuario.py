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

##PARA EL APATARDO DE PERFIL
def obtener_datos_usuario (id):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT p.nombres, p.apellidos, p.n_documento, p.correo, p.telefono, u.username, p.foto FROM persona p inner join usuario u on p.idpersona = u.idpersona WHERE idusuario = %s", (id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

# Función para actualizar los datos del usuario
def actualizar_datos_usuario(id, nombres, apellidos, n_documento, correo, telefono):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE persona SET nombres = %s, apellidos = %s, n_documento = %s, correo = %s, telefono = %s WHERE idpersona = (SELECT idpersona FROM usuario WHERE idusuario = %s)",
                           (nombres, apellidos, n_documento, correo, telefono, id))
            conexion.commit()
            return {"mensaje": "Datos actualizados correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
