from bd import obtener_conexion

def obtener_reporte_horas():
    conexion = obtener_conexion()
    reporte = []
    try:
        with conexion.cursor() as cursor:
            query = """
            SELECT 
    p.idpersona AS docente_id,
    p.nombres AS nombre_docente,
    p.apellidos AS apellido_docente,
    sa.descripcion AS semestre,
    SUM(TIMESTAMPDIFF(HOUR, h.horainicio, h.horafin)) AS total_horas_clase
FROM 
    horario h
JOIN 
    persona p ON h.idpersona = p.idpersona
JOIN 
    grupo g ON h.id_grupo = g.id_grupo
JOIN 
    semestre_academico sa ON g.idsemestre = sa.idsemestre
WHERE 
    p.tipopersona = 'D'
    AND sa.estado = 1  -- Suponiendo que '1' significa 'Activo'
GROUP BY 
    p.idpersona, p.nombres, p.apellidos, sa.descripcion
ORDER BY 
    total_horas_clase DESC;

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