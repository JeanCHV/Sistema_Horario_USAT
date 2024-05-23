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

def obtener_cursoxescuela(escuela,semestre):
    conexion = obtener_conexion()
    cursos = []
    with conexion.cursor() as cursor:
        cursor.execute('''
            SELECT 
                c.idcurso, 
                c.nombre, 
                c.ciclo, 
                COALESCE(grupo_count.contador, 0) AS n_grupos
            FROM 
                curso AS c
            INNER JOIN 
                plan_estudio AS pe ON c.id_plan_estudio = pe.id_plan_estudio
            INNER JOIN 
                escuela AS es ON pe.id_escuela = es.id_escuela
            LEFT JOIN (
                SELECT 
                    gr.idcurso, 
                    COUNT(*) AS contador
                FROM 
                    grupo AS gr
                INNER JOIN 
                    semestre_academico AS se ON gr.idsemestre = se.idsemestre
                WHERE 
                    se.descripcion = %s
                GROUP BY 
                    gr.idcurso
            ) AS grupo_count ON c.idcurso = grupo_count.idcurso
            WHERE 
                es.nombre = %s
            GROUP BY 
                c.idcurso, c.nombre, c.ciclo;

        ''', (semestre,escuela,))
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


def obtener_cursos():
    conexion = obtener_conexion()
    cursos = []
    with conexion.cursor() as cursor:
        cursor.execute("""
    SELECT c.nombre, c.cod_curso, c.creditos, c.horas_teoria, c.horas_practica, 
           CASE c.tipo_curso when 0 then 'PRESENCIAL' when 1 then 'VIRTUAL'
           END as tipo_curso, c.ciclo, p.nombre AS nombre_plan_estudio
    FROM curso c
    JOIN plan_estudio p ON c.id_plan_estudio = p.id_plan_estudio;
    """)
        column_names = [desc[0] for desc in cursor.description]  
        rows = cursor.fetchall()
        for row in rows:
            curso_dict = dict(zip(column_names, row)) 
            cursos.append(curso_dict)

    conexion.close()
    return cursos

##MEJORAR
def agregar_curso(nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO curso (nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo) VALUES (%s, %s, %s, %s, %s, %s)",
                           (nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo))
            conexion.commit()
            return {"mensaje": "Curso agregado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def obtener_planes_de_estudio():
    conexion = obtener_conexion()
    planes_de_estudio = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id_plan_estudio, nombre FROM plan_estudio")
            for plan in cursor.fetchall():
                planes_de_estudio.append({'id_plan_estudio': plan[0], 'nombre': plan[1]})
    finally:
        conexion.close()
    return planes_de_estudio


def eliminar_curso(idcurso):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Curso_Gestion', [4, idcurso, None, None, None, None, None, None])
            conexion.commit()
            return {"mensaje": "Curso eliminado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

##MEJORAR
def modificar_curso(idcurso, nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Curso_Gestion', [2, idcurso, nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo])
            conexion.commit()
            return {"mensaje": "Curso modificado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

