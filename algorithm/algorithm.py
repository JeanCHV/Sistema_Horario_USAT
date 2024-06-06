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
grupos = controlador_grupo.get_grupo()
disponibilidad = controlador_docente_disponibilidad.get_disponibilidad()
curso_ambiente = controlador_curso_ambiente.get_curso_ambiente()

DOCENTES = docentes1
AMBIENTES = ambientes1
CURSOS = cursos1
GRUPOS = grupos
DISPONIBILIDAD_DOCENTES = disponibilidad
CURSO_AMBIENTE = curso_ambiente

NUM_PROFESORES = len(docentes1)
NUM_CURSOS = len(cursos1)
NUM_AULAS = len(ambientes1)
HORAS = [f"{h}:00" for h in range(7, 23)]
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

def generar_poblacion(tamano):
    poblacion = []
    for _ in range(tamano):
        horario = []
        for curso in range(NUM_CURSOS):
            profesor = random.randint(0, NUM_PROFESORES - 1)
            dia = random.choice(DIAS)
            hora_inicio = random.choice(HORAS)
            duracion = CURSOS[curso]["horas_teoria"] + CURSOS[curso]["horas_practica"]
            hora_fin = f"{int(hora_inicio.split(':')[0]) + duracion}:00"
            if any(ca['idcurso'] == curso for ca in CURSO_AMBIENTE):
                ambiente = next(ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == curso)
            else:
                ambiente = random.randint(0, NUM_AULAS - 1)
            if ambiente >= len(AMBIENTES):
                ambiente = random.randint(0, len(AMBIENTES) - 1)
            grupo = next((g for g in GRUPOS if g["idcurso"] == curso), None)
            horario.append((profesor, curso, ambiente, dia, hora_inicio, hora_fin, grupo))
        poblacion.append(horario)
    return poblacion

def calcular_fitness(horario):
    fitness = 0
    
    for dia in DIAS:
        horas_ocupadas = {profesor: [] for profesor in range(NUM_PROFESORES)}
        for (profesor, curso, aula, d, hora_inicio, hora_fin, grupo) in horario:
            if d == dia:
                if hora_inicio in horas_ocupadas[profesor] or hora_inicio not in obtener_horas_disponibles(profesor, d):
                    fitness -= 1
                else:
                    horas_ocupadas[profesor].append(hora_inicio)
                    
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
    hijo2 = padre2[:punto_cruce] + padre1[:punto_cruce:]
    return hijo1, hijo2

def mutacion(individuo):
    if individuo:  # Verificar si la lista individuo no está vacía
        i = random.randint(0, len(individuo) - 1)
        profesor = random.randint(0, NUM_PROFESORES - 1)
        dia = random.choice(DIAS)
        hora_inicio = random.choice(HORAS)
        curso = individuo[i][1]  # Obtener el curso actual en la posición i
        duracion = CURSOS[curso]["horas_teoria"] + CURSOS[curso]["horas_practica"]
        hora_fin = f"{int(hora_inicio.split(':')[0]) + duracion}:00"
        if any(ca['idcurso'] == curso for ca in CURSO_AMBIENTE):
            ambiente = next(ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == curso)
        else:
            ambiente = random.randint(0, NUM_AULAS - 1)
        grupo = next((g for g in GRUPOS if g["idcurso"] == curso), None)
        individuo[i] = (profesor, curso, ambiente, dia, hora_inicio, hora_fin, grupo)

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
    
    resultado = {
        "Generacion": 99,
        "Mejor_fitness": calcular_fitness(mejor_individuo),
        "Horario": []
    }
    
    for curso in range(NUM_CURSOS):
        encontrado = False
        for (profesor, curso_id, aula, dia, hora_inicio, hora_fin, grupo) in mejor_individuo:
            if curso_id == curso:
                nombre_curso = CURSOS[curso]["nombre"]
                nombre_docente = DOCENTES[profesor]["nombres"]
                apellidos_docente = DOCENTES[profesor]["apellidos"]
                if aula < len(AMBIENTES):
                    nombre_aula = AMBIENTES[aula]["nombre"]
                else:
                    nombre_aula = "Aula desconocida"
                resultado["Horario"].append({
                    "Docente": f"{nombre_docente} {apellidos_docente}",
                    "Curso": nombre_curso,
                    "Aula": nombre_aula,
                    "Dia": dia,
                    "Hora_inicio": hora_inicio,
                    "Hora_fin": hora_fin,
                    "Grupo": grupo["nombre"] if grupo else "Desconocido"
                })
                encontrado = True
                break
        if not encontrado:
            # Asignar al menos día, hora y aula para cursos no asignados
            dia = random.choice(DIAS)
            hora_inicio = random.choice(HORAS)
            duracion = CURSOS[curso]["horas_teoria"] + CURSOS[curso]["horas_practica"]
            hora_fin = f"{int(hora_inicio.split(':')[0]) + duracion}:00"
            aula = random.randint(0, len(AMBIENTES) - 1)
            nombre_aula = AMBIENTES[aula]["nombre"]
            grupo = next((g for g in GRUPOS if g["idcurso"] == curso), None)
            resultado["Horario"].append({
                "Docente": "Desconocido",
                "Curso": CURSOS[curso]["nombre"],
                "Aula": nombre_aula,
                "Dia": dia,
                "Hora_inicio": hora_inicio,
                "Hora_fin": hora_fin,
                "Grupo": 
                
                
                
                
                ["nombre"] if grupo else "Desconocido"
            })
    
    return resultado

# Ejecutar el algoritmo y obtener la mejor generación en formato JSON
# mejor_horario = algoritmo_genetico()
# print(json.dumps(mejor_horario, indent=4, ensure_ascii=False))
