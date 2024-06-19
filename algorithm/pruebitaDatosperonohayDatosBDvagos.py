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

# Obtener los datos desde la base de datos
docentes1 = controlador_docente.get_docentes()
ambientes1 = controlador_ambiente.get_ambientes()
cursos1 = controlador_cursos.get_cursos()
grupo = controlador_grupo.get_grupo()
disponibilidad = controlador_docente_disponibilidad.get_disponibilidad()
curso_ambiente = controlador_curso_ambiente.get_curso_ambiente()
curso_docente = controlador_curso_docente.get_curso_docente()

# Convertir los datos en estructuras adecuadas
DOCENTES = {docente['idpersona']: docente for docente in docentes1}
AMBIENTES = {ambiente['idambiente']: ambiente for ambiente in ambientes1}
CURSOS = {curso['idcurso']: curso for curso in cursos1}
GRUPOS = grupo
DISPONIBILIDAD_DOCENTES = disponibilidad
CURSO_AMBIENTE = curso_ambiente
CURSO_DOCENTE = curso_docente

# Convertir las disponibilidades a un formato adecuado
disponibilidad_docente = [
    {"idpersona": d['idpersona'], "dia": d['dia'], "hora_inicio": int(d['hora_inicio'].split(':')[0]), "hora_fin": int(d['hora_fin'].split(':')[0])}
    for d in DISPONIBILIDAD_DOCENTES
]

# Generar bloques horarios para cada curso
def generar_bloques_horarios(horas_totales):
    bloques = []
    while horas_totales > 0:
        if horas_totales >= 5:
            bloques.append(3)
            horas_totales -= 3
        elif horas_totales == 4:
            bloques.append(2)
            bloques.append(2)
            horas_totales -= 4
        elif horas_totales == 3:
            bloques.append(3)
            horas_totales -= 3
        elif horas_totales == 2:
            bloques.append(2)
            horas_totales -= 2
    return bloques

# Generar horarios iniciales con bloques de 2 o 3 horas
def generar_horario():
    horario = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    for curso in CURSOS.values():
        horas_totales = curso["horas_practica"] + curso["horas_teoria"]
        bloques_horarios = generar_bloques_horarios(horas_totales)
        for grupo in [g for g in GRUPOS if g["idcurso"] == curso["idcurso"]]:
            for bloque in bloques_horarios:
                dia = random.choice(dias)
                if curso["idcurso"] % 2 != 0:
                    hora_inicio = random.randint(7, 14 - bloque)  # Cursos impares en la mañana
                else:
                    hora_inicio = random.randint(14, 22 - bloque)  # Cursos pares en la tarde
                hora_fin = hora_inicio + bloque
                entrada_horario = {
                    "idcurso": curso["idcurso"],
                    "idgrupo": grupo["id_grupo"],
                    "idpersona": "No definido",
                    "idambiente": "No definido",
                    "dia": dia,
                    "hora_inicio": hora_inicio,
                    "hora_fin": hora_fin,
                    "duracion": bloque
                }
                horario.append(entrada_horario)
    return horario

# Verificar la disponibilidad de los docentes
def verificar_disponibilidad_docente(idpersona, dia, hora_inicio, hora_fin):
    disponibilidad = next((item for item in disponibilidad_docente if item["idpersona"] == idpersona and item["dia"] == dia), None)
    if disponibilidad and disponibilidad["hora_inicio"] <= hora_inicio and disponibilidad["hora_fin"] >= hora_fin:
        return True
    return False

# Verificar colisiones de horarios de docentes
def verificar_colision_docente(idpersona, dia, hora_inicio, hora_fin, horarios_docentes):
    for key in horarios_docentes:
        if key[0] == idpersona and key[1] == dia:
            if not (hora_fin <= key[2] or hora_inicio >= key[3]):
                return True
    return False

# Verificar colisiones de horarios de ambientes
def verificar_colision_ambiente(idambiente, dia, hora_inicio, hora_fin, horarios_ambientes):
    for key in horarios_ambientes:
        if key[0] == idambiente and key[1] == dia:
            if not (hora_fin <= key[2] or hora_inicio >= key[3]):
                return True
    return False

# Asignar horarios sin colisiones
def asignar_horarios(horario):
    horarios_docentes = {}
    horarios_ambientes = {}
    grupos_asignados = {}
    
    for entrada in horario:
        curso_doc = [item for item in CURSO_DOCENTE if item["idcurso"] == entrada["idcurso"]]
        curso_amb = [item for item in CURSO_AMBIENTE if item["idcurso"] == entrada["idcurso"]]
        
        # Verificar si ya se ha asignado un docente al grupo
        grupo_key = (entrada["idcurso"], entrada["idgrupo"])
        if grupo_key in grupos_asignados:
            docente_asignado = grupos_asignados[grupo_key]
        else:
            docente_asignado = "No definido"
            if curso_doc:
                for idpersona in [doc["idpersona"] for doc in curso_doc]:
                    disponible = all(verificar_disponibilidad_docente(idpersona, e["dia"], e["hora_inicio"], e["hora_fin"]) and not verificar_colision_docente(idpersona, e["dia"], e["hora_inicio"], e["hora_fin"], horarios_docentes) for e in horario if e["idcurso"] == entrada["idcurso"] and e["idgrupo"] == entrada["idgrupo"])
                    if disponible:
                        docente_asignado = idpersona
                        grupos_asignados[grupo_key] = docente_asignado
                        break
        
        ambiente_asignado = "No definido"
        if curso_amb:
            for idambiente in [amb["idambiente"] for amb in curso_amb]:
                if not verificar_colision_ambiente(idambiente, entrada["dia"], entrada["hora_inicio"], entrada["hora_fin"], horarios_ambientes):
                    ambiente_asignado = idambiente
                    break
        
        entrada["idpersona"] = docente_asignado
        entrada["idambiente"] = ambiente_asignado
        
        if docente_asignado != "No definido":
            horarios_docentes[(docente_asignado, entrada["dia"], entrada["hora_inicio"], entrada["hora_fin"])] = entrada
        if ambiente_asignado != "No definido":
            horarios_ambientes[(ambiente_asignado, entrada["dia"], entrada["hora_inicio"], entrada["hora_fin"])] = entrada
    
    return horario

# Verificar que no haya choques de horarios de docentes
def verificar_choques(horario):
    horarios_docentes = {}
    for entrada in horario:
        if entrada["idpersona"] != "No definido" and entrada["idambiente"] != "No definido":
            docente_key = (entrada["idpersona"], entrada["dia"], entrada["hora_inicio"], entrada["hora_fin"])
            if docente_key in horarios_docentes:
                return False
            horarios_docentes[docente_key] = entrada
    return True

# Evaluar la aptitud de un horario
def evaluar_horario(horario):
    if not verificar_choques(horario):
        return 0
    score = 0
    for entrada in horario:
        if entrada["idpersona"] != "No definido" and entrada["idambiente"] != "No definido" and entrada["dia"] != "No definido":
            score += 1
    return score

# Calcular la precisión del horario generado
def calcular_precision(horario):
    total_entradas = len(horario)
    entradas_definidas = sum(1 for entrada in horario if entrada["idpersona"] != "No definido" and entrada["idambiente"] != "No definido")
    precision = (entradas_definidas / total_entradas) * 100
    return precision

# Algoritmo genético
def algoritmo_genetico(generaciones, poblacion_size):
    poblacion = [asignar_horarios(generar_horario()) for _ in range(poblacion_size)]
    mejor_horario = None
    mejor_score = -1
    for _ in range(generaciones):
        poblacion.sort(key=evaluar_horario, reverse=True)
        if evaluar_horario(poblacion[0]) > mejor_score:
            mejor_score = evaluar_horario(poblacion[0])
            mejor_horario = poblacion[0]
        nueva_poblacion = poblacion[:poblacion_size // 2]
        for _ in range(poblacion_size // 2, poblacion_size):
            padre = random.choice(nueva_poblacion)
            madre = random.choice(nueva_poblacion)
            hijo = crossover(padre, madre)
            hijo = mutacion(hijo)
            nueva_poblacion.append(hijo)
        poblacion = nueva_poblacion
    return mejor_horario, calcular_precision(mejor_horario)

# Función de cruce (crossover)
def crossover(padre, madre):
    hijo = padre[:len(padre) // 2] + madre[len(madre) // 2:]
    return hijo

# Función de mutación
def mutacion(hijo):
    if random.random() < 0.1:
        index = random.randint(0, len(hijo) - 1)
        hijo[index] = generar_horario()[index]
    return hijo

# Parámetros del algoritmo genético
generaciones = 1000
poblacion_size = 100

# Ejecutar el algoritmo genético
mejor_horario, precision = algoritmo_genetico(generaciones, poblacion_size)

# Imprimir el mejor horario generado y su precisión
print("Mejor Horario Generado:")
for entrada in mejor_horario:
    print(entrada)
print(f"\nPrecisión del Horario: {precision:.2f}%")
