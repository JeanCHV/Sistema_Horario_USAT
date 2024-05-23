import random

# Definición de parámetros
NUM_PROFESORES = 5
NUM_CURSOS = 10
NUM_AULAS = 3
HORAS = [f"{h}:00" for h in range(9, 18)]
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Ejemplo de disponibilidad de docentes: {docente: [(día, hora_inicio, hora_fin)]}
DISPONIBILIDAD_DOCENTES = {
    0: [("Lunes", "9:00", "11:00"), ("Martes", "11:00", "13:00")],
    1: [("Lunes", "11:00", "13:00"), ("Miércoles", "13:00", "15:00")],
    2: [("Jueves", "9:00", "11:00"), ("Viernes", "15:00", "17:00")],
    3: [("Martes", "10:00", "12:00"), ("Jueves", "14:00", "16:00")],
    4: [("Miércoles", "10:00", "12:00"), ("Viernes", "9:00", "11:00")]
}

# Datos de los docentes
DOCENTES = [
    {"id": 0, "nombre": "Juan", "apellidos": "Perez", "cantidadHoras": 10, "tiemporefrigerio": "30 min"},
    {"id": 1, "nombre": "Ana", "apellidos": "Gomez", "cantidadHoras": 8, "tiemporefrigerio": "30 min"},
    {"id": 2, "nombre": "Luis", "apellidos": "Martinez", "cantidadHoras": 12, "tiemporefrigerio": "30 min"},
    {"id": 3, "nombre": "Maria", "apellidos": "Lopez", "cantidadHoras": 10, "tiemporefrigerio": "30 min"},
    {"id": 4, "nombre": "Carlos", "apellidos": "Diaz", "cantidadHoras": 15, "tiemporefrigerio": "30 min"}
]

# Datos de los ambientes
AMBIENTES = [
    {"id": 0, "nombre": "Aula 101", "aforo": 30},
    {"id": 1, "nombre": "Aula 102", "aforo": 25},
    {"id": 2, "nombre": "Laboratorio 201", "aforo": 20}
]

# Datos de los cursos
CURSOS = [
    {"id": 0, "nombre": "Matemáticas", "horas_teoria": 2, "horas_practica": 1, "ciclo": 1, "tipo_curso": 'P'},
    {"id": 1, "nombre": "Física", "horas_teoria": 3, "horas_practica": 1, "ciclo": 1, "tipo_curso": 'P'},
    {"id": 2, "nombre": "Química", "horas_teoria": 2, "horas_practica": 2, "ciclo": 1, "tipo_curso": 'P'},
    {"id": 3, "nombre": "Biología", "horas_teoria": 1, "horas_practica": 2, "ciclo": 2, "tipo_curso": 'P'},
    {"id": 4, "nombre": "Historia", "horas_teoria": 3, "horas_practica": 0, "ciclo": 2, "tipo_curso": 'P'},
    {"id": 5, "nombre": "Geografía", "horas_teoria": 2, "horas_practica": 1, "ciclo": 2, "tipo_curso": 'P'},
    {"id": 6, "nombre": "Literatura", "horas_teoria": 2, "horas_practica": 1, "ciclo": 3, "tipo_curso": 'P'},
    {"id": 7, "nombre": "Inglés", "horas_teoria": 1, "horas_practica": 2, "ciclo": 3, "tipo_curso": 'P'},
    {"id": 8, "nombre": "Filosofía", "horas_teoria": 2, "horas_practica": 1, "ciclo": 3, "tipo_curso": 'P'},
    {"id": 9, "nombre": "Computación", "horas_teoria": 1, "horas_practica": 3, "ciclo": 3, "tipo_curso": 'P'}
]

# Datos de los grupos de horario
GRUPOS_HORARIO = [
    {"id": 0, "nombre": "Grupo A", "vacantes": 25, "idcurso": 0},
    {"id": 1, "nombre": "Grupo B", "vacantes": 20, "idcurso": 1},
    {"id": 2, "nombre": "Grupo C", "vacantes": 30, "idcurso": 2},
    {"id": 3, "nombre": "Grupo D", "vacantes": 20, "idcurso": 3},
    {"id": 4, "nombre": "Grupo E", "vacantes": 15, "idcurso": 4},
    {"id": 5, "nombre": "Grupo F", "vacantes": 25, "idcurso": 5},
    {"id": 6, "nombre": "Grupo G", "vacantes": 20, "idcurso": 6},
    {"id": 7, "nombre": "Grupo H", "vacantes": 20, "idcurso": 7},
    {"id": 8, "nombre": "Grupo I", "vacantes": 25, "idcurso": 8},
    {"id": 9, "nombre": "Grupo J", "vacantes": 30, "idcurso": 9}
]

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
                if len(horas_ocupadas[profesor]) != CURSOS[curso]["horas_teoria"] + CURSOS[curso]["horas_practica"]:
                    fitness -= 1
    
    return fitness

def obtener_horas_disponibles(profesor, dia):
    for d, hora_inicio, hora_fin in DISPONIBILIDAD_DOCENTES.get(profesor, []):
        if d == dia:
            return [f"{h}:00" for h in range(int(hora_inicio.split(':')[0]), int(hora_fin.split(':')[0]))]
    return []

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
            nombre_docente = DOCENTES[profesor]["nombre"]
            apellidos_docente = DOCENTES[profesor]["apellidos"]
            nombre_aula = AMBIENTES[aula]["nombre"]
            print(f"Profesor {nombre_docente} {apellidos_docente} - Curso: {nombre_curso} - Aula: {nombre_aula} - Día: {dia} - Hora: {hora}")

# Ejecutar el algoritmo genético
algoritmo_genetico()

