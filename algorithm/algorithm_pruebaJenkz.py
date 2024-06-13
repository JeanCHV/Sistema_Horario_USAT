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
import controladores.curso_docente.controlador_curso_docente as controlador_curso_docente

docentes1 = controlador_docente.get_docentes()
ambientes1 = controlador_ambiente.get_ambientes()
cursos1 = controlador_cursos.get_cursos()
grupo = controlador_grupo.get_grupo()
disponibilidad = controlador_docente_disponibilidad.get_disponibilidad()
curso_ambiente = controlador_curso_ambiente.get_curso_ambiente()
curso_docente = controlador_curso_docente.get_curso_docente()

DOCENTES = {docente['idpersona']: docente for docente in docentes1}
AMBIENTES = {ambiente['idambiente']: ambiente for ambiente in ambientes1}
CURSOS = {curso['idcurso']: curso for curso in cursos1}
GRUPOS_HORARIO = grupo
DISPONIBILIDAD_DOCENTES = disponibilidad
CURSO_AMBIENTE = curso_ambiente
CURSO_DOCENTE = curso_docente

NUM_PROFESORES = len(docentes1)
NUM_CURSOS = len(cursos1)
NUM_AULAS = len(ambientes1)
HORAS = [f"{h}:00" for h in range(7, 22)]
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

# Definir duraciones posibles para las clases (en horas)
DURACIONES_CLASES = [2, 3]

def generar_poblacion(tamano):
    poblacion = []
    for _ in range(tamano):
        horario = []
        for idcurso, curso in CURSOS.items():
            docentes_del_curso = [cd['idpersona'] for cd in CURSO_DOCENTE if cd['idcurso'] == idcurso]
            if docentes_del_curso:
                profesor = random.choice(docentes_del_curso)
            else:
                profesor = "No definido"
            
            grupo_cursos = [g for g in GRUPOS_HORARIO if g['idcurso'] == idcurso]
            for grupo_curso in grupo_cursos:
                dia = random.choice(DIAS)
                hora_inicio = random.choice(HORAS)
                duracion = random.choice(DURACIONES_CLASES)
                hora_fin = f"{int(hora_inicio.split(':')[0]) + duracion}:00"
                # Ajustar hora_fin si excede el límite de 23:00
                if int(hora_fin.split(':')[0]) > 23:
                    continue
                
                ambiente = next((ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == idcurso), "No definido")
                
                horario.append((profesor, idcurso, grupo_curso['id_grupo'], ambiente, dia, hora_inicio, hora_fin))
        poblacion.append(horario)
    return poblacion

def calcular_fitness(horario):
    fitness = 0
    
    for dia in DIAS:
        horas_ocupadas = {profesor: [] for profesor in range(NUM_PROFESORES)}
        for (profesor, idcurso, idgrupo, aula, d, hora_inicio, hora_fin) in horario:
            if d == dia and profesor != "No definido" and aula != "No definido":
                if profesor not in horas_ocupadas:
                    continue  # Evitar KeyError si el profesor no está en horas_ocupadas
                horas_profesor = horas_ocupadas[profesor]
                
                if any(hora in horas_profesor for hora in rango_horas(hora_inicio, hora_fin)) or not todas_horas_disponibles(profesor, d, hora_inicio, hora_fin):
                    fitness -= 1
                else:
                    horas_ocupadas[profesor].extend(rango_horas(hora_inicio, hora_fin))
                    
                horas_teoria = CURSOS[idcurso].get("horas_teoria", 0)
                
                if horas_teoria != 0 and len(horas_ocupadas[profesor]) != horas_teoria:
                    fitness -= 1

                if any(ca['idcurso'] == idcurso for ca in CURSO_AMBIENTE):
                    ambiente_especifico = next(ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == idcurso)
                    if aula != ambiente_especifico:
                        fitness -= 1
    
    return fitness

def obtener_horas_disponibles(profesor, dia):
    horas_disponibles = []
    for disponibilidad in DISPONIBILIDAD_DOCENTES:
        if disponibilidad["idpersona"] == profesor and disponibilidad["dia"] == dia:
            hora_inicio = int(disponibilidad["hora_inicio"].split(':')[0])
            hora_fin = int(disponibilidad["hora_fin"].split(':')[0])
            horas_disponibles.extend([f"{h}:00" for h in range(hora_inicio, hora_fin)])
    return horas_disponibles

def todas_horas_disponibles(profesor, dia, hora_inicio, hora_fin):
    horas_disponibles = obtener_horas_disponibles(profesor, dia)
    for hora in rango_horas(hora_inicio, hora_fin):
        if hora not in horas_disponibles:
            return False
    return True

def rango_horas(hora_inicio, hora_fin):
    inicio = int(hora_inicio.split(':')[0])
    fin = int(hora_fin.split(':')[0])
    return [f"{h}:00" for h in range(inicio, fin)]

def seleccion(poblacion):
    poblacion = sorted(poblacion, key=lambda x: calcular_fitness(x), reverse=True)
    return poblacion[:2]

def cruce(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

def mutacion(individuo):
    if random.random() < 0.1:
        i = random.randint(0, len(individuo) - 1)
        idcurso = individuo[i][1]
        docentes_del_curso = [cd['idpersona'] for cd in CURSO_DOCENTE if cd['idcurso'] == idcurso]
        if docentes_del_curso:
            profesor = random.choice(docentes_del_curso)
        else:
            profesor = "No definido"
        
        dia = random.choice(DIAS)
        hora_inicio = random.choice(HORAS)
        duracion = random.choice(DURACIONES_CLASES)
        hora_fin = f"{int(hora_inicio.split(':')[0]) + duracion}:00"
        # Ajustar hora_fin si excede el límite de 23:00
        if int(hora_fin.split(':')[0]) > 23:
            hora_fin = "23:00"
        ambiente = next((ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == idcurso), "No definido")
        individuo[i] = (profesor, idcurso, individuo[i][2], ambiente, dia, hora_inicio, hora_fin)

def algoritmo_genetico():
    poblacion = generar_poblacion(10)
    
    for generacion in range(100):
        nueva_poblacion = []
        
        padres = seleccion(poblacion)
        
        while len(nueva_poblacion) < 10:
            padre1, padre2 = random.sample(padres, 2)
            hijo1, hijo2 = cruce(padre1, padre2)
            mutacion(hijo1)
            mutacion(hijo2)
            nueva_poblacion.extend([hijo1, hijo2])
        
        poblacion = nueva_poblacion
    
    mejor_individuo = max(poblacion, key=calcular_fitness)
    
    resultado = {}
    for (profesor, idcurso, idgrupo, aula, dia, hora_inicio, hora_fin) in mejor_individuo:
        # Verificar si el profesor está dentro del rango válido o es "No definido"
        if profesor != "No definido" and (profesor not in DOCENTES):
            continue  # Ignorar esta entrada si el profesor no es válido
        
        nombre_curso = CURSOS[idcurso]["nombre"]
        nombre_docente = "No definido" if profesor == "No definido" else DOCENTES[profesor]["nombres"]
        apellidos_docente = "" if profesor == "No definido" else DOCENTES[profesor]["apellidos"]
        
        # Validar índice de aula
        if aula == "No definido" or aula not in AMBIENTES:
            nombre_aula = "No definido"
        else:
            nombre_aula = AMBIENTES[aula]["nombre"]
        
        grupo = next((g for g in GRUPOS_HORARIO if g["id_grupo"] == idgrupo), None)
        
        if grupo:
            grupo_nombre = grupo["nombre"]
            if nombre_curso not in resultado:
                resultado[nombre_curso] = {}
            if grupo_nombre not in resultado[nombre_curso]:
                resultado[nombre_curso][grupo_nombre] = []
            resultado[nombre_curso][grupo_nombre].append({
                "docente": f"{nombre_docente} {apellidos_docente}",
                "aula": nombre_aula,
                "dia": dia,
                "hora_inicio": hora_inicio,
                "hora_fin": hora_fin if CURSOS[idcurso].get("horas_teoria", None) is not None else "No definidas"
            })
    
    return resultado

resultado_json = algoritmo_genetico()

#print(json.dumps(resultado_json, ensure_ascii=False, indent=4))
