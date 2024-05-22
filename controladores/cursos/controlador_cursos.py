from bd import obtener_conexion


# def obtener_cursos():
#     conexion = obtener_conexion()
#     cursos = []

#     with conexion.cursor() as cursor:
#         cursor.execute("SELECT * FROM curso c")
#         column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
#         rows = cursor.fetchall()

#         for row in rows:
#             curso_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
#             cursos.append(curso_dict)

#     conexion.close()
#     return cursos

def obtener_curso(escuela):
    conexion = obtener_conexion()
    cursos = []
    with conexion.cursor() as cursor:
        cursor.execute('''
            SELECT c.idcurso, c.nombre, c.ciclo 
            FROM curso AS c 
            INNER JOIN plan_estudio AS pe ON c.id_plan_estudio = pe.id_plan_estudio 
            INNER JOIN escuela AS es ON pe.id_escuela = es.id_escuela
            WHERE es.nombre = %s;
        ''', (escuela,))
        nombres_columnas = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        filas = cursor.fetchall()
        for fila in filas:
            curso_dict = dict(zip(nombres_columnas, fila))  # Convertir cada fila en un diccionario
            cursos.append(curso_dict)
    conexion.close()
    return cursos

def obtener_semestres():
    conexion = obtener_conexion()
    semestres = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT descripcion FROM semestre_academico order by descripcion desc")
        semestres = cursor.fetchall()
    conexion.close()
    return semestres

def obtener_escuelas():
    conexion = obtener_conexion()
    escuelas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT nombre FROM escuela  where  estado = 'A'  order by nombre desc ")
        escuelas = cursor.fetchall()
    conexion.close()
    return escuelas



