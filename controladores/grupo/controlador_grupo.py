from bd import obtener_conexion

#Query Algoritmo Genetico
def get_grupo():
    conexion = obtener_conexion()
    grupo = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT grupo.id_grupo,grupo.nombre,grupo.vacantes,grupo.idcurso FROM grupo")
        grupo = cursor.fetchall()
    conexion.close()
    return grupo

