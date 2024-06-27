from bd import obtener_conexion

## ALGORTIMO GENETICO


def get_grupo_docente():
    conexion = obtener_conexion()
    grupo_docente = []

    with conexion.cursor() as cursor:
        cursor.execute("SELECT idgrupo,idpersona from grupo_docente")
        column_names = [
            desc[0] for desc in cursor.description
        ]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            grupo_docente_dict = dict(
                zip(column_names, row)
            )  # Convertir cada fila en un diccionario
            grupo_docente.append(grupo_docente_dict)

    conexion.close()
    return grupo_docente


def get_docentes_no_asignados():
    conexion = obtener_conexion()
    docente_sin_asignar = []

    with conexion.cursor() as cursor:
        cursor.execute(
            """SELECT
	p.idpersona, 
	p.nombres, 
	p.apellidos
FROM
	persona AS p
	LEFT JOIN
	grupo_docente AS gd
	ON 
		p.idpersona = gd.idpersona
WHERE
	p.tipopersona = 'D' AND
	gd.idpersona IS NULL AND
	p.estado = 1;
"""
        )
        column_names = [
            desc[0] for desc in cursor.description
        ]  # Obtener los nombres de las columnas
        rows = cursor.fetchall()

        for row in rows:
            grupo_docente_dict = dict(
                zip(column_names, row)
            )  # Convertir cada fila en un diccionario
            docente_sin_asignar.append(grupo_docente_dict)

    conexion.close()
    return docente_sin_asignar

## OBTENER DOCENTES POR GRUPO
def obtenerDocentesporGrupo(idgrupo):
    conexion = obtener_conexion()
    docentes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute('''
                SELECT P.idpersona,CONCAT(P.apellidos,' ',P.nombres) AS docente FROM grupo_docente GD INNER JOIN grupo G ON G.id_grupo=GD.idgrupo
                INNER JOIN curso C ON C.idcurso=G.idcurso INNER JOIN persona P ON GD.idpersona=P.idpersona
                WHERE G.id_grupo= %s
            ''', (idgrupo,))
            result = cursor.fetchall()
            if result:
                docentes = [{'idpersona': row[0], 'nombre': row[1]} for row in result]
    except Exception as e:
        print(f"Error al obtener los docentes del grupo {idgrupo}: {e}")
    finally:
        conexion.close()
    return docentes

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
                                GD.idgrupo,
                                GROUP_CONCAT(CONCAT(P.apellidos, ' ', P.nombres) SEPARATOR ', ') AS docentes
                            FROM grupo_docente GD
                            INNER JOIN persona P ON P.idpersona = GD.idpersona
                            GROUP BY GD.idgrupo
                        ) D ON G.id_grupo = D.idgrupo
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

##ASIGNACION
def asignar_docentes_a_grupo(grupoId, docentes, eliminados):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Eliminar docentes
            if eliminados:
                query = 'DELETE FROM grupo_docente WHERE idgrupo = %s AND idpersona IN (' + ','.join(['%s'] * len(eliminados)) + ')'
                cursor.execute(query, [grupoId] + eliminados)

            # Asignar nuevos docentes
            for docenteId in docentes:
                cursor.execute('''
                    INSERT INTO grupo_docente (idgrupo, idpersona) 
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


def eliminar_asignaciones_docentes(idgrupo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Verificar si el idgrupo existe
            cursor.execute('''
                SELECT COUNT(*) FROM grupo_docente
                WHERE idgrupo = %s
            ''', (idgrupo,))
            result = cursor.fetchone()
            if result[0] == 0:
                print(f"El idgrupo {idgrupo} no existe en la tabla grupo_docente")
                return {'error': 'El idgrupo no existe en la tabla grupo_docente'}

            # Intentar eliminar las asignaciones
            print(f"Intentando eliminar asignaciones para el grupo {idgrupo}")
            cursor.execute('''
                DELETE FROM grupo_docente
                WHERE idgrupo = %s
            ''', (idgrupo,))
            filas_afectadas = cursor.rowcount
            print(f"Filas afectadas por la eliminación: {filas_afectadas}")

        conexion.commit()
        print("Eliminación completada exitosamente.")
        return {'success': True}
    except Exception as e:
        conexion.rollback()
        print(f"Error al eliminar asignaciones de docentes: {e}")
        return {'error': str(e)}
    finally:
        conexion.close()