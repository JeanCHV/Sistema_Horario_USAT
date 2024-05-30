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

import controladores.controlador_usuario as controlador_usuario
import controladores.ambientes.controlador_ambiente as controlador_ambientes
import controladores.cursos.controlador_cursos as controlador_cursos
import controladores.controlador_persona as controlador_persona
import controladores.controlador_semestre as controlador_semestre
import controladores.controlador_horario as controlador_horario
import controladores.docente.controlador_docente as controlador_docente
import controladores.grupo.controlador_grupo as controlador_grupo
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


##GESTIONAR CURSOS
@app.route("/get_cursos", methods=["GET"])
def get_cursos():
    cursos = controlador_cursos.obtener_cursos()
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

##ELIMINAR CURSO
@app.route("/eliminar_curso", methods=["POST"])
def eliminar_curso():
    try:
        data = request.get_json()  # Captura correctamente el JSON
        idcurso = data.get('idcurso')  # Asegúrate de capturar 'idcurso'
        print(f"ID del curso a eliminar recibido: {idcurso}")  # Imprime el idcurso en el servidor
        resultado = controlador_cursos.eliminar_curso(idcurso)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})


##MODIFICAR CURSO
@app.route("/modificar_curso", methods=["POST"])
def modificar_curso_endpoint():
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

@app.route('/get_curso/<int:idcurso>', methods=['GET'])
def get_curso(idcurso):
    resultado = controlador_cursos.obtener_curso_por_id(idcurso)
    return jsonify(resultado)

    
#GESTIONAR DOCENTE
    

@app.route("/get_docentes", methods=["GET"])
def get_docentes():
    try:
        docentes = controlador_docente.obtener_docentes()
        return jsonify(docentes)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/agregar_docente", methods=["POST"])
def agregar_docente():
    try:
        nombres = request.json.get('nombres')
        correo = request.json.get('correo')

        # Llama al controlador para agregar el docente
        resultado = controlador_docente.agregar_docente(nombres, correo)

        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/eliminar_docente", methods=["POST"])
def eliminar_docente_route():
    try:
        data = request.json
        idpersona = data.get('idpersona')
        resultado = controlador_docente.eliminar_docente(idpersona)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/modificar_docente", methods=["POST"])
def modificar_docente_route():
    try:
        data = request.json
        idpersona = data.get('idpersona')
        nombres = data.get('nombres')
        correo = data.get('correo')
        resultado = controlador_docente.modificar_docente(idpersona, nombres, correo)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})


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


@app.route("/rellenar_tabla/<string:escuela>")
def rellenar_tabla(escuela):
    cursos = controlador_grupo.obtener_cursoxescuela(escuela)
    return jsonify(cursos)

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
    return render_template("dashboard/horarios.html")

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
