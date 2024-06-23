from bd import obtener_conexion

def obtener_reporte_horas():
    conexion = obtener_conexion()
    reporte = []
    try:
        with conexion.cursor() as cursor:
            query = """
            SELECT 
                g.idsemestre,
                sa.descripcion AS semestre_descripcion,
                cd.idpersona AS docente_id,
                p.nombres AS docente_nombres,
                p.apellidos AS docente_apellidos,
                SUM(c.horas_teoria + c.horas_practica) AS total_horas
            FROM 
                curso c
            JOIN 
                curso_docente cd ON c.idcurso = cd.idcurso
            JOIN 
                grupo g ON c.idcurso = g.idcurso
            JOIN 
                persona p ON cd.idpersona = p.idpersona
            JOIN 
                semestre_academico sa ON g.idsemestre = sa.idsemestre
            WHERE 
                sa.estado = 1
            GROUP BY 
                g.idsemestre, sa.descripcion, cd.idpersona, p.nombres, p.apellidos
            ORDER BY 
                g.idsemestre, total_horas DESC;
            """
            cursor.execute(query)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                reporte_dict = dict(zip(column_names, row))
                reporte.append(reporte_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return reporte
