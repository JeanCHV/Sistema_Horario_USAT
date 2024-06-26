#Librerias y Recursos de Flask
from flask import (Flask,render_template,request,redirect,jsonify,url_for,make_response,session,)

import os
import hashlib
import datetime
import random
import time
########################################################################

#Importar app
from werkzeug.utils import secure_filename
from bd import obtener_conexion
from main import app
#Controladores para consultas al servidor
import controladores.controlador_usuario as controlador_usuario
import controladores.ambientes.controlador_ambiente as controlador_ambientes
import controladores.cursos.controlador_cursos as controlador_cursos
import controladores.controlador_persona as controlador_persona
import controladores.controlador_semestre as controlador_semestre
import controladores.controlador_horario as controlador_horario
import controladores.docente.controlador_docente as controlador_docente
import controladores.grupo.controlador_grupo as controlador_grupo
import controladores.curso_ambiente.controlador_curso_ambiente as controlador_curso_ambiente
import controladores.curso_docente.controlador_curso_docente as controlador_curso_docente
import controladores.controlador_edificio as controlador_edificio
import controladores.disponibilidad.controlador_disponibilidad as controlador_disponibilidad
import controladores.docente_disponibilidad.controlador_docente_disponibilidad as controlador_docente_disponibilidad

##DATOS CURSOS
@app.route("/datos_cursos", methods=["GET"])
def datos_cursos():
    cursos = controlador_cursos.obtener_cursos_Activos()
    return jsonify(cursos)

@app.route("/get_semestre", methods=["GET"])
def get_semestre():
    semestre = controlador_semestre.get_semestre()
    return jsonify(semestre)

@app.route("/get_ambiente_semestre", methods=["POST"])
def get_ambiente_semestre():
    nombre = request.json.get('nombre')
    semestre = controlador_ambientes.obtener_ambiente_semestre(nombre)
    return jsonify(semestre)

##VER DETALLES CURSOS

@app.route("/ver_cursos/<int:idcurso>", methods=["GET"])
def ver_detalles_cursos(idcurso):
    cursos = controlador_cursos.ver_detalle_cursos(idcurso)
    return jsonify(cursos)

##OBTENER PLANES DE ESTUDIO
@app.route('/obtener_planes_estudio', methods=['GET'])
def obtener_PE():
    planes_de_estudio = controlador_cursos.obtener_planes_de_estudio()  
    return jsonify(planes_de_estudio)

##AGREGAR CURSO 
@app.route("/agregar_curso", methods=["POST"])
def agregar_curso():
    try:
        nombre = request.json.get('nombre')
        cod_curso = request.json.get('cod_curso')
        creditos = request.json.get('creditos')
        horas_teoria = request.json.get('horas_teoria')
        horas_practica = request.json.get('horas_practica')
        ciclo = request.json.get('ciclo')
        tipo_curso = request.json.get('tipo_curso')
        estado = request.json.get('estado')
        id_plan_estudio = request.json.get('id_plan_estudio')

        # Verificar que todos los campos requeridos estén presentes
        if not all([nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo, tipo_curso, estado, id_plan_estudio]):
            return jsonify({"error": "Todos los campos son obligatorios"}), 400
        
        resultado = controlador_cursos.agregar_curso(nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo, tipo_curso, estado, id_plan_estudio)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
    

    
@app.route("/obtener_idcurso_por_nombre", methods=["POST"])
def obtener_idcurso_por_nombre():
    try:
        nombre = request.json.get('nombre')

        # Verificar que todos los campos requeridos estén presentes
        if not all([nombre]):
            return jsonify({"error": "Todos los campos son obligatorios"}), 400
        
        resultado = controlador_cursos.obtener_idcurso_por_nombre(nombre)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/asignar_curso_docentes_excel", methods=["POST"])
def asignar_curso_docentes_excel():
    try:
        asignaciones = request.json
        if not asignaciones:
            return jsonify({"error": "No se proporcionaron asignaciones"}), 400

        resultados = []
        for asignacion in asignaciones:
            idcurso = asignacion.get('idcurso')
            iddocente = asignacion.get('iddocente')

            if not idcurso or not iddocente:
                return jsonify({"error": "Todos los campos son obligatorios"}), 400

            resultado = controlador_curso_docente.asignar_curso_docentes_excel(idcurso, iddocente)
            resultados.append(resultado)

        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    
    

##ELIMINAR CURSO
@app.route("/eliminar_curso", methods=["POST"])
def eliminar_curso():
    try:
        data = request.get_json()  
        idcurso = data.get('idcurso')  
        resultado = controlador_cursos.eliminar_curso(idcurso)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})


##MODIFICAR CURSO
@app.route("/modificar_curso", methods=["POST"])
def modificar_curso():
    try:
        data = request.json
        idcurso = data.get('idcurso')
        nombre = data.get('nombre')
        cod_curso = data.get('cod_curso')
        creditos = data.get('creditos')
        horas_teoria = data.get('horas_teoria')
        horas_practica = data.get('horas_practica')
        ciclo = data.get('ciclo')
        tipo_curso = data.get('tipo_curso')
        estado = data.get('estado')
        id_plan_estudio = data.get('id_plan_estudio')
        resultado = controlador_cursos.modificar_curso(idcurso, nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo, tipo_curso, estado, id_plan_estudio)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
    
##OBTENER CURSO POR ID

@app.route('/obtener_curso/<int:idcurso>', methods=['GET'])
def obtener_curso_id(idcurso):
    resultado = controlador_cursos.obtener_curso_por_id(idcurso)
    return jsonify(resultado)

## DAR BAJA CURSO

@app.route("/dar_baja_curso", methods=["POST"])
def dar_baja_curso():
    try:
        data = request.json
        idcurso = data.get('idcurso')
        resultado = controlador_cursos.dar_baja_curso(idcurso)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
    
### CAMBIAR ESTADO CURSOS
@app.route('/curso_estado', methods=['POST'])
def curso_estado():
    data = request.get_json()
    idcurso = data.get('idcurso')
    nuevo_estado = data.get('estado')

    resultado = controlador_cursos.cambiar_estado_curso(idcurso, nuevo_estado)
    if "error" in resultado:
        return jsonify({'error': resultado["error"]}), 500
    else:
        return jsonify({'mensaje': resultado["mensaje"]}), 200

## CARGA MASIVA CURSOS 
@app.route("/asignar_cursos_excel", methods=["POST"])
def asignar_cursos_excel():
    try:
        asignaciones = request.json
        if not asignaciones:
            return jsonify({"error": "No se proporcionaron asignaciones"}), 400

        resultados = []
        for asignacion in asignaciones:
            nombre = asignacion.get('nombre')
            cod_curso = asignacion.get('cod_curso')
            creditos = asignacion.get('creditos')
            horas_teoria = asignacion.get('horas_teoria')
            horas_practica = asignacion.get('horas_practica')
            ciclo = asignacion.get('ciclo')
            tipo_curso = asignacion.get('tipo_curso')
            estado = asignacion.get('estado')
            id_plan_estudio = asignacion.get('id_plan_estudio')

            # Verificar que todos los campos requeridos estén presentes
            if not all(key in asignacion for key in ['nombre', 'cod_curso', 'creditos', 'horas_teoria', 'horas_practica', 'ciclo', 'tipo_curso', 'estado', 'id_plan_estudio']):
                return jsonify({"error": "Todos los campos son obligatorios"}), 400

            resultado = controlador_cursos.asignar_curso_excel(nombre, cod_curso, creditos, horas_teoria, horas_practica, ciclo, tipo_curso, estado, id_plan_estudio)
            resultados.append(resultado)

        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500    