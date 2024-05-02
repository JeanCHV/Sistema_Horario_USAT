from bd import obtener_conexion

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


# def obtener_usuario_con_tipopersona_por_username(username):
#     conexion = obtener_conexion()
#     usuario = None
#     with conexion.cursor() as cursor:
#         cursor.execute(
#             "SELECT usu.idusuario, usu.username, usu.password, usu.estado, usu.idpersona, usu.token, per.tipopersona FROM usuario usu INNER JOIN persona per ON per.idpersona = usu.idpersona WHERE usu.username =  %s", (username,))
#         usuario = cursor.fetchone()
#     conexion.close()
#     return usuario

# def obtener_usuario_por_username(username):
#     conexion = obtener_conexion()
#     usuario = None
#     with conexion.cursor() as cursor:
#         cursor.execute(
#             "SELECT idusuario, username, password, estado, idpersona, token FROM usuario WHERE username = %s", (username,))
#         usuario = cursor.fetchone()
#     conexion.close()
#     return usuario

# def obtener_usuario_por_id(id):
#     conexion = obtener_conexion()
#     usuario = None
#     with conexion.cursor() as cursor:
#         cursor.execute(
#             "SELECT idusuario, username, password, estado, idpersona, token FROM usuario WHERE id = %s", (id,))
#         usuario = cursor.fetchone()
#     conexion.close()
#     return usuario

# def actualizar_token(username,token):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("UPDATE usuario SET token = %s WHERE username = %s",
#                        (token,username))
#     conexion.commit()
#     conexion.close()