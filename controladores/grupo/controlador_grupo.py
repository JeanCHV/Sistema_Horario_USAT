from bd import obtener_conexion

#
def obtener_cursoxescuela(escuela):
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
                                        es.nombre = %s
                                    GROUP BY 
                                        c.idcurso, c.nombre, c.ciclo;
                                    ;
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

