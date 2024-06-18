import random

# Datos de ejemplo para cursos, docentes, ambientes y grupos
cursos = [
    {"idcurso": 1, "horas_practica": 3, "horas_teoria": 0, "ciclo": 1},
    {"idcurso": 2, "horas_practica": 2, "horas_teoria": 3, "ciclo": 1},
    {"idcurso": 3, "horas_practica": 1, "horas_teoria": 4, "ciclo": 2},
    {"idcurso": 4, "horas_practica": 2, "horas_teoria": 2, "ciclo": 2},
    {"idcurso": 5, "horas_practica": 3, "horas_teoria": 2, "ciclo": 3},
    {"idcurso": 6, "horas_practica": 2, "horas_teoria": 3, "ciclo": 3},
    {"idcurso": 7, "horas_practica": 1, "horas_teoria": 4, "ciclo": 4},
    {"idcurso": 8, "horas_practica": 2, "horas_teoria": 2, "ciclo": 4},
    {"idcurso": 9, "horas_practica": 3, "horas_teoria": 2, "ciclo": 5},
    {"idcurso": 10, "horas_practica": 2, "horas_teoria": 3, "ciclo": 5},
    {"idcurso": 11, "horas_practica": 1, "horas_teoria": 4, "ciclo": 6},
    {"idcurso": 12, "horas_practica": 0, "horas_teoria": 3, "ciclo": 6},
]

curso_docente = [
    {"idcurso": 1, "idpersona": [1, 4]},
    {"idcurso": 2, "idpersona": [2, 5]},
    {"idcurso": 3, "idpersona": [3, 6]},
    {"idcurso": 4, "idpersona": [4, 7]},
    {"idcurso": 5, "idpersona": [5, 8]},
    {"idcurso": 6, "idpersona": [2, 6]},
    {"idcurso": 7, "idpersona": [3, 9]},
    {"idcurso": 8, "idpersona": [8]},
    {"idcurso": 9, "idpersona": [1, 9]},
    {"idcurso": 10, "idpersona": [2, 10]},
    {"idcurso": 11, "idpersona": [6, 10]},
    {"idcurso": 12, "idpersona": [4, 7, 5]},
]

curso_ambiente = [
    {"idcurso": 1, "idambiente": [1, 2]},
    {"idcurso": 2, "idambiente": [2]},
    {"idcurso": 3, "idambiente": [3]},
    {"idcurso": 4, "idambiente": [4]},
    {"idcurso": 5, "idambiente": [1]},
    {"idcurso": 6, "idambiente": [2]},
    {"idcurso": 7, "idambiente": [4]},
    {"idcurso": 8, "idambiente": [4]},
    {"idcurso": 9, "idambiente": [3]},
    {"idcurso": 10, "idambiente": [2]},
    {"idcurso": 11, "idambiente": [3]},
    {"idcurso": 12, "idambiente": [1, 4]},
]

grupos = [
    {"idcurso": 1, "nombre": "A"},
    {"idcurso": 1, "nombre": "B"},
    {"idcurso": 2, "nombre": "A"},
    {"idcurso": 3, "nombre": "A"},
    {"idcurso": 4, "nombre": "A"},
    {"idcurso": 5, "nombre": "A"},
    {"idcurso": 6, "nombre": "A"},
    {"idcurso": 7, "nombre": "A"},
    {"idcurso": 8, "nombre": "A"},
    {"idcurso": 9, "nombre": "A"},
    {"idcurso": 10, "nombre": "A"},
    {"idcurso": 11, "nombre": "A"},
    {"idcurso": 12, "nombre": "A"},
    {"idcurso": 12, "nombre": "B"},
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
    {"idpersona": 1, "dia": "Lunes", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 1, "dia": "Miércoles", "hora_inicio": 14, "hora_fin": 18},
    {"idpersona": 1, "dia": "Sabado", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 1, "dia": "Viernes", "hora_inicio": 8, "hora_fin": 12},

    {"idpersona": 2, "dia": "Martes", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 2, "dia": "Jueves", "hora_inicio": 9, "hora_fin": 13},
    {"idpersona": 2, "dia": "Viernes", "hora_inicio": 14, "hora_fin": 18},
    {"idpersona": 2, "dia": "Miércoles", "hora_inicio": 14, "hora_fin": 18},

    {"idpersona": 3, "dia": "Miércoles", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 3, "dia": "Jueves", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 3, "dia": "Viernes", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 3, "dia": "Lunes", "hora_inicio": 10, "hora_fin": 14},

    {"idpersona": 4, "dia": "Jueves", "hora_inicio": 9, "hora_fin": 17},
    {"idpersona": 4, "dia": "Sabado", "hora_inicio": 14, "hora_fin": 18},
    {"idpersona": 4, "dia": "Miércoles", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 4, "dia": "Lunes", "hora_inicio": 9, "hora_fin": 13},

    {"idpersona": 5, "dia": "Lunes", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 5, "dia": "Sabado", "hora_inicio": 14, "hora_fin": 18},
    {"idpersona": 5, "dia": "Jueves", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 5, "dia": "Viernes", "hora_inicio": 8, "hora_fin": 12},

    {"idpersona": 6, "dia": "Martes", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 6, "dia": "Jueves", "hora_inicio": 9, "hora_fin": 13},
    {"idpersona": 6, "dia": "Viernes", "hora_inicio": 14, "hora_fin": 18},
    {"idpersona": 6, "dia": "Miércoles", "hora_inicio": 14, "hora_fin": 18},

    {"idpersona": 7, "dia": "Miércoles", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 7, "dia": "Jueves", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 7, "dia": "Viernes", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 7, "dia": "Lunes", "hora_inicio": 10, "hora_fin": 14},

    {"idpersona": 8, "dia": "Sabado", "hora_inicio": 9, "hora_fin": 17},
    {"idpersona": 8, "dia": "Viernes", "hora_inicio": 14, "hora_fin": 18},
    {"idpersona": 8, "dia": "Miércoles", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 8, "dia": "Lunes", "hora_inicio": 9, "hora_fin": 13},

    {"idpersona": 9, "dia": "Lunes", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 9, "dia": "Miércoles", "hora_inicio": 14, "hora_fin": 18},
    {"idpersona": 9, "dia": "Jueves", "hora_inicio": 8, "hora_fin": 12},
    {"idpersona": 9, "dia": "Sabado", "hora_inicio": 8, "hora_fin": 12},

    {"idpersona": 10, "dia": "Martes", "hora_inicio": 10, "hora_fin": 14},
    {"idpersona": 10, "dia": "Jueves", "hora_inicio": 9, "hora_fin": 13},
    {"idpersona": 10, "dia": "Sabado", "hora_inicio": 14, "hora_fin": 18},
    {"idpersona": 10, "dia": "Miércoles", "hora_inicio": 14, "hora_fin": 18},
]

# Función para obtener los días disponibles para un docente
def obtener_dias_disponibles(docente, disponibilidad_docente):
    if docente == "No definido" or docente is None:
        return ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    return [d["dia"] for d in disponibilidad_docente if d["idpersona"] == docente]

# Función para verificar la disponibilidad de un docente
def verificar_disponibilidad_docente(docente, dia, hora_inicio, hora_fin, disponibilidad_docente):
    if docente == "No definido" or docente is None:
        return True
    for disponibilidad in disponibilidad_docente:
        if disponibilidad["idpersona"] == docente and disponibilidad["dia"] == dia:
            if disponibilidad["hora_inicio"] <= hora_inicio and hora_fin <= disponibilidad["hora_fin"]:
                return True
    return False

# Función para verificar la disponibilidad de un ambiente
def verificar_disponibilidad_ambiente(horario, ambiente, dia, hora_inicio, hora_fin):
    for bloque in horario:
        if bloque["ambiente"] == ambiente and bloque["dia"] == dia:
            if not (hora_fin <= bloque["hora_inicio"] or hora_inicio >= bloque["hora_fin"]):
                return False
    return True

# Función para verificar la disponibilidad de un docente en un horario ya asignado
def verificar_no_choque_docente(horario, docente, dia, hora_inicio, hora_fin):
    for bloque in horario:
        if bloque["docente"] == docente and bloque["dia"] == dia:
            if not (hora_fin <= bloque["hora_inicio"] or hora_inicio >= bloque["hora_fin"]):
                return False
    return True

# Función para verificar que un docente no tenga el mismo horario en cursos de diferentes ciclos
def verificar_no_choque_ciclos(horario, docente, dia, hora_inicio, hora_fin, curso_actual, cursos):
    ciclo_actual = next(curso["ciclo"] for curso in cursos if curso["idcurso"] == curso_actual)
    for bloque in horario:
        if bloque["docente"] == docente and bloque["dia"] == dia and bloque["curso"] != curso_actual:
            ciclo_bloque = next(curso["ciclo"] for curso in cursos if curso["idcurso"] == bloque["curso"])
            if ciclo_actual != ciclo_bloque and not (hora_fin <= bloque["hora_inicio"] or hora_inicio >= bloque["hora_fin"]):
                return False
    return True

# Función para dividir horas en bloques de 2 o 3 horas
def dividir_horas_en_bloques(total_horas):
    bloques = []
    while total_horas > 0:
        if total_horas == 2:
            bloques.append(2)
            total_horas -= 2
        elif total_horas == 3:
            bloques.append(3)
            total_horas -= 3
        elif total_horas == 5:
            bloques.append(3)
            bloques.append(2)
            total_horas -= 5
        elif total_horas >= 4:
            bloques.append(2)
            total_horas -= 2
        else:
            bloques.append(3)
            total_horas -= 3
    return bloques

# Función para asegurar el descanso obligatorio
def asegurar_descanso(horario):
    for bloque in horario:
        if bloque["hora_inicio"] <= 12 < bloque["hora_fin"]:
            bloque["hora_fin"] = 12
        elif bloque["hora_inicio"] < 13 <= bloque["hora_fin"]:
            bloque["hora_inicio"] = 13
    return horario

# Inicialización de población
def inicializar_poblacion(tamaño_población, cursos, curso_docente, curso_ambiente, grupos, disponibilidad_docente):
    población = []
    for _ in range(tamaño_población):
        horario = []
        for grupo in grupos:
            curso = next((c for c in cursos if c["idcurso"] == grupo["idcurso"]), None)
            if curso is None:
                continue

            docentes_asignados = next((item["idpersona"] for item in curso_docente if item["idcurso"] == curso["idcurso"]), ["No definido"])
            ambientes_asignados = next((item["idambiente"] for item in curso_ambiente if item["idcurso"] == curso["idcurso"]), [None])

            if not docentes_asignados or not ambientes_asignados:
                print(f"Advertencia: No hay docentes o ambientes asignados para el curso {curso['idcurso']}")
                continue

            total_horas = curso["horas_practica"] + curso["horas_teoria"]
            bloques = dividir_horas_en_bloques(total_horas)

            for duracion in bloques:
                dia, hora_inicio, hora_fin, docente_asignado, ambiente_asignado = asignar_bloque(
                    docentes_asignados, ambientes_asignados, duracion, curso, disponibilidad_docente, horario)
                horario.append({
                    "curso": curso["idcurso"],
                    "grupo": grupo["nombre"],
                    "docente": docente_asignado,
                    "ambiente": ambiente_asignado,
                    "dia": dia,
                    "hora_inicio": hora_inicio,
                    "hora_fin": hora_fin
                })
        población.append(horario)
    return población

# Función para asignar un bloque horario
def asignar_bloque(docentes_asignados, ambientes_asignados, duracion, curso, disponibilidad_docente, horario):
    intentos = 0
    max_intentos = 100
    while intentos < max_intentos:
        docente_asignado = random.choice(docentes_asignados)
        ambiente_asignado = random.choice(ambientes_asignados)
        dias_disponibles = obtener_dias_disponibles(docente_asignado, disponibilidad_docente)
        dia = random.choice(dias_disponibles)
        if curso["idcurso"] % 2 == 1:  # Cursos impares
            hora_inicio = random.randint(7, 11 - duracion)  # Horario de inicio entre 7 y 11-duración horas
        else:  # Cursos pares
            hora_inicio = random.randint(14, 22 - duracion)  # Horario de inicio entre 14 y 22-duración horas
        hora_fin = hora_inicio + duracion
        if 12 < hora_inicio < 13 or 12 < hora_fin < 13:  # Asegurar descanso obligatorio
            continue
        if (verificar_disponibilidad_docente(docente_asignado, dia, hora_inicio, hora_fin, disponibilidad_docente) and
                verificar_disponibilidad_ambiente(horario, ambiente_asignado, dia, hora_inicio, hora_fin) and
                verificar_no_choque_docente(horario, docente_asignado, dia, hora_inicio, hora_fin) and
                verificar_no_choque_ciclos(horario, docente_asignado, dia, hora_inicio, hora_fin, curso["idcurso"], cursos)):
            return dia, hora_inicio, hora_fin, docente_asignado, ambiente_asignado
        intentos += 1
    print(f"Advertencia: No se encontró una disponibilidad válida para el curso {curso['idcurso']} con el docente {docente_asignado}")
    return "Lunes", 7, 9, "No definido", random.choice(ambientes_asignados)

# Evaluación de población (función fitness)
def evaluar_población(población, disponibilidad_docente):
    puntuaciones = []
    for horario in población:
        penalizacion = 0
        # Verificar colisiones de docentes y ambientes
        for i in range(len(horario)):
            for j in range(i + 1, len(horario)):
                if horario[i]["dia"] == horario[j]["dia"] and not (
                    horario[i]["hora_fin"] <= horario[j]["hora_inicio"] or
                    horario[j]["hora_fin"] <= horario[i]["hora_inicio"]
                ):
                    if horario[i]["docente"] == horario[j]["docente"] and horario[i]["docente"] != "No definido":
                        penalizacion += 1
                    if horario[i]["ambiente"] == horario[j]["ambiente"]:
                        penalizacion += 1
                    if horario[i]["grupo"] == horario[j]["grupo"]:
                        penalizacion += 1
        # Verificar disponibilidad de docentes
        for bloque in horario:
            if bloque["docente"] != "No definido":
                disponible = any(
                    d["idpersona"] == bloque["docente"] and d["dia"] == bloque["dia"] and 
                    d["hora_inicio"] <= bloque["hora_inicio"] < d["hora_fin"] and
                    d["hora_inicio"] < bloque["hora_fin"] <= d["hora_fin"]
                    for d in disponibilidad_docente
                )
                if not disponible:
                    penalizacion += 1
        puntuaciones.append(-penalizacion)  # Minimizar penalizaciones

    # Ajustar puntuaciones para evitar todas las negativas
    min_puntuacion = min(puntuaciones)
    if min_puntuacion < 0:
        puntuaciones = [p - min_puntuacion + 1 for p in puntuaciones]
    else:
        puntuaciones = [p + 1 for p in puntuaciones]  # Asegurar que no haya ceros

    return puntuaciones

# Selección de población
def seleccionar_población(población, fitness, cantidad):
    return random.choices(población, weights=fitness, k=cantidad)

# Cruce (Crossover)
def cruzar(horario1, horario2):
    punto_cruce = random.randint(1, len(horario1) - 1)
    hijo = horario1[:punto_cruce] + horario2[punto_cruce:]
    return hijo

# Mutación
def mutar(horario, tasa_mutación, disponibilidad_docente, cursos):
    for bloque in horario:
        if random.random() < tasa_mutación:
            intentos = 0
            max_intentos = 100
            dias_disponibles = obtener_dias_disponibles(bloque["docente"], disponibilidad_docente)
            while intentos < max_intentos:
                nuevo_dia = random.choice(dias_disponibles)  # Restringir días a los disponibles para el docente
                duracion = random.choice([2, 3])  # Duración de la clase de 2 o 3 horas
                if bloque["curso"] % 2 == 1:  # Cursos impares
                    nueva_hora_inicio = random.randint(7, 11 - duracion)
                else:  # Cursos pares
                    nueva_hora_inicio = random.randint(14, 22 - duracion)
                nueva_hora_fin = nueva_hora_inicio + duracion
                if 12 < nueva_hora_inicio < 13 or 12 < nueva_hora_fin < 13:  # Asegurar descanso obligatorio
                    continue
                if (verificar_disponibilidad_docente(bloque["docente"], nuevo_dia, nueva_hora_inicio, nueva_hora_fin, disponibilidad_docente) and
                        verificar_disponibilidad_ambiente(horario, bloque["ambiente"], nuevo_dia, nueva_hora_inicio, nueva_hora_fin) and
                        verificar_no_choque_docente(horario, bloque["docente"], nuevo_dia, nueva_hora_inicio, nueva_hora_fin) and
                        verificar_no_choque_ciclos(horario, bloque["docente"], nuevo_dia, nueva_hora_inicio, nueva_hora_fin, bloque["curso"], cursos)):
                    bloque["dia"] = nuevo_dia
                    bloque["hora_inicio"] = nueva_hora_inicio
                    bloque["hora_fin"] = nueva_hora_fin
                    break
                intentos += 1
            else:
                print(f"Advertencia: No se encontró una disponibilidad válida durante la mutación para el docente {bloque['docente']}")

# Algoritmo Genético Principal
def algoritmo_genetico(tamaño_población, generaciones, tasa_mutación, cursos, curso_docente, curso_ambiente, grupos, disponibilidad_docente):
    población = inicializar_poblacion(tamaño_población, cursos, curso_docente, curso_ambiente, grupos, disponibilidad_docente)
    
    for _ in range(generaciones):
        fitness = evaluar_población(población, disponibilidad_docente)
        print(f"Fitness: {fitness}")  # Imprimir para depurar
        padres = seleccionar_población(población, fitness, tamaño_población // 2)
        nueva_población = []
        
        while len(nueva_población) < tamaño_población:
            padre1, padre2 = random.sample(padres, 2)
            hijo = cruzar(padre1, padre2)
            mutar(hijo, tasa_mutación, disponibilidad_docente, cursos)
            nueva_población.append(hijo)
        
        población = nueva_población
    
    mejor_horario = max(población, key=lambda h: evaluar_población([h], disponibilidad_docente)[0])
    return mejor_horario

# Parámetros del Algoritmo Genético
tamaño_población = 10
generaciones = 50
tasa_mutación = 0.01

mejor_horario = algoritmo_genetico(tamaño_población, generaciones, tasa_mutación, cursos, curso_docente, curso_ambiente, grupos, disponibilidad_docente)
print("Mejor horario generado:")
for bloque in mejor_horario:
    print(bloque)
