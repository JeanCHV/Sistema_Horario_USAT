#Librerias y Recursos de Flask
from flask import (request,jsonify,)
########################################################################

#Importar app
from main import app
#Controladores para consultas al servidor

import controladores.docente.controlador_docente as controlador_docente

#GESTIONAR DOCENTE

@app.route("/datos_docentes", methods=["GET"])
def get_docentes():
    try:
        docentes = controlador_docente.datos_docentes()
        return jsonify(docentes)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/agregar_docente", methods=["POST"])
def agregar_docente():
    try:
        nombres = request.json.get('nombres')
        apellidos = request.json.get('apellidos')
        n_documento = request.json.get('n_documento')
        telefono = request.json.get('telefono')
        correo = request.json.get('correo')
        cantHoras = request.json.get('cantHoras')
        tiempo_ref = request.json.get('tiempo_ref')
        estado = request.json.get('estado')
        # Llama al controlador para agregar el docente
        resultado = controlador_docente.agregar_docente(nombres, apellidos, n_documento, telefono, correo, cantHoras, tiempo_ref, estado)


        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
@app.route("/obtener_docente_por_nombre", methods=["POST"])
def obtener_docente_por_nombre():
    try:
        nombres = request.json.get('nombres')
        # Llama al controlador para agregar el docente
        resultado = controlador_docente.obtener_docente_por_nombre(nombres)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/eliminar_docente", methods=["POST"])
def eliminar_docente():
    try:
        data = request.json
        idpersona = data.get('idpersona')
        resultado = controlador_docente.eliminar_docente(idpersona)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/modificar_docente", methods=["POST"])
def modificar_docente():
    try:
        data = request.json
        idpersona = data.get('idpersona')
        nombres = data.get('nombres')
        apellidos = data.get('apellidos')
        n_documento = data.get('n_documento')
        telefono = data.get('telefono')
        correo = data.get('correo')
        cantHoras = data.get('cantHoras')
        tiempo_ref = data.get('tiempo_ref')
        estado = data.get('estado')

        resultado = controlador_docente.modificar_docente(idpersona, nombres, apellidos, n_documento, telefono, correo, cantHoras, tiempo_ref, estado)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/obtener_docente_por_id/<int:idpersona>', methods=['GET'])
def obtener_docente_por_id(idpersona):
    resultado = controlador_docente.obtener_docente_por_id(idpersona)
    return jsonify(resultado)

## CARGA MASIVA DOCENTES 
@app.route("/asignar_docentes_excel", methods=["POST"])
def asignar_docentes_excel():
    try:
        asignaciones = request.json
        if not asignaciones:
            return jsonify({"error": "No se proporcionaron asignaciones"}), 400

        resultados = []
        for asignacion in asignaciones:
            nombres = asignacion.get('nombres')
            apellidos = asignacion.get('apellidos')
            n_documento = asignacion.get('n_documento')
            telefono = asignacion.get('telefono')
            correo = asignacion.get('correo')
            tipopersona = asignacion.get('tipopersona')
            cantHoras = asignacion.get('cantHoras')
            tiempo_ref = asignacion.get('tiempo_ref')
            estado = asignacion.get('estado')

            # Verificar que todos los campos requeridos estén presentes
            if not all(key in asignacion for key in ['nombres', 'apellidos', 'n_documento', 'telefono', 'correo', 'tipopersona', 'cantHoras', 'tiempo_ref', 'estado']):
                return jsonify({"error": "Todos los campos son obligatorios"}), 400

            resultado = controlador_docente.asignar_docente_excel(nombres, apellidos, n_documento, telefono, correo, tipopersona, cantHoras, tiempo_ref, estado)
            resultados.append(resultado)

        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  