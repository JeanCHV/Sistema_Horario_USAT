from flask import (
    Flask,
    render_template,
    request,
    redirect,
    jsonify,
    make_response,
    session,
)
import hashlib
import random
from main import app

import controladores.usuario.usuario as controlador_usuarios
import clases.usuario_clase as usuario_clase

import controladores.controlador_usuario as controlador_usuario
import controladores.ambientes.controlador_ambiente as controlador_ambientes
import controladores.cursos.controlador_cursos as controlador_cursos
import controladores.controlador_persona as controlador_persona
import controladores.controlador_semestre as controlador_semestre
import controladores.controlador_horario as controlador_horario
import controladores.controlador_docente as controlador_docente
import clases.usuario as clase_usuario
import clases.persona as clase_persona


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login/login.html")

"""MÉTODO A MODIFICAR A FUTURO PARA VALIDAR TIPO DE USUARIO Y PERMISOS"""
""" @app.route("/validar_login", methods=["POST"])
def validar_login():
    try:
        username = request.json.get('username')
        token = request.json.get('token')

        usuario = controlador_usuario.obtener_usuario_por_username(username)

        if usuario == None or username != usuario[1] or token != usuario[5] or not usuario[3]:
            return jsonify({'logeo':False})
        else:
            return jsonify({'logeo': True}) 
    except:
        return jsonify({'logeo':False}) """


@app.route("/logout")
def logout():
    resp = make_response(redirect("/login"))
    session.clear()
    return resp

@app.route("/procesar_login", methods=["POST"])
def procesar_login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        usuario = controlador_usuario.obtener_usuario_con_tipopersona_por_username(username)

        if usuario == None:
            return jsonify({'mensaje':'El usuario no existe', 'logeo':False})
        
        elif username != usuario[1]:
            return jsonify({'mensaje':'El username es incorrecto', 'logeo':False})
        
        elif not usuario[3]:
            return jsonify({'mensaje':'El usuario está inactivo', 'logeo':False})
        
        else:
            # Encriptar password ingresado por usuario
            h = hashlib.new("sha256")
            h.update(bytes(password, encoding="utf-8"))
            encpassword = h.hexdigest()
            if encpassword == usuario[2]:
                # Obteniendo token
                t = hashlib.new("sha256")
                entale = random.randint(1, 1024)
                strEntale = str(entale)
                t.update(bytes(strEntale, encoding="utf-8"))
                token = t.hexdigest()
                controlador_usuario.actualizar_token(username, token)
                persona = controlador_persona.obtener_persona_por_id(usuario[4])
                foto = persona[9]
                nombre = persona[1].split()[0]
                return jsonify({'logeo': True, 'token': token, 'foto':foto, 'nombre':nombre})

            return jsonify({'mensaje':'La contraseña es incorrecta', 'logeo':False})
    except NameError:
        return jsonify({'mensaje':'Error al procesar el login'+NameError, 'logeo':False})
    

@app.route("/get_ambientes", methods=["GET"])
def get_ambientes():
    ambientes = controlador_ambientes.obtener_ambientes()
    return jsonify(ambientes)
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
        data = request.json
        idambiente = data.get('id')
        resultado = controlador_ambientes.eliminar_ambiente(idambiente)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
#DAR DE BAJA AMBIENTE 

@app.route("/dar_baja_ambiente", methods=["POST"])
def dar_baja_ambiente_route():
    try:
        data = request.json
        idambiente = data.get('id')
        resultado = controlador_ambientes.dar_baja_ambiente(idambiente)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
#MODIFICAR AMBIENTE 

@app.route("/modificar_ambiente", methods=["POST"])
def modificar_ambiente_route():
    try:
        data = request.json
        idambiente = data.get('id')
        nombre = data.get('nombre')
        aforo = data.get('aforo')
        estado = data.get('estado')
        idedificio = data.get('idedificio')
        idambientetipo = data.get('idambientetipo')
        resultado = controlador_ambientes.modificar_ambiente(idambiente, nombre, aforo, estado, idedificio, idambientetipo)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
   
@app.route("/get_cursos", methods=["GET"])
def get_cursos():
    cursos = controlador_cursos.obtener_cursos()
    return jsonify(cursos)

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


@app.route("/rellenar_tabla,<string>escuela")
def rellenar_tabla(escuela):
    cursos = controlador_cursos.obtener_curso(escuela)
    return cursos

@app.route("/cursos")
def cursos():
    semestres = controlador_cursos.obtener_semestres()
    escuelas = controlador_cursos.obtener_escuelas()
    return render_template("dashboard/cursos.html", semestres=semestres, escuelas=escuelas)


@app.route('/docentes')
def mostrar_docentes():
    persona = controlador_docente.mostrar_docentes()
    return render_template('dashboard/docentes.html', docentes=persona)

@app.route("/horarios")
def horarios():
    return render_template("dashboard/horarios.html")

@app.route("/usuario")
def usuario():
    return render_template("dashboard/usuario.html")

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

@app.route("/get_horarios_docentesNombres_semestre", methods=["POST"])
def get_horarios_docentesNombres_semestre():
    nombre_docente = request.json.get('nombre_docente')
    semestre = request.json.get('semestre')
    horarios = controlador_horario.obtener_horarios_por_docenteNombre_semestre(nombre_docente,semestre)
    return jsonify(horarios)  
    
@app.route("/perfil")
def perfil():
    return render_template("dashboard/perfil.html")