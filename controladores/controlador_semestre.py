from bd import obtener_conexion

def obtener_semestres():
    conexion = obtener_conexion()
    semestres = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idsemestre,descripcion,estado FROM semestre_academico")
        semestres = cursor.fetchall()
    conexion.close()
    return semestres