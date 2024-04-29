from flask import Flask, render_template, request, redirect, jsonify, make_response, session
import hashlib
import random
from main import app

import controladores.usuario.usuario as controlador_usuarios
import clases.usuario_clase as usuario_clase

import controladores.controlador_usuario as controlador_usuario
import controladores.controlador_persona as controlador_persona
import clases.usuario as clase_usuario
import clases.persona as clase_persona


@app.route("/")
@app.route("/login",methods=["GET","POST"])
def login():
    try:
        username = session.get('username')
        token = session.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        if username is None:
            return render_template("login/login.html")
        
        if token == usuario[5] and usuario[3]:
            return render_template("dashboard/home.html")
    except:
        return render_template("login/login.html")

@app.route("/logout")
def logout():
    resp = make_response(redirect("/login"))
    """ session.pop('username',None)
    session.pop('token',None) """
    session.clear()
    return resp                          

@app.route("/procesar_login", methods=["POST"])
def procesar_login():
    username = request.form["username"]
    password = request.form["password"]
    rec_chk = request.form.get("recordar_check")
    usuario = controlador_usuario.obtener_usuario_con_tipopersona_por_username(username)

    if usuario == None or not usuario[3]:
        return render_template("login/login.html")
    else:
        # Encriptar password ingresado por usuario
        h = hashlib.new('sha256')
        h.update(bytes(password,encoding='utf-8'))
        encpassword = h.hexdigest()
        if encpassword == usuario[2]:
            # Obteniendo token
            t = hashlib.new('sha256')
            entale = random.randint(1,1024)
            strEntale = str(entale)
            t.update(bytes(strEntale,encoding='utf-8'))
            token = t.hexdigest()
            if rec_chk == 'on':
                session['username'] = username
                session['token'] = token
                session.permanent = True
                controlador_usuario.actualizar_token(username, token)
                return redirect("/index")
            else:
                session['username'] = username
                session['token'] = token
                session.permanent = False
                controlador_usuario.actualizar_token(username, token)
                return redirect("/index")
                     
        return render_template("login/login.html")


@app.route("/index")
def index():
    try:
        username = session.get('username')
        token = session.get('token')
        usuario = controlador_usuario.obtener_usuario_por_username(username)
        persona = controlador_persona.obtener_persona_por_id(usuario[4])
        foto = persona[9]
        primer_nombre = persona[1].split()[0]
        if username is None:
            return render_template("login/login.html")
        
        if token == usuario[5] and usuario[3]:
            return render_template("dashboard/index.html",foto=foto,primer_nombre=primer_nombre,esSesionIniciada=True)
    except:
        return render_template("login/login.html")



@app.route("/ambientes")
def ambientes():
    return render_template("dashboard/ambientes.html")

@app.route("/cursos")
def cursos():
    return render_template("dashboard/cursos.html")


@app.route("/docentes")
def docentes():
    return render_template("dashboard/docentes.html")

@app.route("/horarios")
def horarios():
    return render_template("dashboard/horarios.html")

@app.route("/horarios_por_docente")
def horarios_por_docente():
    return render_template("horarios/horarios_por_docente.html")