from main import app
from flask import request, session, redirect, url_for,jsonify

#Algorithm 
import algorithm.algorithm as algoritmo
#import algorithm.algorithm_pruebaJenkz as algoritmoJenkz
import controladores.controlador_horario as controlador_horario

#ALGORITHM
@app.route('/generarHorario', methods=['GET'])
def obtener_horarios():
    try:
        horario = algoritmo.algoritmo_genetico()
        return jsonify(horario)
    except Exception as e:
        return jsonify({"error": str(e)})
    
# PRUEBA ALGORITMO - JENKZ
# @app.route('/generarHorario_Jenkz', methods=['GET'])
# def obtener_horariosJenkz():
#     try:
#         horario = algoritmoJenkz.algoritmo_genetico()
#         return jsonify(horario)
#     except Exception as e:
#         return jsonify({"error": str(e)})

@app.route("/insertar_horarios_ia", methods=["POST"])
def insertar_horarios_ia():
    data = request.get_json()
    horarios = data.get('horariosgenerado')
    if not horarios:
        return jsonify({"error": "No se proporcionaron horarios"}), 400
    resultado = controlador_horario.insertar_horarios_ia(horarios)
    if "error" in resultado:
        return jsonify(resultado), 500

    return jsonify(resultado), 200