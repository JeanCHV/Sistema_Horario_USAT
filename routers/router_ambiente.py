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
import controladores.ambientes.controlador_ambiente as controlador_ambientes

@app.route("/datos_ambientes", methods=["GET"])
def datos_ambientes():
    ambientes = controlador_ambientes.obtener_ambientes()
    return jsonify(ambientes)

@app.route("/get_edificios", methods=["GET"])
def get_edificios():
    edificio = controlador_edificio.obtener_edificios()
    return jsonify(edificio)