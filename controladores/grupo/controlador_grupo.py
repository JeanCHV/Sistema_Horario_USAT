from bd import obtener_conexion

#
def obtener_cursoxescuela(escuela, semestre):
    conexion = obtener_conexion()
    cursos = []
    with conexion.cursor() as cursor:
        cursor.execute('''SELECT 
                                        c.idcurso, 
                                        c.nombre, 
                                        c.ciclo, 
                                        COUNT(g.id_grupo) AS total_grupos
                                    FROM 
                                        curso AS c
                                    INNER JOIN 
                                        plan_estudio AS pe ON c.id_plan_estudio = pe.id_plan_estudio
                                    INNER JOIN 
                                        escuela AS es ON pe.id_escuela = es.id_escuela
                                    LEFT JOIN 
                                        grupo AS g ON c.idcurso = g.idcurso
                                    WHERE 
                                        es.nombre = %s and g.idsemestre = %s
                                    GROUP BY 
                                        c.idcurso, c.nombre, c.ciclo;
                                    ;
        ''', (escuela,semestre))
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            curso_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            cursos.append(curso_dict)

    conexion.close()
    return cursos

#OBTENER GRUPO POR ID
def obtener_grupo_por_id(id_grupo):
    conexion = obtener_conexion()
    grupo = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM grupo WHERE id_grupo = %s", (id_grupo,))
            persona = cursor.fetchone()
            if persona:
                columnas = [desc[0] for desc in cursor.description]  # Obtiene los nombres de las columnas
                persona_dict = dict(zip(columnas, grupo))  # Convierte la tupla en un diccionario
                return persona_dict
            else:
                return {"error": "Grupo no encontrado"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
     
def obtener_idsemestre(semestre):
    conexion = obtener_conexion()
    id = None  # Inicializar id como None en lugar de una lista
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idsemestre FROM semestre_academico WHERE descripcion = %s", (semestre,))
            result = cursor.fetchone()
            if result:
                id = result[0]
    except Exception as e:
        print(f"Error al obtener idsemestre: {e}")
    finally:
        conexion.close()
    return id

#obtener el total de los grupos
def obtener_total_grupo(escuela,id_semestre, id_curso):
    conexion = obtener_conexion()
    total_grupo = None  
    try:
        with conexion.cursor() as cursor:
            cursor.execute('''SELECT 
                COUNT(g.id_grupo) AS total_grupos
            FROM 
                curso AS c
            INNER JOIN 
                plan_estudio AS pe ON c.id_plan_estudio = pe.id_plan_estudio
            INNER JOIN 
                escuela AS es ON pe.id_escuela = es.id_escuela
            LEFT JOIN 
                grupo AS g ON c.idcurso = g.idcurso
            WHERE 
                es.nombre = %s 
                AND g.idsemestre = %s
                AND c.idcurso = %s
            ''', (escuela,id_semestre,id_curso))
            result = cursor.fetchone()
            if result:
                total_grupo = result[0]
    except Exception as e:
        print(f"Error al obtener idsemestre: {e}")
    finally:
        conexion.close()
    return total_grupo

##retorna ids a borrar
def ids_eliminar(escuela, id_semestre, id_curso, restante):
    conexion = obtener_conexion()
    total_grupo = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute('''
                SELECT 
                    g.id_grupo,
                    COUNT(g.id_grupo) AS total_grupos
                FROM 
                    curso AS c
                INNER JOIN 
                    plan_estudio AS pe ON c.id_plan_estudio = pe.id_plan_estudio
                INNER JOIN 
                    escuela AS es ON pe.id_escuela = es.id_escuela
                LEFT JOIN 
                    grupo AS g ON c.idcurso = g.idcurso
                WHERE 
                    es.nombre = %s 
                    AND g.idsemestre = %s 
                    AND c.idcurso = %s
                GROUP BY 
                    c.idcurso, c.nombre, c.ciclo, g.id_grupo, g.nombre
                LIMIT 18446744073709551615 OFFSET %s;
            ''', (escuela, id_semestre, id_curso, restante))
            total_grupo = cursor.fetchall()

    except Exception as e:
        print(f"Error al obtener ids a eliminar : {e}")
    finally:
        conexion.close()
    
    return total_grupo

#Query Algoritmo Genetico
def get_grupo():
    conexion = obtener_conexion()
    grupos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_grupo, nombre, vacantes, idcurso FROM grupo")
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()
        for row in rows:
            grupo_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            grupos.append(grupo_dict)
    conexion.close()
    return grupos


def manejo_grupos(datos):
    conexion = obtener_conexion()  # Obtener conexión a la base de datos
    semestre = datos.get('semestre')
    escuela = datos.get('escuela')
    mensaje = "correcto"
    try:
        with conexion.cursor() as cursor:
            for data in datos['valores']:
                id_curso = data.get('id')
                n_grupos = int(data.get('valor'))
                id_semestre = obtener_idsemestre(semestre)       
                total_group = obtener_total_grupo(escuela, id_semestre, id_curso)
                if total_group < n_grupos:
                    iteracion = n_grupos - total_group
                    vacante = 15
                    for numeros in range(iteracion):
                        grupo = chr(65 + total_group + numeros)
                        # Aquí podrías llamar a la función para agregar grupo
                        agregar_grupo(grupo, vacante, id_curso, id_semestre)
                        #print(f"Agregando grupo: {grupo}")
               
                elif total_group == n_grupos:
                    faltante = n_grupos
                else:
                    faltante = n_grupos
                    idss_eliminar = ids_eliminar(escuela, id_semestre, id_curso, faltante)
                    #print(f"IDs a eliminar: {idss_eliminar}")       
                    for id_eliminar in idss_eliminar:
                        id_grupo = id_eliminar[0]
                        eliminar_grupo(id_grupo)
                        #print(f"Eliminando grupo con ID: {id_grupo}")     
                    #print("Eliminamos")
            conexion.commit()
           # print("Transacción completada correctamente.")  
    except Exception as e:
        conexion.rollback() 
        mensaje = "fallo"
        #print(f"Error en manejo de grupos: {e}")
    finally:
        conexion.close()
    return mensaje

def obtener_grupos():
    conexion = obtener_conexion()
    grupos = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT G.id_grupo,G.nombre, G.vacantes, C.nombre as curso,S.descripcion FROM grupo G inner join semestre_academico S on S.idsemestre=G.idsemestre inner join curso C on C.idcurso = G.idcurso")
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            grupos_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            grupos.append(grupos_dict)

    conexion.close()
    return grupos

def obtener_grupo_por_id(id_grupo):
    conexion = obtener_conexion()
    grupo = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM grupo WHERE id_grupo = %s", (id_grupo,))
            grupo = cursor.fetchone()
            if grupo:
                columnas = [desc[0] for desc in cursor.description]  # Obtiene los nombres de las columnas
                grupo_dict = dict(zip(columnas, grupo))  # Convierte la tupla en un diccionario
                return grupo_dict
            else:
                return {"error": "Grupo no encontrado"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def agregar_grupo(nombre, vacantes, idcurso, idsemestre):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO grupo (nombre, vacantes, idcurso, idsemestre) VALUES (%s, %s, %s, %s)",
                           (nombre, vacantes, idcurso, idsemestre))
            conexion.commit()
            return {"mensaje": "Grupo agregado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()


def eliminar_grupo(id_grupo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Grupo_Gestion', [4, id_grupo, None, None, None,None])
            conexion.commit()
            return {"mensaje": "Grupo eliminado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def dar_baja_grupo(id_grupo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Grupo_Gestion', [3, id_grupo, None, None, None,None])
            conexion.commit()
            return {"mensaje": "Grupo dado de baja correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def modificar_grupo(id_grupo, nombre,vacantes, idcurso, idsemestre):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.callproc('sp_Grupo_Gestion', [2, id_grupo,nombre,vacantes,idcurso, idsemestre])
            conexion.commit()
            return {"mensaje": "Grupo modificado correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()



def retornar_grupos():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('''
            SELECT COUNT(DISTINCT p.idpersona) AS total_docentes, COUNT(DISTINCT CASE WHEN dd.idpersona IS NOT NULL THEN 
                       p.idpersona END) AS docentes_con_disponibilidad, COUNT(DISTINCT CASE WHEN dd.idpersona IS NULL THEN p.idpersona END)
                        AS docentes_sin_disponibilidad FROM persona p LEFT JOIN docente_disponibilidad dd ON p.idpersona = dd.idpersona WHERE p.tipopersona = 'D';
                       ''')
        rows = cursor.fetchone()
    conexion.close()
    return rows

def retornar_docentes():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('''
                SELECT 
                    COUNT(DISTINCT c.idcurso) AS total_cursos,
                    COUNT(DISTINCT g.id_grupo) AS total_grupos,
                    COUNT(DISTINCT CASE WHEN h.idhorario IS NOT NULL THEN g.id_grupo END) AS grupos_con_horario,
                    COUNT(DISTINCT CASE WHEN h.idhorario IS NULL THEN g.id_grupo END) AS grupos_sin_horario
                FROM 
                    curso c
                LEFT JOIN 
                    grupo g ON c.idcurso = g.idcurso
                LEFT JOIN 
                    horario h ON g.id_grupo = h.id_grupo
                INNER JOIN 
                    semestre_academico se ON se.idsemestre = g.idsemestre
                WHERE 
                    se.descripcion = '2024-I';

                       ''')
        rows = cursor.fetchone()
    conexion.close()
    return rows

#DASHBOARD
def get_cant_grupos_semestre():
    conexion = obtener_conexion()
    grupos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT sa.descripcion AS semestre,COUNT(g.id_grupo) AS cantidad_grupos FROM grupo g JOIN semestre_academico sa ON g.idsemestre=sa.idsemestre GROUP BY sa.descripcion;")
        column_names = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()
        for row in rows:
            grupo_dict = dict(zip(column_names, row))  # Convertir cada fila en un diccionario
            grupos.append(grupo_dict)
    conexion.close()
    return grupos

