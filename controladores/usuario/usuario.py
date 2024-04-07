import hashlib
import random
from bd import obtener_conexion


def obtener_usuarios():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idusuario, username,password,idpersona,idestado FROM usuario")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios