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



def actualizar_docentes_curso(cursoid, docenteid):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_CursosDocente_Gestion', [2, cursoid, docenteid])
            conexion.commit()
            return {"status": "success", "message": "Curso por docente actualizado correctamente"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
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

#### PARA LA TABLA

def datosCursoxDocente(escuela, semestre):
    conexion = obtener_conexion()
    cursos = []
    with conexion.cursor() as cursor:
        cursor.execute('''SELECT C.idcurso,G.id_grupo,C.ciclo as ciclo, C.nombre as curso, G.nombre as grupo,
                            COALESCE(D.docentes, 'No tiene docente asignado') AS docentes
                        FROM grupo G INNER JOIN curso C ON G.idcurso = C.idcurso
                        INNER JOIN plan_estudio PE ON C.id_plan_estudio = PE.id_plan_estudio
                        INNER JOIN escuela E ON PE.id_escuela = E.id_escuela
                        LEFT JOIN (
                            SELECT 
                                CD.idcurso,
                                GROUP_CONCAT(CONCAT(P.apellidos, ' ', P.nombres) SEPARATOR ', ') AS docentes
                            FROM curso_docente CD
                            INNER JOIN persona P ON P.idpersona = CD.idpersona
                            GROUP BY CD.idcurso
                        ) D ON G.id_grupo = D.idcurso
                            WHERE E.id_escuela = %s AND G.idsemestre = %s
                            ORDER BY curso,grupo
                                    ;
        ''', (escuela,semestre))
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            curso_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            cursos.append(curso_dict)

    conexion.close()
    return cursos

def ver_docente_grupo(idcurso):
    conexion = obtener_conexion()
    docentes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT CONCAT(P.nombres, ' ', P.apellidos) AS docente 
                FROM curso_docente CD
                INNER JOIN grupo G ON G.id_grupo = CD.idcurso
                INNER JOIN persona P ON P.idpersona = CD.idpersona
                WHERE G.id_grupo = %s
            """, (idcurso,))
            resultados = cursor.fetchall()
            for row in resultados:
                docentes.append(row[0])  # Añadir solo el nombre del docente a la lista
            if docentes:
                return {"docentes": docentes}
            else:
                return {"error": "Docentes de grupo no encontrados"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

## OBTENER ID ESCUELA
def obtener_idescuela(escuela):
    conexion = obtener_conexion()
    id = None  
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id_escuela FROM escuela WHERE nombre = %s", (escuela,))
            result = cursor.fetchone()
            if result:
                id = result[0]
    except Exception as e:
        print(f"Error al obtener ID Escuela: {e}")
    finally:
        conexion.close()
    return id

def asignar_docentes_a_grupo(grupoId, docentes, eliminados):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Eliminar docentes
            if eliminados:
                query = 'DELETE FROM curso_docente WHERE idcurso = %s AND idpersona IN (' + ','.join(['%s'] * len(eliminados)) + ')'
                cursor.execute(query, [grupoId] + eliminados)

            # Asignar nuevos docentes
            for docenteId in docentes:
                cursor.execute('''
                    INSERT INTO curso_docente (idcurso, idpersona) 
                    VALUES (%s, %s)
                    ON DUPLICATE KEY UPDATE idpersona = idpersona
                ''', (grupoId, docenteId))

        conexion.commit()
        return True, None
    except Exception as e:
        conexion.rollback()
        print(f"Error al asignar docentes: {e}")
        return False, str(e)
    finally:
        conexion.close()


## OBTENER DOCENTES POR GRUPO
def obtenerDocentesporGrupo(idcurso):
    conexion = obtener_conexion()
    docentes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute('''
                SELECT 
                    P.idpersona, 
                    CONCAT(P.apellidos, ' ', P.nombres) AS nombre
                FROM grupo G
                INNER JOIN curso C ON G.idcurso = C.idcurso 
                LEFT JOIN curso_docente CD ON G.id_grupo = CD.idcurso
                INNER JOIN persona P ON P.idpersona = CD.idpersona
                WHERE G.id_grupo = %s
            ''', (idcurso,))
            result = cursor.fetchall()
            if result:
                docentes = [{'idpersona': row[0], 'nombre': row[1]} for row in result]
    except Exception as e:
        print(f"Error al obtener los docentes del grupo {idcurso}: {e}")
    finally:
        conexion.close()
    return docentes



