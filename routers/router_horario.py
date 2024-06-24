from main import app
from flask import request, session, redirect, url_for,jsonify

#Algorithm 
import algorithm.algorithm as algoritmo
import algorithm.algorithm_pruebaJenkz as algoritmoJenkz


#ALGORITHM
@app.route('/generarHorario', methods=['GET'])
def obtener_horarios():
    try:
        horario = algoritmo.algoritmo_genetico()
        return jsonify(horario)
    except Exception as e:
        return jsonify({"error": str(e)})
    
# PRUEBA ALGORITMO - JENKZ
@app.route('/generarHorario_Jenkz', methods=['GET'])
def obtener_horariosJenkz():
    try:
        horario = algoritmoJenkz.algoritmo_genetico()
        return jsonify(horario)
    except Exception as e:
        return jsonify({"error": str(e)})