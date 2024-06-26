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
from routers.router_curso import *
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

login_attempts = {}


@app.route("/procesar_login", methods=["POST"])
def procesar_login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        usuario = controlador_usuario.obtener_usuario_con_tipopersona_por_username(username)

        if username not in login_attempts:
            login_attempts[username] = {'attempts': 0, 'last_attempt_time': 0}

        if login_attempts[username]['attempts'] >= 3 and (time.time() - login_attempts[username]['last_attempt_time']) < 300:
            return jsonify({'mensaje': 'Cuenta bloqueada. Intente de nuevo más tarde.', 'logeo': False})
        
        if usuario == None:
            return jsonify({'mensaje':'El usuario no existe', 'logeo':False})
        
        elif username != usuario[1]:
            return jsonify({'mensaje':'El username es incorrecto', 'logeo':False})
        
        elif not usuario[3]:
            return jsonify({'mensaje':'El usuario está inactivo', 'logeo':False})
        
        else:
            h = hashlib.new("sha256")
            h.update(bytes(password, encoding="utf-8"))
            encpassword = h.hexdigest()
            if encpassword == usuario[2]:
                t = hashlib.new("sha256")
                entale = random.randint(1, 1024)
                strEntale = str(entale)
                t.update(bytes(strEntale, encoding="utf-8"))
                token = t.hexdigest()
                controlador_usuario.actualizar_token(username, token)
                persona = controlador_persona.obtener_persona_por_id(usuario[4])
                foto = persona[9]
                nombre = persona[1].split()[0]
                session['user_id'] = usuario[0]
                session.permanent = True
                return jsonify({'logeo': True, 'token': token, 'foto':foto, 'nombre':nombre})
            else:
                login_attempts[username]['attempts'] += 1
                login_attempts[username]['last_attempt_time'] = time.time()
                return jsonify({'mensaje': 'La contraseña es incorrecta', 'logeo': False})
    except NameError:
        return jsonify({'mensaje':'Error al procesar el login'+NameError, 'logeo':False})

@app.route("/logout")
def logout():
    session.pop('idusuario', None)
    return redirect(url_for('login'))