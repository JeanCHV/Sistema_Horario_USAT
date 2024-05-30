import random
import json
import sys
import os

# Agrega el directorio base del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import controladores.docente.controlador_docente as controlador_docente
import controladores.ambientes.controlador_ambiente as controlador_ambiente
import controladores.cursos.controlador_cursos as controlador_cursos
import controladores.grupo.controlador_grupo as controlador_grupo
import controladores.docente_disponibilidad.controlador_docente_disponibilidad as controlador_docente_disponibilidad

docentes1 = controlador_docente.get_docentes()
ambientes1 = controlador_ambiente.get_ambientes()
cursos1 = controlador_cursos.get_cursos()
grupo= controlador_grupo.get_grupo()
disponibilidad=controlador_docente_disponibilidad.get_disponibilidad()

DOCENTES=docentes1
AMBIENTES=ambientes1
CURSOS=cursos1
GRUPOS_HORARIO =grupo
DISPONIBILIDAD_DOCENTES=disponibilidad

# Definición de parámetros
NUM_PROFESORES = len(docentes1)
NUM_CURSOS = len(cursos1)
NUM_AULAS = len(ambientes1)
HORAS = [f"{h}:00" for h in range(7, 23)]
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado"]

# Ejemplo de disponibilidad de docentes en formato JSON
# DISPONIBILIDAD_DOCENTES= '''
# [
#     {"dia": "Lunes", "hora_inicio": "9:00", "hora_fin": "11:00", "idpersona": 0},
#     {"dia": "Martes", "hora_inicio": "11:00", "hora_fin": "13:00", "idpersona": 0},
#     {"dia": "Lunes", "hora_inicio": "11:00", "hora_fin": "13:00", "idpersona": 1},
#     {"dia": "Miércoles", "hora_inicio": "13:00", "hora_fin": "15:00", "idpersona": 1},
#     {"dia": "Jueves", "hora_inicio": "9:00", "hora_fin": "11:00", "idpersona": 2},
#     {"dia": "Viernes", "hora_inicio": "15:00", "hora_fin": "17:00", "idpersona": 2},
#     {"dia": "Martes", "hora_inicio": "10:00", "hora_fin": "12:00", "idpersona": 3},
#     {"dia": "Jueves", "hora_inicio": "14:00", "hora_fin": "16:00", "idpersona": 3},
#     {"dia": "Miércoles", "hora_inicio": "10:00", "hora_fin": "12:00", "idpersona": 4},
#     {"dia": "Viernes", "hora_inicio": "9:00", "hora_fin": "11:00", "idpersona": 4}
# ]
# '''

# Datos de los docentes

# DOCENTES = [
#     {"idpersona": 0, "nombres": "Juan", "apellidos": "Perez", "cantHoras": 10, "tiempo_ref": 30},
#     {"idpersona": 1, "nombres": "Ana", "apellidos": "Gomez", "cantHoras": 8, "tiempo_ref": 30},
#     {"idpersona": 2, "nombres": "Luis", "apellidos": "Martinez", "cantHoras": 12, "tiempo_ref": 30},
#     {"idpersona": 3, "nombres": "Maria", "apellidos": "Lopez", "cantHoras": 10, "tiempo_ref": 30},
#     {"idpersona": 4, "nombres": "Carlos", "apellidos": "Diaz", "cantHoras": 15, "tiempo_ref": 30}
# ]

# Datos de los ambientes


# AMBIENTES = [
#     {"idambiente": 0, "nombre": "Aula 101", "aforo": 30},
#     {"idambiente": 1, "nombre": "Aula 102", "aforo": 25},
#     {"idambiente": 2, "nombre": "Laboratorio 201", "aforo": 20}
# ]

# Datos de los cursos

# CURSOS = [
#     {"idcurso": 0, "nombre": "Matemáticas", "horas_teoria": 2, "horas_practica": 1, "ciclo": 1, "tipo_curso": 'P'},
#     {"idcurso": 1, "nombre": "Física", "horas_teoria": 3, "horas_practica": 1, "ciclo": 1, "tipo_curso": 'P'},
#     {"idcurso": 2, "nombre": "Química", "horas_teoria": 2, "horas_practica": 2, "ciclo": 1, "tipo_curso": 'P'},
#     {"idcurso": 3, "nombre": "Biología", "horas_teoria": 1, "horas_practica": 2, "ciclo": 2, "tipo_curso": 'P'},
#     {"idcurso": 4, "nombre": "Historia", "horas_teoria": 3, "horas_practica": 0, "ciclo": 2, "tipo_curso": 'P'},
#     {"idcurso": 5, "nombre": "Geografía", "horas_teoria": 2, "horas_practica": 1, "ciclo": 2, "tipo_curso": 'P'},
#     {"idcurso": 6, "nombre": "Literatura", "horas_teoria": 2, "horas_practica": 1, "ciclo": 3, "tipo_curso": 'P'},
#     {"idcurso": 7, "nombre": "Inglés", "horas_teoria": 1, "horas_practica": 2, "ciclo": 3, "tipo_curso": 'P'},
#     {"idcurso": 8, "nombre": "Filosofía", "horas_teoria": 2, "horas_practica": 1, "ciclo": 3, "tipo_curso": 'P'},
#     {"idcurso": 9, "nombre": "Computación", "horas_teoria": 1, "horas_practica": 3, "ciclo": 3, "tipo_curso": 'P'}
# ]


# Datos de los grupos de horario

# GRUPOS_HORARIO = [
#     {"id_grupo": 0, "nombre": "Grupo A", "vacantes": 25, "idcurso": 0},
#     {"id_grupo": 1, "nombre": "Grupo B", "vacantes": 20, "idcurso": 1},
#     {"id_grupo": 2, "nombre": "Grupo C", "vacantes": 30, "idcurso": 2},
#     {"id_grupo": 3, "nombre": "Grupo D", "vacantes": 20, "idcurso": 3},
#     {"id_grupo": 4, "nombre": "Grupo E", "vacantes": 15, "idcurso": 4},
#     {"id_grupo": 5, "nombre": "Grupo F", "vacantes": 25, "idcurso": 5},
#     {"id_grupo": 6, "nombre": "Grupo G", "vacantes": 20, "idcurso": 6},
#     {"id_grupo": 7, "nombre": "Grupo H", "vacantes": 20, "idcurso": 7},
#     {"id_grupo": 8, "nombre": "Grupo I", "vacantes": 25, "idcurso": 8},
#     {"id_grupo": 9, "nombre": "Grupo J", "vacantes": 30, "idcurso": 9}
# ]

# Generar una población inicial
def generar_poblacion(tamano):
    return [[(random.randint(0, NUM_PROFESORES-1), i, random.randint(0, NUM_AULAS-1), random.choice(DIAS), random.choice(HORAS)) for i in range(NUM_CURSOS)] for _ in range(tamano)]

# Función de fitness
def calcular_fitness(horario):
    fitness = 0
    
    # Evitar solapamiento de horarios para el mismo profesor y respetar disponibilidad
    for dia in DIAS:
        horas_ocupadas = {profesor: [] for profesor in range(NUM_PROFESORES)}
        for (profesor, curso, aula, d, hora) in horario:
            if d == dia:
                if hora in horas_ocupadas[profesor] or hora not in obtener_horas_disponibles(profesor, d):
                    fitness -= 1
                else:
                    horas_ocupadas[profesor].append(hora)
                    
                # Verificar duración del curso
                horas_ocupadas_total = sum([CURSOS[curso]["horas_teoria"], CURSOS[curso]["horas_practica"]])
                if len(horas_ocupadas[profesor]) != horas_ocupadas_total:
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

# Selección
def seleccion(poblacion):
    poblacion = sorted(poblacion, key=lambda x: calcular_fitness(x), reverse=True)
    return poblacion[:2]

# Crossover
def cruce(padre1, padre2):
    punto_cruce = random.randint(1, NUM_CURSOS - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

# Mutación
def mutacion(individuo):
    if random.random() < 0.1:  # Tasa de mutación
        i = random.randint(0, NUM_CURSOS - 1)
        individuo[i] = (random.randint(0, NUM_PROFESORES-1), i, random.randint(0, NUM_AULAS-1), random.choice(DIAS), random.choice(HORAS))

# Algoritmo genético
def algoritmo_genetico():
    poblacion = generar_poblacion(10)
    
    for generacion in range(100):
        nueva_poblacion = []
        
        # Selección
        padres = seleccion(poblacion)
        
        # Crossover y mutación
        while len(nueva_poblacion) < 10:
            padre1, padre2 = random.sample(padres, 2)
            hijo1, hijo2 = cruce(padre1, padre2)
            mutacion(hijo1)
            mutacion(hijo2)
            nueva_poblacion.extend([hijo1, hijo2])
        
        poblacion = nueva_poblacion
        
        # Imprimir mejor resultado de la generación actual
        mejor_individuo = max(poblacion, key=calcular_fitness)
        print(f"Generación {generacion}: Mejor fitness: {calcular_fitness(mejor_individuo)}")
        for (profesor, curso, aula, dia, hora) in mejor_individuo:
            nombre_curso = CURSOS[curso]["nombre"]
            nombre_docente = DOCENTES[profesor]["nombres"]
            apellidos_docente = DOCENTES[profesor]["apellidos"]
            nombre_aula = AMBIENTES[aula]["nombre"]
            print(f"Docente {nombre_docente} {apellidos_docente} - Curso: {nombre_curso} - Aula: {nombre_aula} - Día: {dia} - Hora: {hora}")

# Ejecutar el algoritmo genético
algoritmo_genetico()