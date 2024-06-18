from bd import obtener_conexion

## ALGORTIMO GENETICO 

def get_curso_docente():
    conexion = obtener_conexion()
    cursos_docente = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM curso_docente ")
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            cursos_docente_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            cursos_docente.append(cursos_docente_dict)

    conexion.close()
    return cursos_docente

## DATOS CURSOS DOCENTES (NOMBRES)
def datos_cursos_docentes():
    conexion = obtener_conexion()
    cursos_docentes = []

    with conexion.cursor() as cursor:
        cursor.execute("""
    SELECT CD.idcurso, C.nombre AS nombreCurso, CD.idpersona, CONCAT(P.nombres, ' ', P.apellidos) AS 
    nombreDocente FROM curso_docente CD INNER JOIN curso C ON C.idcurso = CD.idcurso INNER JOIN 
    persona P ON CD.idpersona = P.idpersona;
    """)
        column_names = [desc[0] for desc in cursor.description]  
        rows = cursor.fetchall()

        for row in rows:
            curso_dict = dict(zip(column_names, row)) 
            cursos_docentes.append(curso_dict)

    conexion.close()
    return cursos_docentes

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
                WHERE C.estado = 'A' AND C.tipo_curso = 0
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            
            for row in rows:
                curso_dict = dict(zip(column_names, row))
                cursos.append(curso_dict)
    finally:
        conexion.close()
    return cursos

#PARA OBTENER A LOS DOCENTES
def obtener_docentes():
    conexion = obtener_conexion()
    docentes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""SELECT idpersona, CONCAT(nombres, ' ', apellidos) AS nombre, correo, telefono 
                           FROM persona WHERE tipopersona = 'D'""")
            column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
            rows = cursor.fetchall()

            for row in rows:
                curso_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
                docentes.append(curso_dict)
    finally:
        conexion.close()
    return docentes


def guardar_docentes_curso(curso_id, docentes):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            for docente_id in docentes:
                cursor.execute("""
                    INSERT INTO curso_docente(idcurso, idpersona) 
                    VALUES (%s, %s) AS new 
                    ON DUPLICATE KEY UPDATE idpersona = new.idpersona
                """, (curso_id, docente_id))
        
        conexion.commit()
        return {'status': 'success'}
    except Exception as e:
        print(e)
        return {'status': 'error', 'message': str(e)}
    finally:
        conexion.close()
    

def eliminar_cursoxambiente(idcurso, idpersona):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_CursosDocente_Gestion', [3, idcurso, idpersona])
            conexion.commit()
            return {"mensaje": "Docente por Curso eliminado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()


def asignar_curso_docentes_excel(idcurso, iddocente):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_CursosDocente_Gestion', [1, idcurso, iddocente])
            conexion.commit()
            return {"mensaje": f"Curso {idcurso} asignado a docente {iddocente} correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()



