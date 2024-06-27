import random
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import controladores.docente.controlador_docente as controlador_docente
import controladores.ambientes.controlador_ambiente as controlador_ambiente
import controladores.cursos.controlador_cursos as controlador_cursos
import controladores.grupo.controlador_grupo as controlador_grupo
import controladores.docente_disponibilidad.controlador_docente_disponibilidad as controlador_docente_disponibilidad
import controladores.curso_ambiente.controlador_curso_ambiente as controlador_curso_ambiente
import controladores.grupo_docente.controlador_grupo_docente as controlador_grupo_docente

docentes1 = controlador_docente.get_docentes()  # SELECT persona.idpersona,persona.nombres,persona.apellidos,persona.cantHoras,persona.tiempo_ref FROM persona WHERE persona.tipopersona='D' AND persona.estado=1
ambientes1 = controlador_ambiente.get_ambientes()  # SELECT ambiente.idambiente,ambiente.nombre,ambiente.aforo FROM ambiente WHERE ambiente.estado='A'
cursos1 = controlador_cursos.get_cursos()  # SELECT curso.idcurso,curso.nombre,curso.horas_teoria,curso.horas_practica,curso.tipo_curso,curso.ciclo FROM curso WHERE curso.estado='A'
grupo = controlador_grupo.get_grupo()  # SELECT id_grupo, nombre, vacantes, idcurso, idsemestre FROM grupo where idsemestre=1
disponibilidad = controlador_docente_disponibilidad.get_disponibilidad()  # SELECT dia,TIME_FORMAT(hora_inicio,'%H:%i') AS hora_inicio,TIME_FORMAT(hora_fin,'%H:%i') AS hora_fin,idpersona FROM docente_disponibilidad;
curso_ambiente = controlador_curso_ambiente.get_curso_ambiente()  # SELECT idcurso,idambiente FROM curso_ambiente
grupo_docente = controlador_grupo_docente.get_grupo_docente()  # SELECT idgrupo,idpersona from grupo_docente

DOCENTES = {docente['idpersona']: docente for docente in docentes1}
AMBIENTES = {ambiente['idambiente']: ambiente for ambiente in ambientes1}
CURSOS = {curso['idcurso']: curso for curso in cursos1}
GRUPOS_HORARIO = grupo
DISPONIBILIDAD_DOCENTES = disponibilidad
CURSO_AMBIENTE = curso_ambiente
GRUPO_DOCENTE = grupo_docente

NUM_PROFESORES = len(docentes1)
NUM_CURSOS = len(cursos1)
NUM_AULAS = len(ambientes1)
HORAS = [f"{h}:00" for h in range(7, 22)]
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

# Definir duraciones posibles para las clases (en horas)
DURACIONES_CLASES = [2, 3]

# Horas divididas por mañana y tarde
horas_inicio_manana = [f"{h}:00" for h in range(7, 12)]
horas_inicio_tarde = [f"{h}:00" for h in range(13, 22)]

def generar_poblacion(tamano):
    try:
        poblacion = []
        for _ in range(tamano):
            horario = []
            for idcurso, curso in CURSOS.items():
                grupo_cursos = [g for g in GRUPOS_HORARIO if g['idcurso'] == idcurso]
                
                for grupo_curso in grupo_cursos:
                    docentes_del_grupo = [gd['idpersona'] for gd in GRUPO_DOCENTE if gd['idgrupo'] == grupo_curso['id_grupo']]
                    if len(docentes_del_grupo) > 1:
                        for profesor in docentes_del_grupo:
                            horas_totales = curso['horas_teoria'] + curso['horas_practica']
                            while horas_totales > 0:
                                dia = random.choice(DIAS)
                                if horas_totales == 3:
                                    duracion = 3
                                else:
                                    duracion = min(horas_totales, random.choice(DURACIONES_CLASES))
                                
                                hora_inicio = random.choice(HORAS)
                                hora_fin = f"{int(hora_inicio.split(':')[0]) + duracion}:00"
                                # Ajustar hora_fin si excede el límite de 22:00
                                if int(hora_fin.split(':')[0]) > 22:
                                    continue

                                # Ambiente "No definido" si no hay asignación
                                ambiente = next((ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == idcurso), "No definido")
                                horario.append((profesor, idcurso, grupo_curso['id_grupo'], ambiente, dia, hora_inicio, hora_fin))
                                horas_totales -= duracion
                    else:
                        if docentes_del_grupo:
                            profesor = docentes_del_grupo[0]
                        else:
                            profesor = "No definido"
                        
                        horas_totales = curso['horas_teoria'] + curso['horas_practica']
                        while horas_totales > 0:
                            dia = random.choice(DIAS)
                            if horas_totales == 3:
                                duracion = 3
                            else:
                                duracion = min(horas_totales, random.choice(DURACIONES_CLASES))
                            
                            hora_inicio = random.choice(HORAS)
                            hora_fin = f"{int(hora_inicio.split(':')[0]) + duracion}:00"
                            # Ajustar hora_fin si excede el límite de 22:00
                            if int(hora_fin.split(':')[0]) > 22:
                                continue

                            # Ambiente "No definido" si no hay asignación
                            ambiente = next((ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == idcurso), "No definido")
                            horario.append((profesor, idcurso, grupo_curso['id_grupo'], ambiente, dia, hora_inicio, hora_fin))
                            horas_totales -= duracion

            poblacion.append(horario)
        return poblacion
    except Exception as e:
        return []

def calcular_fitness(horario):
    try:
        fitness = 0
        
        for dia in DIAS:
            horas_ocupadas = {profesor: [] for profesor in DOCENTES}
            aulas_ocupadas = {aula: [] for aula in AMBIENTES}
            grupos_docentes = {}
            for entry in horario:
                try:
                    profesor, idcurso, idgrupo, aula, d, hora_inicio, hora_fin = entry
                except ValueError as e:
                    continue
                
                if d == dia and profesor != "No definido" and aula != "No definido":
                    if not todas_horas_disponibles(profesor, d, hora_inicio, hora_fin):
                        fitness -= 1
                    
                    # Verificar si el docente tiene superposición de horas
                    horas_profesor = horas_ocupadas[profesor]
                    if any(hora in horas_profesor for hora in rango_horas(hora_inicio, hora_fin)):
                        fitness -= 1
                    else:
                        horas_ocupadas[profesor].extend(rango_horas(hora_inicio, hora_fin))
                    
                    # Verificar si el aula tiene superposición de horas
                    horas_aula = aulas_ocupadas[aula]
                    if any(hora in horas_aula for hora in rango_horas(hora_inicio, hora_fin)):
                        fitness -= 1
                    else:
                        aulas_ocupadas[aula].extend(rango_horas(hora_inicio, hora_fin))
                    
                    # Verificar si se respeta el ambiente preferido
                    if any(ca['idcurso'] == idcurso for ca in CURSO_AMBIENTE):
                        ambiente_especifico = next(ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == idcurso)
                        if aula != ambiente_especifico:
                            fitness -= 1
                    
                    # Verificar el total de horas asignadas
                    horas_curso = CURSOS[idcurso]['horas_teoria'] + CURSOS[idcurso]['horas_practica']
                    if horas_curso != 0 and len(horas_ocupadas[profesor]) != horas_curso:
                        fitness -= 1

                    # Verificar que no haya más de 3 horas de clase seguidas
                    if len(rango_horas(hora_inicio, hora_fin)) > 3:
                        fitness -= 1

                    # Verificar que no se asignen horas durante el almuerzo
                    if any(hora in ['12:00', '13:00'] for hora in rango_horas(hora_inicio, hora_fin)):
                        fitness -= 1

                    # Verificar si las horas se asignan en el ciclo correcto (mañana/tarde)
                    ciclo = CURSOS[idcurso]['ciclo']
                    if ciclo % 2 == 1:  # ciclo impar: tarde
                        if any(hora in horas_inicio_manana for hora in rango_horas(hora_inicio, hora_fin)):
                            fitness -= 1
                    else:  # ciclo par: mañana
                        if any(hora in horas_inicio_tarde for hora in rango_horas(hora_inicio, hora_fin)):
                            fitness -= 1

                    # Verificar que cada grupo tenga solo un docente
                    if idgrupo not in grupos_docentes:
                        grupos_docentes[idgrupo] = profesor
                    else:
                        if grupos_docentes[idgrupo] != profesor:
                            fitness -= 1

                    # Nueva restricción: Verificar que los cursos de primer ciclo se dicten en la mañana
                    if ciclo == 1 and any(hora in horas_inicio_tarde for hora in rango_horas(hora_inicio, hora_fin)):
                        fitness -= 1

        return fitness
    except Exception as e:
        return -1

def obtener_horas_disponibles(profesor, dia):
    try:
        horas_disponibles = []
        for disponibilidad in DISPONIBILIDAD_DOCENTES:
            if disponibilidad["idpersona"] == profesor and disponibilidad["dia"] == dia:
                hora_inicio = int(disponibilidad["hora_inicio"].split(':')[0])
                hora_fin = int(disponibilidad["hora_fin"].split(':')[0])
                horas_disponibles.extend([f"{h}:00" for h in range(hora_inicio, hora_fin)])
        return horas_disponibles
    except Exception as e:
        return []

def todas_horas_disponibles(profesor, dia, hora_inicio, hora_fin):
    try:
        horas_disponibles = obtener_horas_disponibles(profesor, dia)
        for hora in rango_horas(hora_inicio, hora_fin):
            if hora not in horas_disponibles:
                return False
        return True
    except Exception as e:
        return False

def rango_horas(hora_inicio, hora_fin):
    try:
        inicio = int(hora_inicio.split(':')[0])
        fin = int(hora_fin.split(':')[0])
        return [f"{h}:00" for h in range(inicio, fin)]
    except Exception as e:
        return []

def seleccion(poblacion):
    try:
        poblacion = sorted(poblacion, key=lambda x: calcular_fitness(x), reverse=True)
        return poblacion[:2]
    except Exception as e:
        return []

def cruce(padre1, padre2):
    try:
        punto_cruce = random.randint(1, len(padre1) - 1)
        hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
        hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
        return hijo1, hijo2
    except Exception as e:
        return padre1, padre2

def mutacion(individuo):
    try:
        if random.random() < 0.1:
            i = random.randint(0, len(individuo) - 1)
            idcurso = individuo[i][1]
            docentes_del_grupo = [gd['idpersona'] for gd in GRUPO_DOCENTE if gd['idgrupo'] == individuo[i][2]]
            if docentes_del_grupo:
                profesor = random.choice(docentes_del_grupo)
            else:
                profesor = "No definido"
            
            dia = random.choice(DIAS)
            duracion = CURSOS[idcurso]['horas_teoria'] + CURSOS[idcurso]['horas_practica']
            if duracion == 3:
                duracion = 3
            else:
                duracion = random.choice(DURACIONES_CLASES)
            hora_inicio = random.choice(HORAS)
            hora_fin = f"{int(hora_inicio.split(':')[0]) + duracion}:00"
            # Ajustar hora_fin si excede el límite de 22:00
            if int(hora_fin.split(':')[0]) > 22:
                hora_fin = "22:00"
            ambiente = next((ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == idcurso), "No definido")
            individuo[i] = (profesor, idcurso, individuo[i][2], ambiente, dia, hora_inicio, hora_fin)
    except Exception as e:
        pass

def algoritmo_genetico():
    try:
        poblacion = generar_poblacion(200)  # Aumentar a 200 para mayor diversidad
        
        for generacion in range(200):  # Aumentar a 200 para más iteraciones
            nueva_poblacion = []
            
            padres = seleccion(poblacion)
            
            while len(nueva_poblacion) < 200:
                padre1, padre2 = random.sample(padres, 2)
                hijo1, hijo2 = cruce(padre1, padre2)
                mutacion(hijo1)
                mutacion(hijo2)
                nueva_poblacion.extend([hijo1, hijo2])
            
            poblacion = nueva_poblacion[:200]  # Limitar la población a 200
        
        mejor_individuo = max(poblacion, key=calcular_fitness)
        
        resultado = []
        for (profesor, idcurso, idgrupo, aula, dia, hora_inicio, hora_fin) in mejor_individuo:
            # Verificar si el profesor está dentro del rango válido o es "No definido"
            if profesor == "No definido" or profesor not in DOCENTES:
                continue  # Ignorar esta entrada si el profesor no es válido
            
            # Verificar si el aula está dentro del rango válido o es "No definido"
            if aula == "No definido" or aula not in AMBIENTES:
                continue  # Ignorar esta entrada si el aula no es válida
            
            nombre_curso = CURSOS[idcurso]["nombre"]
            tipo_curso = CURSOS[idcurso]["tipo_curso"]
            nombre_docente = DOCENTES[profesor]["nombres"]
            apellidos_docente = DOCENTES[profesor]["apellidos"]
            nombre_aula = AMBIENTES[aula]["nombre"]
            
            grupo = next((g for g in GRUPOS_HORARIO if g["id_grupo"] == idgrupo), None)
            
            if grupo:
                grupo_nombre = grupo["nombre"]
                tipo_curso_str = "Presencial" if tipo_curso == 0 else "Virtual"
                resultado.append({
                    "curso": nombre_curso,
                    "grupo": grupo_nombre,
                    "docente": f"{nombre_docente} {apellidos_docente}",
                    "aula": nombre_aula,
                    "dia": dia,
                    "hora_inicio": hora_inicio,
                    "hora_fin": hora_fin,
                    "tipo_curso": tipo_curso_str
                })
        
        return resultado
        
    except Exception as e:
        return []

# Ejecución del algoritmo genético mejorado
resultado = algoritmo_genetico()
