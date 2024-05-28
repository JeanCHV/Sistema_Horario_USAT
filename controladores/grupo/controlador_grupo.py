from bd import obtener_conexion

#
def obtener_cursoxescuela(escuela):
    conexion = obtener_conexion()
    cursos = []
    with conexion.cursor() as cursor:
        cursor.execute('''SELECT c.idcurso, c.nombre, c.ciclo 
            FROM curso AS c 
            INNER JOIN plan_estudio AS pe ON c.id_plan_estudio = pe.id_plan_estudio 
            INNER JOIN escuela AS es ON pe.id_escuela = es.id_escuela
            where es.nombre = %s;
        ''', (escuela))
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            curso_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            cursos.append(curso_dict)

    conexion.close()
    return cursos
     


#Query Algoritmo Genetico
def get_grupo():
    conexion = obtener_conexion()
    grupo = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT grupo.id_grupo,grupo.nombre,grupo.vacantes,grupo.idcurso FROM grupo")
        grupo = cursor.fetchall()
    conexion.close()
    return grupo

