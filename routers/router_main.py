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

from routers.router_login import *
from routers.router_curso import *
from routers.router_docente import *
from routers.router_ambiente import *
from routers.router_horario import *

from routers.router_page_not_found import *


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
import controladores.grupo_docente.controlador_grupo_docente as controlador_grupo_docente

login_attempts = {}

@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login/login.html")

# @app.before_request
# def before_request():
#     session.modified = True
#     if 'idusuario' in session:
#         session['last_activity'] = datetime.datetime.now()

#DASHBOARD
@app.route("/get_cursos_activos", methods=["GET"])
def get_cursos_activos():
    cursos_activos = controlador_cursos.obtener_cursos_activos()
    return jsonify(cursos_activos)


@app.route("/get_docentes_activos", methods=["GET"])
def get_docentes_activos():
    docentes_activos = controlador_docente.get_docentes_activos()
    return jsonify(docentes_activos)


@app.route("/docentes_validar_horas", methods=["GET"])
def docentes_validar_horas():
    docentes_validar_horas = controlador_docente.docentes_validar_horas()
    return jsonify(docentes_validar_horas)

@app.route("/get_ambientes_disponibles", methods=["GET"])
def get_ambientes_disponibles():
    ambientes_activos = controlador_ambientes.get_ambientes_disponibles()
    return jsonify(ambientes_activos)

@app.route("/get_ambientes_capacidad_ocupacion", methods=["GET"])
def get_ambientes_capacidad_ocupacion():
    ambientes_capacidad_ocupacion = controlador_ambientes.get_ambientes_capacidad_ocupacion()
    return jsonify(ambientes_capacidad_ocupacion)

@app.route("/get_cursos_por_ciclo", methods=["GET"])
def get_cursos_por_ciclo():
    cursos_por_ciclo = controlador_cursos.obtener_cursos_por_ciclo()
    return jsonify(cursos_por_ciclo)


@app.route("/get_cursos_tipo", methods=["GET"])
def get_cursos_tipo():
    get_cursos_tipo = controlador_cursos.get_cursos_tipo()
    return jsonify(get_cursos_tipo)

@app.route("/get_edificio_ambientes", methods=["GET"])
def get_edificio_ambientes():
    get_edificio_ambientes = controlador_edificio.get_edificio_ambientes()
    return jsonify(get_edificio_ambientes)


@app.route("/get_reporte_cursos", methods=["GET"])
def get_reporte_cursos():
    get_reporte_cursos = controlador_horario.get_reporte_cursos()
    return jsonify(get_reporte_cursos)

@app.route("/get_cant_cursos_docente", methods=["GET"])
def get_cant_cursos_docente():
    get_cant_cursos_docente =  controlador_cursos.get_cant_cursos_docente()
    return jsonify(get_cant_cursos_docente)

@app.route("/get_cant_grupos_semestre", methods=["GET"])
def get_cant_grupos_semestre():
    grupos = controlador_grupo.get_cant_grupos_semestre()
    return jsonify(grupos)

#GRUPO PINEDA

@app.route('/obtener_grupo_por_id/<int:id_grupo>', methods=['GET'])
def obtener_grupo_por_id(id_grupo):
    resultado = controlador_grupo.obtener_grupo_por_id(id_grupo)
    return jsonify(resultado)

#AGREGAR AMBIENTE
@app.route("/agregar_ambiente", methods=["POST"])
def agregar_ambiente():
    try:
        nombre = request.json.get('nombre')
        aforo = request.json.get('aforo')
        estado = request.json.get('estado')
        idedificio = request.json.get('idedificio')
        idambientetipo = request.json.get('idambientetipo')

        # Realiza las validaciones necesarias aquí antes de agregar el ambiente

        # Llama al controlador para agregar el ambiente
        resultado = controlador_ambientes.agregar_ambiente(nombre, aforo, estado, idedificio, idambientetipo)

        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
#ELIMINAR AMBIENTE 
@app.route("/eliminar_ambiente", methods=["POST"])
def eliminar_ambiente_route():
    try:
        data = request.get_json()
        idambiente = data.get('idambiente')
        print(f"ID del ambiente a eliminar recibido: {idambiente}")
        resultado = controlador_ambientes.eliminar_ambiente(idambiente)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
    
#DAR DE BAJA AMBIENTE 
@app.route("/dar_baja_ambiente", methods=["POST"])
def dar_baja_ambiente_route():
    try:
        data = request.json
        idambiente = data.get('idambiente')
        resultado = controlador_ambientes.dar_baja_ambiente(idambiente,)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
#MODIFICAR AMBIENTE 

@app.route("/modificar_ambiente", methods=["POST"])
def modificar_ambiente_route():
    try:
        data = request.json
        idambiente = data.get('idambiente')
        nombre = data.get('nombre')
        aforo = data.get('aforo')
        estado = data.get('estado')
        idedificio = data.get('idedificio')
        idambientetipo = data.get('idambientetipo')
        resultado = controlador_ambientes.modificar_ambiente(idambiente, nombre, aforo, estado, idedificio, idambientetipo)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
##OBTENER AMBIENTE POR ID
@app.route('/get_ambiente/<int:idambiente>', methods=['GET'])
def get_ambiente(idambiente):
    resultado = controlador_ambientes.obtener_ambiente_por_id(idambiente)
    return jsonify(resultado)

### CAMBIAR ESTADO CURSOS
@app.route('/ambiente_estado', methods=['POST'])
def ambiente_estado():
    data = request.get_json()
    idambiente = data.get('idambiente')
    nuevo_estado = data.get('estado')

    resultado = controlador_ambientes.cambiar_estado_ambiente(idambiente, nuevo_estado)
    if "error" in resultado:
        return jsonify({'error': resultado["error"]}), 500
    else:
        return jsonify({'mensaje': resultado["mensaje"]}), 200

    
#Gestionar Perfil
#@app.route('/perfil', methods=["GET"])
#def perfil():
#    try:
#        usuario= controlador_usuario.obtener_usuario_por_id()
#        return jsonify(usuario)
#    except Exception as e:
#        return jsonify({"error": str(e)})


@app.route("/validar_sesion", methods=["POST"])
def get_datos_usuario():
    try:
        username = request.json.get('username')
        token = request.json.get('token')

        usuario = controlador_usuario.obtener_usuario_por_username(username)

        if usuario == None or username != usuario[1] or token != usuario[5] or not usuario[3]:
            return jsonify({'logeo':False,'alerta':'No hay una sesión activa, por favor vuelva a acceder al sistema'})
        else:
            return jsonify({'logeo':True}) 
    except Exception as e:
        return jsonify({'logeo':False,'alerta':str(e)})

@app.route("/index")
def index():
    return render_template("dashboard/home.html")
    


@app.route("/ambientes")
def ambientes():
    return render_template("dashboard/ambientes.html")

@app.route("/cursos")
def cursos():
    return render_template("dashboard/cursos.html")

@app.route("/grupos")
def grupos():
    return render_template("dashboard/grupos.html")

@app.route("/disponibilidad")
def disponibilidad():
    return render_template("dashboard/disponibilidad.html")

@app.route("/rellenar_tabla/<string:escuela>/<string:semestre>")
def rellenar_tabla(escuela,semestre):
    id_semestre = controlador_grupo.obtener_idsemestre(semestre)
    cursos = controlador_grupo.obtener_cursoxescuela(escuela,id_semestre)
    return jsonify(cursos)

@app.route('/mantenimiento_grupos', methods=['POST'])
def mantenimiento_grupos():
    datos = request.json
    mensaje = controlador_grupo.manejo_grupos(datos)
    if mensaje == "fallo":
        return jsonify({"mensaje": "Error al agregar grupos"})
    else:
        return jsonify({"mensaje": "Grupos modificados correctamente"})



@app.route('/get_registrodocente_grupo_horario')
def get_registrodocente_grupo_horario():
    try:
        grupos = controlador_grupo.retornar_grupos()
        docente = controlador_grupo.retornar_docentes()
        return jsonify({
            "docentes_con_disponibilidad": grupos[1],
            "docentes_sin_disponibilidad": grupos[2], 
            "grupos_con_horario": docente[2],    
            "grupos_sin_horario": docente[3]  
        })
    except Exception as e:
        print(f"Error en la consulta: {str(e)}")
        return jsonify({"error": "Error al obtener registros"}), 500

@app.route("/cursosxescuela")
def cursosxescuela():
    semestres = controlador_cursos.obtener_semestres()
    escuelas = controlador_cursos.obtener_escuelas()
    return render_template("dashboard/cursosxescuela.html", semestres=semestres, escuelas=escuelas)

@app.route("/usuario")
def usuario():
    return render_template("dashboard/usuario.html")

@app.route('/docentes', methods=["GET"])
def docentes():
    try:
        persona = controlador_docente.obtener_docentes()
        return render_template('dashboard/docentes.html', personas=persona)
    except Exception as e:
        return str(e), 500
    
@app.route("/horarios")
def horarios():
    persona = controlador_docente.obtener_docentes()
    semestres = controlador_semestre.obtener_semestres()
    return render_template("dashboard/horarios.html", docente=persona,semestre=semestres)

@app.route("/ReporteAmbiente")
def ReporteAmbiente():
    return render_template("dashboard/Reporte.html")

@app.route("/horarios_por_docente")
def horarios_por_docente():
    semestres = controlador_semestre.obtener_semestres()
    return render_template("horarios/horarios_por_docente.html",semestres=semestres)

@app.route("/get_personas_activas", methods=["GET"])
def get_personas_activas():
    personas_activas = controlador_persona.obtener_personas_activas()
    return jsonify(personas_activas)

@app.route("/get_personas_docentes_activas", methods=["GET"])
def get_personas_docentes_activas():
    personas_docentes_activas = controlador_persona.obtener_personas_docentes_activas()
    return jsonify(personas_docentes_activas)

@app.route("/get_horarios_docentesId_semestre", methods=["POST"])
def get_horarios_docentesNombres_semestre():
    id_docente = request.json.get('id_docente')
    semestre = request.json.get('semestre')
    horarios = controlador_horario.obtener_horarios_por_docenteId_semestre(id_docente,semestre)
    return jsonify(horarios)  
    
######### PERFIL ############
@app.route("/perfil")
def perfil():
    return render_template("dashboard/perfil.html")

####### DATOS DE LA PANTALLA PERFIL ##########
@app.route('/datos_usuario', methods=['GET'])
def api_obtener_usuario():
    user_id = session.get('user_id')  
    if user_id:
        usuario = controlador_usuario.obtener_datos_usuario(user_id)
        if usuario:
            return jsonify({
                'nombres': usuario[0],
                'apellidos': usuario[1],
                'n_documento': usuario[2],
                'correo': usuario[3],
                'telefono': usuario[4],
                'username': usuario[5],
                'foto': usuario[6]
            })
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    else:
        return jsonify({"error": "No autenticado"}), 401

###### MODIFICAR LOS DATOS DE LA PANTALLA PERFIL #########

@app.route('/actualizar_datos', methods=['POST'])
def api_actualizar_usuario():
    user_id = session.get('user_id')  # Suponiendo que almacenas el ID del usuario en la sesión
    if user_id:
        data = request.json
        nombres = data.get('nombres')
        apellidos = data.get('apellidos')
        n_documento = data.get('n_documento')
        correo = data.get('correo')
        telefono = data.get('telefono')
        resultado = controlador_usuario.actualizar_datos_usuario(user_id, nombres, apellidos, n_documento, correo, telefono)
        return jsonify(resultado)
    else:
        return jsonify({"error": "No autenticado"}), 401
    

####### CAMBIAR FOTO ###########
@app.route('/actualizar_foto', methods=['POST'])
def upload_foto():
    if 'foto' not in request.files:
        return jsonify({"error": "No se encontró el archivo"}), 400

    file = request.files['foto']
    if file.filename == '':
        return jsonify({"error": "No se seleccionó ningún archivo"}), 400

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Aquí debes actualizar la ruta de la imagen en la base de datos
        user_id = session.get('user_id')
        if user_id:
            conexion = obtener_conexion()
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("UPDATE persona SET foto = %s WHERE idpersona = (SELECT idpersona FROM usuario WHERE idusuario = %s)",
                                   (filename, user_id))
                    conexion.commit()
                    return jsonify({"mensaje": "Foto actualizada correctamente", "foto": filename})
            except Exception as e:
                return jsonify({"error": str(e)}), 500
            finally:
                conexion.close()
        else:
            return jsonify({"error": "No autenticado"}), 401
    else:
        return jsonify({"error": "Error al subir el archivo"}), 500

## RUTAS 
@app.route("/obtener_cursos_ambientes", methods=["GET"])
def get_curso_ambientes():
    curso_ambientes = controlador_curso_ambiente.datos_cursos_ambientes()
    return jsonify(curso_ambientes)


@app.route("/obtener_cursos_presenciales", methods=["GET"])
def curso_prensenciales():
    curso_prensenciales = controlador_curso_ambiente.obtener_cursos_presenciales()
    return jsonify(curso_prensenciales)


@app.route("/obtener_ambientes_activos", methods=["GET"])
def obtener_ambientes():
    ambientes_activos = controlador_curso_ambiente.obtener_ambientes()
    return jsonify(ambientes_activos)

@app.route("/guardar_ambientes_curso", methods=["POST"])
def api_guardar_ambientes_curso():
    data = request.get_json()
    curso_id = data.get('curso')
    ambientes = data.get('ambientes')

    if not curso_id or not ambientes:
        return jsonify({'status': 'error', 'message': 'Curso y ambientes son requeridos'}), 400

    result = controlador_curso_ambiente.guardar_ambientes_curso(curso_id, ambientes)
    if result['status'] == 'success':
        return jsonify(result), 200
    else:
        return jsonify(result), 500
    
@app.route("/eliminar_cursoAmbiente", methods=["POST"])
def eliminar_cursoAmbiente():
    try:
        data = request.json
        idcurso = data.get('idcurso')
        idambiente = data.get('idambiente')
        resultado = controlador_curso_ambiente.eliminar_cursoxambiente(idcurso,idambiente)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/get_grupos", methods=["GET"])
def get_grupos():
    grupos = controlador_grupo.obtener_grupos()
    return jsonify(grupos)



#AGREGAR GRUPO
@app.route("/agregar_grupo", methods=["POST"])
def agregar_grupo():
    try:
        nombre = request.json.get('nombre')
        vacantes = request.json.get('vacantes')
        curso = request.json.get('idcurso')
        idsemestre = request.json.get('idsemestre')


        # Llama al controlador para agregar el grupo
        resultado = controlador_grupo.agregar_grupo(nombre, vacantes,curso, idsemestre)

        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/eliminar_grupo", methods=["POST"])
def eliminar_grupo():
    try:
        data = request.json
        idgrupo = data.get('id_grupo')  # Correctly receive id_grupo
        resultado = controlador_grupo.eliminar_grupo(idgrupo)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
    
#DAR DE BAJA GRUPO 

@app.route("/dar_baja_grupo", methods=["POST"])
def dar_baja_grupo():
    try:
        data = request.json
        idgrupo = data.get('id_grupo')
        resultado = controlador_grupo.dar_baja_grupo(idgrupo)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
    
#MODIFICAR GRUPO 

@app.route("/modificar_grupo", methods=["POST"])
def modificar_grupo():
    try:
        data = request.json
        id_grupo = data.get('id_grupo')
        nombre = data.get('nombre')
        vacantes = data.get('vacantes')
        idcurso = data.get('idcurso')
        idsemestre = data.get('idsemestre')
        resultado = controlador_grupo.modificar_grupo(id_grupo, nombre, vacantes, idcurso, idsemestre)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})

    
       ###################################
@app.route("/obtener_docentes_activos", methods=["GET"])
def obtener_docentes():
    docentes_activos = controlador_curso_docente.obtener_docentes()
    return jsonify(docentes_activos)

@app.route("/obtener_cursos_docentes", methods=["GET"])
def get_curso_docente():
    curso_docentes = controlador_curso_docente.datos_cursos_docentes()
    return jsonify(curso_docentes)


@app.route("/obtener_cursos_presenciales", methods=["GET"])
def curso_prensencial():
    curso_prensencial = controlador_curso_docente.obtener_cursos_presenciales()
    return jsonify(curso_prensencial)


## ACTUALIZAR DOCENTE CURSO
@app.route("/actualizar_docentes_curso", methods=["POST"])
def api_actualizar_docentes_curso():
    data = request.get_json()
    curso_id = data.get('curso')
    iddocente = data.get('docentes')

    if not curso_id or not iddocente:
        return jsonify({'status': 'error', 'message': 'Curso y docentes son requeridos'}), 400

    result = controlador_curso_docente.actualizar_docentes_curso(curso_id, iddocente)
    if result['status'] == 'success':
        return jsonify(result), 200
    else:
        return jsonify(result), 500
    
@app.route("/eliminar_cursoDocente", methods=["POST"])
def eliminar_cursoDocente():
    try:
        data = request.json
        idcurso = data.get('idcurso')
        idpersona = data.get('idpersona')
        resultado = controlador_curso_docente.eliminar_cursoxambiente(idcurso,idpersona)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})


""" @app.route("/guardar_ambientes_curso", methods=["POST"])
def api_guardar_ambientes_curso():
    data = request.get_json()
    curso_id = data.get('curso')
    ambientes = data.get('ambientes')

    if not curso_id or not ambientes:
        return jsonify({'status': 'error', 'message': 'Curso y ambientes son requeridos'}), 400

    result = controlador_curso_ambiente.guardar_ambientes_curso(curso_id, ambientes)
    if result['status'] == 'success':
        return jsonify(result), 200
    else:
        return jsonify(result), 500
    
@app.route("/eliminar_cursoAmbiente", methods=["POST"])
def eliminar_cursoAmbiente():
    try:
        data = request.json
        idcurso = data.get('idcurso')
        idambiente = data.get('idambiente')
        resultado = controlador_curso_ambiente.eliminar_cursoxambiente(idcurso,idambiente)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}) """



# #ALGORITHM
# @app.route('/generarHorario', methods=['GET'])
# def obtener_horarios():
#     try:
#         horario = algoritmo.algoritmo_genetico()
#         return jsonify(horario)
#     except Exception as e:
#         return jsonify({"error": str(e)})
    
# # PRUEBA ALGORITMO - JENKZ
# @app.route('/generarHorario_Jenkz', methods=['GET'])
# def obtener_horariosJenkz():
#     try:
#         horario = algoritmoJenkz.algoritmo_genetico()
#         return jsonify(horario)
#     except Exception as e:
#         return jsonify({"error": str(e)})
    


###HORARIO POR AMBIENTE

@app.route("/horarios_por_ambiente")
def horarios_por_ambiente():
    semestres = controlador_semestre.obtener_semestres()
    edificios = controlador_edificio.obtener_edificios()  
    return render_template("horarios/horarios_por_ambiente.html", semestres=semestres, edificios=edificios)



@app.route("/ambientes_por_edificio/<idedificio>", methods=["GET"])
def ambientes_por_edificio(idedificio):
    ambientes = controlador_ambientes.ambientes_por_edificio(idedificio)
    return jsonify(ambientes)

###HORARIOS POR AMBIENTE 
@app.route("/obtener_horarios_por_ambiente", methods=["POST"])
def obtener_horarios_por_ambiente():
    idambiente = request.json.get('idambiente')
    semestre = request.json.get('semestre')
    horarios = controlador_horario.obtener_horarios_por_ambiente(idambiente,semestre)
    return jsonify(horarios) 


###HORARIOS POR CICLO 
@app.route("/obtener_horarios_semestre_ciclo", methods=["POST"])
def obtener_horarios_semestre_ciclo():
    ciclo = request.json.get('ciclo')
    semestre = request.json.get('semestre')
    horarios = controlador_horario.obtener_horarios_por_ciclo(ciclo,semestre)
    return jsonify(horarios) 

@app.route("/horarios_por_ciclo")
def horarios_por_ciclo():
    semestres = controlador_semestre.obtener_semestres()
    ciclos = controlador_cursos.obtener_ciclos()
    return render_template("horarios/horarios_por_ciclo.html",semestres=semestres,ciclos=ciclos)

#DISPONIBILIDAD
# Ruta para obtener todas las disponibilidades
@app.route('/get_disponibilidad', methods=['GET'])
def get_disponibilidad():
    disponibilidades = controlador_disponibilidad.get_disponibilidad()
    return jsonify(disponibilidades)

@app.route('/get_docente_sin_disponibilidad', methods=['GET'])
def get_docente_sin_disponibilidad():
    get_docente_sin_disponibilidad = controlador_disponibilidad.get_docente_sin_disponibilidad()
    return jsonify(get_docente_sin_disponibilidad)

@app.route('/get_docentes_no_asignados', methods=['GET'])
def get_docentes_no_asignados():
    get_docentes_no_asignados = controlador_disponibilidad.get_docentes_no_asignados()
    return jsonify(get_docentes_no_asignados)

# Ruta para agregar una nueva disponibilidad
@app.route('/add_disponibilidad', methods=['POST'])
def agregar_disponibilidad():
    datos = request.json
    idpersona = datos.get('idpersona')
    dia = datos.get('dia')
    hora_inicio = datos.get('hora_inicio')
    hora_fin = datos.get('hora_fin')
    
    resultado = controlador_disponibilidad.agregar_disponibilidad(idpersona, dia, hora_inicio, hora_fin)
    return jsonify(resultado)

# Ruta para modificar una disponibilidad existente
@app.route('/update_disponibilidad', methods=['PUT'])
def modificar_disponibilidad():
    datos = request.json
    idpersona = datos.get('idpersona')
    dia = datos.get('dia')
    hora_inicio = datos.get('hora_inicio')
    hora_fin = datos.get('hora_fin')
    nuevo_dia = datos.get('nuevo_dia')
    nueva_hora_inicio = datos.get('nueva_hora_inicio')
    nueva_hora_fin = datos.get('nueva_hora_fin')
    
    resultado = controlador_disponibilidad.modificar_disponibilidad(idpersona, dia, hora_inicio, hora_fin, nuevo_dia, nueva_hora_inicio, nueva_hora_fin)
    return jsonify(resultado)


# Ruta para eliminar una disponibilidad
@app.route('/eliminar_disponibilidad/<int:idpersona>', methods=['DELETE'])
def eliminar_disponibilidad_por_idpersona(idpersona):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM docente_disponibilidad WHERE idpersona = %s", (idpersona,))
            conexion.commit()
            return {"mensaje": "Disponibilidad eliminada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()


# Ruta para obtener una disponibilidad por detalles específicos (idpersona, dia, hora_inicio, hora_fin)
@app.route('/get_disponibilidad_by_id/<int:id_disponibilidad_docente>', methods=['GET'])
def get_disponibilidad_by_id(id_disponibilidad_docente):
    resultado = controlador_disponibilidad.obtener_disponibilidad_por_id(id_disponibilidad_docente)
    return jsonify(resultado)

@app.route('/update_disponibilidad', methods=['PUT'])
def actualizar_disponibilidad():
    datos = request.json
    id_disponibilidad_docente = datos.get('id_disponibilidad_docente')
    nuevo_dia = datos.get('nuevo_dia')
    nueva_hora_inicio = datos.get('nueva_hora_inicio')
    nueva_hora_fin = datos.get('nueva_hora_fin')
    
    resultado = controlador_disponibilidad.modificar_disponibilidad(id_disponibilidad_docente, nuevo_dia, nueva_hora_inicio, nueva_hora_fin)
    return jsonify(resultado)


@app.route('/docentes_disponibilidad', methods=['GET'])
def obtener_disponibilidad():
    try:
        personas = controlador_disponibilidad.obtener_disponibilidad()
        return jsonify(personas)
    except Exception as e:
        return jsonify({'error': str(e)}), 500



###CURSO X DOCENTE

@app.route("/docentesxcursos")
def docentesxcursos():
    semestres = controlador_cursos.obtener_semestres()
    escuelas = controlador_cursos.obtener_escuelas()
    return render_template("dashboard/docentexcurso.html", semestres=semestres , escuelas=escuelas)

##  GRUPOS DOCENTES
@app.route("/grupo_docentes")
def grupo_docentes():
    semestres = controlador_cursos.obtener_semestres()
    escuelas = controlador_cursos.obtener_escuelas()
    return render_template("dashboard/docentes/grupo_docentes.html", semestres=semestres , escuelas=escuelas)


@app.route("/tabla_curso_docente/<string:escuela>/<string:semestre>")
def tabla_curso_docente(escuela,semestre):
    id_semestre = controlador_grupo.obtener_idsemestre(semestre)
    id_escuela = controlador_curso_docente.obtener_idescuela(escuela)
    datos = controlador_grupo_docente.datosCursoxDocente(id_escuela,id_semestre)
    return jsonify(datos)

@app.route('/asignar_docentes', methods=['POST'])
def asignar_docentes():
    data = request.json
    grupoId = data['grupoId']
    docentes = data['docentes']
    eliminados = data['eliminados']
    
    success, error = controlador_grupo_docente.asignar_docentes_a_grupo(grupoId, docentes, eliminados)
    
    if success:
        return jsonify({'success': True})
    else:
        return jsonify({'error': error}), 500

@app.route('/obtenerDocentesGrupo/<int:id_grupo>', methods=['GET'])
def obtenerDocentesGrupo(id_grupo):
    datos = controlador_grupo_docente.obtenerDocentesporGrupo(id_grupo)    
    return jsonify(datos)

@app.route('/eliminar_asignaciones_docentes/<int:idgrupo>', methods=['DELETE'])
def eliminar_asignaciones_docentes(idgrupo):
    resultado = controlador_grupo_docente.eliminar_asignaciones_docentes(idgrupo)
    if 'success' in resultado:
        return jsonify({'message': 'Asignaciones de docentes eliminadas exitosamente'}), 200
    else:
        return jsonify({'error': resultado['error']}), 500

## CURSO AMBIENTE

@app.route("/ambientesxCursos")
def ambientesxCursos():
    semestres = controlador_cursos.obtener_semestres()
    escuelas = controlador_cursos.obtener_escuelas()
    return render_template("dashboard/ambientesxcurso.html",semestres=semestres,escuelas=escuelas)

@app.route("/obtener_ambientes_activos", methods=["GET"])
def obtener_ambientes_activos():
    ambiente = controlador_curso_ambiente.obtener_ambientes()
    return jsonify(ambiente)

@app.route('/obtener_cursos', methods=['GET'])
def obtener_cursos():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute('SELECT idcurso, nombre, ciclo FROM curso')
            cursos = cursor.fetchall()
        return jsonify(cursos)
    except Exception as e:
        print(f"Error al obtener cursos: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        conexion.close()

@app.route('/asignar_ambientes', methods=['POST'])
def asignar_ambientes():
    data = request.json
    idcurso = data['idcurso']
    idambientes = data['idambientes']

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute('DELETE FROM curso_ambiente WHERE idcurso = %s', (idcurso,))
            for idambiente in idambientes:
                cursor.execute('INSERT INTO curso_ambiente (idcurso, idambiente) VALUES (%s, %s)', (idcurso, idambiente))

        conexion.commit()
    except Exception as e:
        conexion.rollback()
        print(f"Error al asignar ambientes: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        conexion.close()
    
    return jsonify({'success': True})

@app.route('/tabla_curso_ambiente/<string:escuela>/<string:semestre>', methods=['GET'])
def tabla_curso_ambiente(escuela, semestre):
    id_semestre = controlador_grupo.obtener_idsemestre(semestre)
    id_escuela = controlador_curso_docente.obtener_idescuela(escuela)
    datos = controlador_curso_ambiente.obtener_cursos_con_ambientes(id_escuela, id_semestre)
    return jsonify(datos)
   
@app.route('/obtenerAmbientesCurso/<int:idcurso>', methods=['GET'])
def obtener_ambientes_curso_endpoint(idcurso):
    ambientes = controlador_curso_ambiente.obtener_ambientes_curso(idcurso)
    if "error" in ambientes:
        return jsonify(ambientes), 500
    return jsonify(ambientes)

@app.route('/eliminar_ambientes_curso/<int:idcurso>', methods=['DELETE'])
def eliminar_ambientes_curso_route(idcurso):
    resultado = controlador_curso_ambiente.eliminar_ambientes_curso(idcurso)
    if 'error' in resultado:
        return jsonify(resultado), 500
    return jsonify(resultado)


@app.route('/asignar_disponibilidad_excel', methods=['POST'])
def asignar_disponibilidad_excel():
    data = request.get_json()
    conexion = obtener_conexion()
    resultados = []

    try:
        for item in data:
            idpersona = controlador_disponibilidad.obtener_id_persona(item['docente'])
            if not idpersona:
                resultados.append({"error": f"No se encontró el docente: {item['docente']}"})
                continue
            
            try:
                with conexion.cursor() as cursor:
                    cursor.callproc('sp_disponibilidad_Gestion', [1, item['dia'], item['hora_inicio'], item['hora_fin'], idpersona])
                    conexion.commit()
                    resultados.append({"mensaje": f"Disponibilidad agregada correctamente para {item['docente']}"})
            except Exception as e:
                resultados.append({"error": str(e)})
    finally:
        conexion.close()

    return jsonify(resultados)
