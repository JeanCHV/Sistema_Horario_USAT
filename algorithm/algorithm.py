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
grupo = controlador_grupo.get_grupo()
disponibilidad = controlador_docente_disponibilidad.get_disponibilidad()
curso_ambiente = controlador_curso_ambiente.get_curso_ambiente()

DOCENTES = docentes1
AMBIENTES = ambientes1
CURSOS = cursos1
GRUPOS_HORARIO = grupo
DISPONIBILIDAD_DOCENTES = disponibilidad
CURSO_AMBIENTE = curso_ambiente

NUM_PROFESORES = len(docentes1)
NUM_CURSOS = len(cursos1)
NUM_AULAS = len(ambientes1)
HORAS = [f"{h}:00" for h in range(7, 23)]
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

# Depuración: Mostrar la estructura de GRUPOS_HORARIO
#print("GRUPOS_HORARIO:", json.dumps(GRUPOS_HORARIO, indent=4, ensure_ascii=False))

def generar_poblacion(tamano):
    poblacion = []
    for _ in range(tamano):
        horario = []
        for curso in CURSOS:
            idcurso = curso['idcurso']
            for grupo in GRUPOS_HORARIO:
                if grupo['idcurso'] == idcurso:
                    profesor = random.randint(0, NUM_PROFESORES - 1)
                    dia = random.choice(DIAS)
                    hora = random.choice(HORAS)
                    if any(ca['idcurso'] == idcurso for ca in CURSO_AMBIENTE):
                        ambiente = next(ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == idcurso)
                    else:
                        ambiente = random.randint(0, NUM_AULAS - 1)
                    horario.append((profesor, idcurso, grupo['id_grupo'], ambiente, dia, hora))
        poblacion.append(horario)
    return poblacion

def calcular_fitness(horario):
    fitness = 0
    
    for dia in DIAS:
        horas_ocupadas = {profesor: [] for profesor in range(NUM_PROFESORES)}
        for (profesor, idcurso, idgrupo, aula, d, hora) in horario:
            if d == dia:
                if hora in horas_ocupadas[profesor] or hora not in obtener_horas_disponibles(profesor, d):
                    fitness -= 1
                else:
                    horas_ocupadas[profesor].append(hora)
                    
                horas_ocupadas_total = sum([curso["horas_teoria"] for curso in CURSOS if curso["idcurso"] == idcurso])
                if len(horas_ocupadas[profesor]) != horas_ocupadas_total:
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
        profesor = random.randint(0, NUM_PROFESORES - 1)
        dia = random.choice(DIAS)
        hora = random.choice(HORAS)
        idcurso = individuo[i][1]
        if any(ca['idcurso'] == idcurso for ca in CURSO_AMBIENTE):
            ambiente = next(ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == idcurso)
        else:
            ambiente = random.randint(0, NUM_AULAS - 1)
        individuo[i] = (profesor, idcurso, individuo[i][2], ambiente, dia, hora)

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
    for (profesor, idcurso, idgrupo, aula, dia, hora) in mejor_individuo:
        nombre_curso = next(curso["nombre"] for curso in CURSOS if curso["idcurso"] == idcurso)
        nombre_docente = DOCENTES[profesor]["nombres"]
        apellidos_docente = DOCENTES[profesor]["apellidos"]
        
        # Validar índice de aula
        if aula < 0 or aula >= len(AMBIENTES):
            continue  # Ignorar esta entrada si el aula no es válida
        
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
                "hora": hora
            })
    
    return resultado

resultado_json = algoritmo_genetico()
print(json.dumps(resultado_json, ensure_ascii=False, indent=4))
