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

## OBTENER LOS CURSOS CON SUS DATOS EN LA TABLA GENERAL
def obtener_datos_cursos():
    conexion = obtener_conexion()
    cursos = []

    with conexion.cursor() as cursor:
        cursor.execute("""
    SELECT c.idcurso,c.nombre, c.cod_curso, c.creditos, c.horas_teoria, c.horas_practica, 
           CASE c.tipo_curso when 0 then 'PRESENCIAL' when 1 then 'VIRTUAL'
           END as tipo_curso, c.ciclo, p.nombre AS nombre_plan_estudio, c.estado
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

def ver_detalle_cursos(idcurso):
   conexion = obtener_conexion()
   curso = None
   try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT c.idcurso, c.nombre, c.cod_curso, c.creditos, c.horas_teoria, c.horas_practica, c.ciclo,
                       CASE c.tipo_curso WHEN 0 THEN 'PRESENCIAL' WHEN 1 THEN 'VIRTUAL' END as tipo_curso,
                       CASE c.estado WHEN 'A' THEN 'ACTIVO' WHEN 'I' THEN 'INACTIVO' END as estado,
                       p.nombre AS nombre_plan_estudio
                FROM curso c
                JOIN plan_estudio p ON c.id_plan_estudio = p.id_plan_estudio
                WHERE c.idcurso = %s
            """, (idcurso,))
            curso = cursor.fetchone()
            if curso:
                columnas = [desc[0] for desc in cursor.description]  
                curso_dict = dict(zip(columnas, curso)) 
                return curso_dict
            else:
                return {"error": "Curso no encontrado"}
   except Exception as e:
        return {"error": str(e)}
   finally:
        conexion.close()

##MEJORAR
def agregar_curso(nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo, tipo_curso, estado, id_plan_estudio):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Curso_Gestion', [1, None, nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo, tipo_curso, estado, id_plan_estudio])
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
            cursor.callproc('sp_Curso_Gestion', [4, idcurso, None, None, None, None, None, None, None, None, None])
            conexion.commit()
            return {"mensaje": "Curso eliminado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def modificar_curso(idcurso, nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo, tipo_curso, estado, id_plan_estudio):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Curso_Gestion', [2, idcurso, nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo, tipo_curso, estado, id_plan_estudio])
            conexion.commit()
            return {"mensaje": "Curso modificado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

##OBTENER CURSO POR ID

def obtener_curso_por_id(idcurso):
    conexion = obtener_conexion()
    curso = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM curso WHERE idcurso = %s", (idcurso,))
            curso = cursor.fetchone()
            if curso:
                columnas = [desc[0] for desc in cursor.description]  # Obtiene los nombres de las columnas
                curso_dict = dict(zip(columnas, curso))  # Convierte la tupla en un diccionario
                return curso_dict
            else:
                return {"error": "Curso no encontrado"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()



## ALGORTIMO GENETICO 

def get_cursos():
    conexion = obtener_conexion()
    cursos = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT curso.idcurso,curso.nombre,curso.horas_teoria,curso.horas_practica,curso.tipo_curso,curso.ciclo FROM curso WHERE curso.estado='A'")
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            curso_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            cursos.append(curso_dict)

    conexion.close()
    return cursos


def obtener_cursosFiltro():
    conexion = obtener_conexion()
    cursos = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idcurso, nombre FROM curso")
            for plan in cursor.fetchall():
                cursos.append({'idcurso': plan[0], 'nombre': plan[1]})
    finally:
        conexion.close()
    return cursos

#FILTRAR LOS CICLOS
def obtener_ciclos():
    conexion = obtener_conexion()
    ciclos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT DISTINCT ciclo FROM curso")
        ciclos = cursor.fetchall()
    conexion.close()
    return ciclos


def obtener_idcurso_por_nombre(nombre):
    conexion = obtener_conexion()
    curso = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idcurso FROM curso WHERE nombre = %s", (nombre,))
            curso = cursor.fetchone()
            if curso:
                columnas = [desc[0] for desc in cursor.description]  # Obtiene los nombres de las columnas
                curso_dict = dict(zip(columnas, curso))  # Convierte la tupla en un diccionario
                return curso_dict
            else:
                return {"error": "Curso no encontrado"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

