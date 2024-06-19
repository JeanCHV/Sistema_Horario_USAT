import random

# Datos de ejemplo para cursos, docentes, ambientes y grupos
cursos = [
    {"idcurso": 1, "horas_practica": 2, "horas_teoria": 1, "ciclo": 1},
    {"idcurso": 2, "horas_practica": 3, "horas_teoria": 2, "ciclo": 1},
    {"idcurso": 3, "horas_practica": 1, "horas_teoria": 4, "ciclo": 2},
    {"idcurso": 4, "horas_practica": 2, "horas_teoria": 3, "ciclo": 2},
    {"idcurso": 5, "horas_practica": 3, "horas_teoria": 1, "ciclo": 3},
    {"idcurso": 6, "horas_practica": 1, "horas_teoria": 2, "ciclo": 3},
    {"idcurso": 7, "horas_practica": 2, "horas_teoria": 2, "ciclo": 4},
    {"idcurso": 8, "horas_practica": 3, "horas_teoria": 3, "ciclo": 4},
    {"idcurso": 9, "horas_practica": 2, "horas_teoria": 1, "ciclo": 5},
    {"idcurso": 10, "horas_practica": 3, "horas_teoria": 2, "ciclo": 5},
    {"idcurso": 11, "horas_practica": 1, "horas_teoria": 4, "ciclo": 6},
    {"idcurso": 12, "horas_practica": 0, "horas_teoria": 3, "ciclo": 6},
    {"idcurso": 13, "horas_practica": 2, "horas_teoria": 1, "ciclo": 7},
    {"idcurso": 14, "horas_practica": 3, "horas_teoria": 2, "ciclo": 7},
    {"idcurso": 15, "horas_practica": 1, "horas_teoria": 4, "ciclo": 8},
    {"idcurso": 16, "horas_practica": 2, "horas_teoria": 3, "ciclo": 8},
]

curso_docente = [
    {"idcurso": 1, "idgrupo": 1, "idpersona": [1, 2]},
    {"idcurso": 2, "idgrupo": 2, "idpersona": [2, 3]},
    {"idcurso": 3, "idgrupo": 3, "idpersona": [3, 4]},
    {"idcurso": 4, "idgrupo": 4, "idpersona": [4, 5]},
    {"idcurso": 5, "idgrupo": 5, "idpersona": [5, 6]},
    {"idcurso": 6, "idgrupo": 6, "idpersona": [6, 7]},
    {"idcurso": 7, "idgrupo": 7, "idpersona": [7, 8]},
    {"idcurso": 8, "idgrupo": 8, "idpersona": [8, 9]},
    {"idcurso": 9, "idgrupo": 9, "idpersona": [9, 10]},
    {"idcurso": 10, "idgrupo": 10, "idpersona": [10, 1]},
    {"idcurso": 11, "idgrupo": 11, "idpersona": [1, 3]},
    {"idcurso": 12, "idgrupo": 12, "idpersona": [2, 4]},
    {"idcurso": 13, "idgrupo": 13, "idpersona": [3, 5]},
    {"idcurso": 14, "idgrupo": 14, "idpersona": [4, 6]},
    {"idcurso": 15, "idgrupo": 15, "idpersona": [5, 7]},
    {"idcurso": 16, "idgrupo": 16, "idpersona": [6, 8]},
]

curso_ambiente = [
    {"idcurso": 1, "idambiente": [1, 2]},
    {"idcurso": 2, "idambiente": [2, 3]},
    {"idcurso": 3, "idambiente": [3, 4]},
    {"idcurso": 4, "idambiente": [1, 4]},
    {"idcurso": 5, "idambiente": [1, 3]},
    {"idcurso": 6, "idambiente": [2, 4]},
    {"idcurso": 7, "idambiente": [1, 3]},
    {"idcurso": 8, "idambiente": [2, 4]},
    {"idcurso": 9, "idambiente": [1, 4]},
    {"idcurso": 10, "idambiente": [2, 3]},
    {"idcurso": 11, "idambiente": [3, 4]},
    {"idcurso": 12, "idambiente": [1, 2]},
    {"idcurso": 13, "idambiente": [2, 3]},
    {"idcurso": 14, "idambiente": [3, 4]},
    {"idcurso": 15, "idambiente": [1, 2]},
    {"idcurso": 16, "idambiente": [2, 3]},
]


grupos = [
    {"idgrupo": 1, "nombreGrupo": "A", "idcurso": 1},
    {"idgrupo": 2, "nombreGrupo": "B", "idcurso": 2},
    {"idgrupo": 3, "nombreGrupo": "A", "idcurso": 3},
    {"idgrupo": 4, "nombreGrupo": "B", "idcurso": 4},
    {"idgrupo": 5, "nombreGrupo": "A", "idcurso": 5},
    {"idgrupo": 6, "nombreGrupo": "B", "idcurso": 6},
    {"idgrupo": 7, "nombreGrupo": "A", "idcurso": 7},
    {"idgrupo": 8, "nombreGrupo": "B", "idcurso": 8},
    {"idgrupo": 9, "nombreGrupo": "A", "idcurso": 9},
    {"idgrupo": 10, "nombreGrupo": "B", "idcurso": 10},
    {"idgrupo": 11, "nombreGrupo": "A", "idcurso": 11},
    {"idgrupo": 12, "nombreGrupo": "B", "idcurso": 12},
    {"idgrupo": 13, "nombreGrupo": "A", "idcurso": 13},
    {"idgrupo": 14, "nombreGrupo": "B", "idcurso": 14},
    {"idgrupo": 15, "nombreGrupo": "A", "idcurso": 15},
    {"idgrupo": 16, "nombreGrupo": "B", "idcurso": 16},
]


docentes = [
    {"idpersona": 1, "nombre": "Docente 1"},
    {"idpersona": 2, "nombre": "Docente 2"},
    {"idpersona": 3, "nombre": "Docente 3"},
    {"idpersona": 4, "nombre": "Docente 4"},
    {"idpersona": 5, "nombre": "Docente 5"},
    {"idpersona": 6, "nombre": "Docente 6"},
    {"idpersona": 7, "nombre": "Docente 7"},
    {"idpersona": 8, "nombre": "Docente 8"},
    {"idpersona": 9, "nombre": "Docente 9"},
    {"idpersona": 10, "nombre": "Docente 10"},
]


ambientes = [
    {"idambiente": 1, "nombre": "Ambiente 1"},
    {"idambiente": 2, "nombre": "Ambiente 2"},
    {"idambiente": 3, "nombre": "Ambiente 3"},
    {"idambiente": 4, "nombre": "Ambiente 4"},
]


disponibilidad_docente = [
    {"idpersona": 1, "dia": "Lunes", "hora_inicio": 8, "hora_fin": 15},
    {"idpersona": 1, "dia": "Martes", "hora_inicio": 10, "hora_fin": 18},
    {"idpersona": 1, "dia": "Jueves", "hora_inicio": 8, "hora_fin": 15},
    {"idpersona": 1, "dia": "Viernes", "hora_inicio": 10, "hora_fin": 18},
    {"idpersona": 2, "dia": "Miércoles", "hora_inicio": 8, "hora_fin": 14},
    {"idpersona": 2, "dia": "Jueves", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 3, "dia": "Viernes", "hora_inicio": 14, "hora_fin": 18},
    {"idpersona": 3, "dia": "Lunes", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 4, "dia": "Sábado", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 4, "dia": "Jueves", "hora_inicio": 14, "hora_fin": 18},
    {"idpersona": 5, "dia": "Miércoles", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 5, "dia": "Viernes", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 6, "dia": "Lunes", "hora_inicio": 14, "hora_fin": 18},
    {"idpersona": 6, "dia": "Martes", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 7, "dia": "Miércoles", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 7, "dia": "Jueves", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 8, "dia": "Sábado", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 8, "dia": "Lunes", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 9, "dia": "Martes", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 9, "dia": "Jueves", "hora_inicio": 14, "hora_fin": 18},
    {"idpersona": 10, "dia": "Sábado", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 10, "dia": "Viernes", "hora_inicio": 14, "hora_fin": 18},
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
    for curso in cursos:
        horas_totales = curso["horas_practica"] + curso["horas_teoria"]
        bloques_horarios = generar_bloques_horarios(horas_totales)
        for grupo in [g for g in grupos if g["idcurso"] == curso["idcurso"]]:
            for bloque in bloques_horarios:
                dia = random.choice(dias)
                if curso["idcurso"] % 2 != 0:
                    hora_inicio = random.randint(7, 14 - bloque)  # Cursos impares en la mañana
                else:
                    hora_inicio = random.randint(14, 22 - bloque)  # Cursos pares en la tarde
                hora_fin = hora_inicio + bloque
                entrada_horario = {
                    "idcurso": curso["idcurso"],
                    "idgrupo": grupo["idgrupo"],
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
        curso_doc = next((item for item in curso_docente if item["idcurso"] == entrada["idcurso"] and item["idgrupo"] == entrada["idgrupo"]), None)
        curso_amb = next((item for item in curso_ambiente if item["idcurso"] == entrada["idcurso"]), None)
        
        # Verificar si ya se ha asignado un docente al grupo
        grupo_key = (entrada["idcurso"], entrada["idgrupo"])
        if grupo_key in grupos_asignados:
            docente_asignado = grupos_asignados[grupo_key]
        else:
            docente_asignado = "No definido"
            if curso_doc:
                for idpersona in curso_doc["idpersona"]:
                    disponible = all(verificar_disponibilidad_docente(idpersona, e["dia"], e["hora_inicio"], e["hora_fin"]) and not verificar_colision_docente(idpersona, e["dia"], e["hora_inicio"], e["hora_fin"], horarios_docentes) for e in horario if e["idcurso"] == entrada["idcurso"] and e["idgrupo"] == entrada["idgrupo"])
                    if disponible:
                        docente_asignado = idpersona
                        grupos_asignados[grupo_key] = docente_asignado
                        break
        
        if curso_amb:
            ambiente_asignado = "No definido"
            for idambiente in curso_amb["idambiente"]:
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
generaciones = 10000
poblacion_size = 100

# Ejecutar el algoritmo genético
mejor_horario, precision = algoritmo_genetico(generaciones, poblacion_size)

# Imprimir el mejor horario generado y su precisión
print("Mejor Horario Generado:")
for entrada in mejor_horario:
    print(entrada)
print(f"\nPrecisión del Horario: {precision:.2f}%")
