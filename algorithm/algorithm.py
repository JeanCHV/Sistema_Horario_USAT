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

docentes1 = controlador_docente.get_docentes()
ambientes1 = controlador_ambiente.get_ambientes()
cursos1 = controlador_cursos.get_cursos()
grupo= controlador_grupo.get_grupo()
disponibilidad=controlador_docente_disponibilidad.get_disponibilidad()
curso_ambiente = controlador_curso_ambiente.get_curso_ambiente()

DOCENTES=docentes1
AMBIENTES=ambientes1
CURSOS=cursos1
GRUPOS_HORARIO =grupo
DISPONIBILIDAD_DOCENTES=disponibilidad
CURSO_AMBIENTE = curso_ambiente

NUM_PROFESORES = len(docentes1)
NUM_CURSOS = len(cursos1)
NUM_AULAS = len(ambientes1)
HORAS = [f"{h}:00" for h in range(7, 23)]
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado"]

def generar_poblacion(tamano):
    poblacion = []
    for _ in range(tamano):
        horario = []
        for curso in range(NUM_CURSOS):
            profesor = random.randint(0, NUM_PROFESORES - 1)
            dia = random.choice(DIAS)
            hora = random.choice(HORAS)
            if any(ca['idcurso'] == curso for ca in CURSO_AMBIENTE):
                ambiente = next(ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == curso)
            else:
                ambiente = random.randint(0, NUM_AULAS - 1)
            horario.append((profesor, curso, ambiente, dia, hora))
        poblacion.append(horario)
    return poblacion

def calcular_fitness(horario):
    fitness = 0
    
    for dia in DIAS:
        horas_ocupadas = {profesor: [] for profesor in range(NUM_PROFESORES)}
        for (profesor, curso, aula, d, hora) in horario:
            if d == dia:
                if hora in horas_ocupadas[profesor] or hora not in obtener_horas_disponibles(profesor, d):
                    fitness -= 1
                else:
                    horas_ocupadas[profesor].append(hora)
                    
                horas_ocupadas_total = sum([CURSOS[curso]["horas_teoria"], CURSOS[curso]["horas_practica"]])
                if len(horas_ocupadas[profesor]) != horas_ocupadas_total:
                    fitness -= 1

                if any(ca['idcurso'] == curso for ca in CURSO_AMBIENTE):
                    ambiente_especifico = next(ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == curso)
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

def seleccion(poblacion):
    poblacion = sorted(poblacion, key=lambda x: calcular_fitness(x), reverse=True)
    return poblacion[:2]

def cruce(padre1, padre2):
    punto_cruce = random.randint(1, NUM_CURSOS - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

def mutacion(individuo):
    if random.random() < 0.1:
        i = random.randint(0, NUM_CURSOS - 1)
        profesor = random.randint(0, NUM_PROFESORES - 1)
        dia = random.choice(DIAS)
        hora = random.choice(HORAS)
        if any(ca['idcurso'] == individuo[i][1] for ca in CURSO_AMBIENTE):
            ambiente = next(ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == individuo[i][1])
        else:
            ambiente = random.randint(0, NUM_AULAS - 1)
        individuo[i] = (profesor, individuo[i][1], ambiente, dia, hora)

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
        print(f"Generación {generacion}: Mejor fitness: {calcular_fitness(mejor_individuo)}")
        for (profesor, curso, aula, dia, hora) in mejor_individuo:
            nombre_curso = CURSOS[curso]["nombre"]
            nombre_docente = DOCENTES[profesor]["nombres"]
            apellidos_docente = DOCENTES[profesor]["apellidos"]
            nombre_aula = AMBIENTES[aula]["nombre"]
            print(f"Docente {nombre_docente} {apellidos_docente} - Curso: {nombre_curso} - Aula: {nombre_aula} - Día: {dia} - Hora: {hora}")

algoritmo_genetico()
