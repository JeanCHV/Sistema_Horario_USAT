from bd import obtener_conexion

def obtener_semestres():
    conexion = obtener_conexion()
    semestres = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idsemestre,descripcion,estado FROM semestre_academico")
        semestres = cursor.fetchall()
    conexion.close()
    return semestres

def obtener_semestreCombo():
    conexion = obtener_conexion()
    semestre = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idsemestre, descripcion FROM semestre_academico")
            for plan in cursor.fetchall():
                semestre.append({'idsemestre': plan[0], 'descripcion': plan[1]})
    finally:
        conexion.close()
    return semestre


def get_semestre():
    conexion = obtener_conexion()
    semestre = []

    with conexion.cursor() as cursor:
        cursor.execute("""
SELECT idsemestre,descripcion,estado FROM semestre_academico
    """)
        column_names = [desc[0] for desc in cursor.description]  
        rows = cursor.fetchall()

        for row in rows:
            curso_dict = dict(zip(column_names, row)) 
            semestre.append(curso_dict)

    conexion.close()
    return semestre