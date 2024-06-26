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

@app.route("/datos_ambientes", methods=["GET"])
def datos_ambientes():
    ambientes = controlador_ambientes.obtener_ambientes()
    return jsonify(ambientes)

@app.route("/get_edificios", methods=["GET"])
def get_edificios():
    edificio = controlador_edificio.obtener_edificios()
    return jsonify(edificio)