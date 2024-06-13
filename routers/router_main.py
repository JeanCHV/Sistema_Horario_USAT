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
import os
from werkzeug.utils import secure_filename
from bd import obtener_conexion

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

import clases.usuario as clase_usuario
import clases.persona as clase_persona

#Algorithm 
import algorithm.algorithm as algoritmo
import algorithm.algorithm_pruebaJenkz as algoritmoJenkz


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
                # Almacenar el ID del usuario en la sesión
                session['user_id'] = usuario[0]
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


##DATOS CURSOS
@app.route("/datos_cursos", methods=["GET"])
def datos_cursos():
    cursos = controlador_cursos.obtener_datos_cursos()
    return jsonify(cursos)

##VER DETALLES CURSOS

@app.route("/ver_cursos/<int:idcurso>", methods=["GET"])
def ver_detalles_cursos(idcurso):
    cursos = controlador_cursos.ver_detalle_cursos(idcurso)
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
        data = request.get_json()  
        idcurso = data.get('idcurso')  
        resultado = controlador_cursos.eliminar_curso(idcurso)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})


##MODIFICAR CURSO
@app.route("/modificar_curso", methods=["POST"])
def modificar_curso():
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

@app.route('/obtener_curso/<int:idcurso>', methods=['GET'])
def obtener_curso_id(idcurso):
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

@app.route("/ambientesxCursos")
def ambientesxCursos():
    return render_template("dashboard/ambientesxcurso.html")

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
    
@app.route("/docentesxcursos")
def docentesxcursos():
    return render_template("dashboard/docentexcurso.html")

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

@app.route("/obtener_cursos", methods=["GET"])
def obtener_curso():
    cursos = controlador_cursos.obtener_cursosFiltro()
    return jsonify(cursos)

@app.route("/obtener_semestres", methods=["GET"])
def obtener_semestres():
    semestres = controlador_semestre.obtener_semestreCombo()
    return jsonify(semestres)

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
        idgrupo = data.get('id')
        nombre = data.get('nombre')
        vacantes = data.get('vacantes')
        idcurso = data.get('idcurso')
        idsemestre = data.get('idsemestre')
        resultado = controlador_grupo.modificar_grupo(idgrupo, nombre, vacantes, idcurso, idsemestre)
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


@app.route("/guardar_docentes_curso", methods=["POST"])
def api_guardar_docentes_curso():
    data = request.get_json()
    curso_id = data.get('curso')
    docentes = data.get('docentes')

    if not curso_id or not docentes:
        return jsonify({'status': 'error', 'message': 'Curso y docentes son requeridos'}), 400

    result = controlador_curso_docente.guardar_docentes_curso(curso_id, docentes)
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
        resultado = controlador_curso_ambiente.eliminar_cursoxambiente(idcurso,idpersona)
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
    


###HORARIO POR AMBIENTE

@app.route("/horarios_por_ambiente")
def horarios_por_ambiente():
    semestres = controlador_semestre.obtener_semestreCombo()
    edificios = controlador_edificio.obtener_edificios()  
    return render_template("horarios/horarios_por_ambiente.html", semestres=semestres, edificios=edificios)



@app.route("/ambientes_por_edificio/<idedificio>", methods=["GET"])
def ambientes_por_edificio(idedificio):
    ambientes = controlador_ambientes.ambientes_por_edificio(idedificio)
    return jsonify(ambientes)

@app.route("/horarios_por_ambiente/<idambiente>/<idsemestre>", methods=["GET"])
def horarios_por_ambiente_route(idambiente, idsemestre):
    try:
        horarios = controlador_horario.obtener_horarios_por_ambiente(idambiente, idsemestre)
        print("Datos enviados:", horarios)  # Depuración
        response = jsonify(horarios)
        response.status_code = 200 if horarios else 204
    except Exception as e:
        print(f"Error al obtener los horarios: {e}")
        response = jsonify({"error": "No se pudieron obtener los horarios"})
        response.status_code = 500
