from bd import obtener_conexion
## ALGORTIMO GENETICO 

def get_curso_ambiente():
    conexion = obtener_conexion()
    cursos_ambiente = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM curso_ambiente ")
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            cursos_ambiente_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            cursos_ambiente.append(cursos_ambiente_dict)

    conexion.close()
    return cursos_ambiente

## DATOS CURSOS AMBIENTES (NOMBRES)
def datos_cursos_ambientes():
    conexion = obtener_conexion()
    cursos_ambientes = []

    with conexion.cursor() as cursor:
        cursor.execute("""
    SELECT CA.idcurso, C.nombre as nombreCurso, CA.idambiente, A.nombre as nombreAmbiente FROM curso_ambiente CA inner join curso C on C.idcurso = CA.idcurso 
    inner join ambiente A on CA.idambiente = A.idambiente;
    """)
        column_names = [desc[0] for desc in cursor.description]  
        rows = cursor.fetchall()

        for row in rows:
            curso_dict = dict(zip(column_names, row)) 
            cursos_ambientes.append(curso_dict)

    conexion.close()
    return cursos_ambientes

### PARA MODAL CURSOS

def obtener_cursos_presenciales():
    conexion = obtener_conexion()
    cursos = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT C.idcurso, C.nombre, C.cod_curso as codigoCurso, C.ciclo, PE.nombre AS nombre_plan_estudio
                FROM curso C
                INNER JOIN plan_estudio PE ON PE.id_plan_estudio = C.id_plan_estudio
                WHERE C.estado = 'A' 
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            
            for row in rows:
                curso_dict = dict(zip(column_names, row))
                cursos.append(curso_dict)
    finally:
        conexion.close()
    return cursos


def obtener_ambientes():
    conexion = obtener_conexion()
    ambientes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT A.idambiente,A.nombre,A.aforo,E.nombre as nombreEdificio FROM ambiente A 
                           inner join edificio E on A.idedificio=E.idedificio where A.estado='A'
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            
            for row in rows:
                curso_dict = dict(zip(column_names, row))
                ambientes.append(curso_dict)
    finally:
        conexion.close()
    return ambientes


def guardar_ambientes_curso(curso_id, ambientes):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            for ambiente_id in ambientes:
                cursor.execute("""
                    INSERT INTO curso_ambiente (idcurso, idambiente) 
                    VALUES (%s, %s) AS new 
                    ON DUPLICATE KEY UPDATE idambiente = new.idambiente
                """, (curso_id, ambiente_id))
        
        conexion.commit()
        return {'status': 'success'}
    except Exception as e:
        print(e)
        return {'status': 'error', 'message': str(e)}
    finally:
        conexion.close()
    

def eliminar_cursoxambiente(idcurso, idambiente):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_CursosAmbiente_Gestion', [3, idcurso, idambiente])
            conexion.commit()
            return {"mensaje": "Ambiente por Curso eliminado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

### NUEVO
def obtener_cursos_con_ambientes(escuela, semestre):
    conexion = obtener_conexion()
    cursos = []
    with conexion.cursor() as cursor:
        cursor.execute('''
                SELECT DISTINCT C.idcurso,
       C.ciclo AS ciclo,
       C.nombre AS cursos,
       COALESCE(GROUP_CONCAT(DISTINCT A.nombre SEPARATOR ', '), 'No tiene ambiente asignado') AS ambientes
        FROM curso C
        LEFT JOIN curso_ambiente CA ON C.idcurso = CA.idcurso
        LEFT JOIN ambiente A ON CA.idambiente = A.idambiente
        LEFT JOIN grupo G ON G.idcurso = C.idcurso
        LEFT JOIN plan_estudio PE ON PE.id_plan_estudio = C.id_plan_estudio
        LEFT JOIN semestre_academico SA ON SA.idsemestre = G.idsemestre
        LEFT JOIN escuela E ON E.id_escuela = PE.id_escuela
        WHERE E.id_escuela = %s AND SA.idsemestre = %s
        GROUP BY C.idcurso, C.ciclo, C.nombre
        ''', (escuela, semestre))
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()
        for row in rows:
            curso_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            cursos.append(curso_dict)
    conexion.close()
    return cursos
        
def obtener_ambientes_curso(idcurso):
    conexion = obtener_conexion()
    ambientes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT A.idambiente, A.nombre
                FROM curso_ambiente CA
                INNER JOIN ambiente A ON A.idambiente = CA.idambiente
                WHERE CA.idcurso = %s
            """, (idcurso,))
            resultados = cursor.fetchall()
            for row in resultados:
                ambientes.append({"idambiente": row[0], "nombre": row[1]})
            return ambientes
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()


