import pandas as pd
import random

# Crear los DataFrames manualmente
data_docentes = {
    'idpersona': [4, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'nombres': ['Ernesto Ludwin', 'Marcos Oswaldo', 'Mariana', 'Miguel Orlando', 'Roger Ernesto', 'Luis Augusto', 'Maria Ysabel', 'Gregorio Manuel', 'Ricardo David', 'Karla Cecilia'],
    'apellidos': ['Nicho Cordova', 'Arnao Vasquez', 'Chavarry Chankay', 'Diaz Vidarte', 'Alarcon Garcia', 'Zuñe Bispo', 'Aranguri Garcia', 'Leon Tenorio', 'Iman Espinoza', 'Reyes Burgos'],
    'cantHoras': [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'tiempo_ref': [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

data_cursos = {
    'idcurso': list(range(1, 36)),
    'nombre': [
        'COMPRENSIÓN DE TEXTOS', 'DESARROLLO DE COMPETENCIAS', 'ESTRATEGIAS PARA EL APRENDIZAJE', 'INTRODUCCIÓN A LA INGENIERÍA',
        'MATEMÁTICA BÁSICA', 'MATEMÁTICA DISCRETA', 'CÁLCULO DE UNA VARIABLE', 'COMPRENSIÓN Y REDACCIÓN DE TEXTOS',
        'ECOLOGÍA Y DESARROLLO', 'ECONOMÍA Y REALIDAD NACIONAL', 'FUNDAMENTOS DE PROGRAMACIÓN', 'TEORÍA Y PROCESOS ORGANIZACIONALES',
        'ANÁLISIS Y ESPECIFICACIÓN DE REQUISITOS', 'CÁLCULO DE VARIAS VARIABLES', 'CONTABILIDAD Y FINANZAS', 'FILOSOFÍA',
        'FÍSICA DE LOS CUERPOS RÍGIDOS', 'METODOLOGÍAS DE PROGRAMACIÓN', 'ANTROPOLOGÍA FILOSÓFICA', 'BASE DE DATOS',
        'DISEÑO DE SOFTWARE', 'ECUACIONES DIFERENCIALES', 'ELECTRICIDAD Y MAGNETISMO', 'ESTRUCTURA DE DATOS Y ALGORITMOS',
        'ADMINISTRACIÓN DE BASES DE DATOS', 'ARQUITECTURA Y ORGANIZACIÓN DE COMPUTADORAS', 'DISEÑO WEB', 'ESTADÍSTICA Y PROBABILIDAD',
        'ÉTICA', 'INGENIERÍA DE PROCESOS', 'TEORÍA GENERAL DE SISTEMAS', 'CURSO ADICIONAL 1', 'CURSO ADICIONAL 2', 'CURSO ADICIONAL 3', 'CURSO ADICIONAL 4'
    ],
    'horas_teoria': [1, 1, 1, 2, 1, 3, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 3, 1, 1, 2, 1, 2, 3, 2, 2, 1, 1, 1, 2, 2, 1, 1],
    'horas_practica': [4, 2, 4, 4, 4, 2, 4, 4, 4, 4, 4, 2, 4, 4, 2, 4, 2, 4, 4, 4, 2, 4, 4, 4, 2, 4, 4, 2, 0, 4, 2, 2, 2, 1, 1],
    'tipo_curso': [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
}

data_ambientes = {
    'idambiente': list(range(1, 33)),
    'nombre': [
        'LABORATORIO-CLÍNICO 1 - CEFO', 'LABORATORIO-CLÍNICO 2 - CEFO', 'LABORATORIO-CLÍNICO 3 - CEFO', 'LABORATORIO-CLÍNICO 4 - CEFO',
        'LABORATORIO-CLÍNICO 5 - CEFO', 'LABORATORIO-ODONTOLÓGICO 1', 'LABORATORIO-ODONTOLÓGICO 2', 'AULA-03', 'AULA-04', 'AULA-DE MÚSICA 1',
        'LABORATORIO-DE FÍSICA', 'LABORATORIO-DE GEOTECNIA, CAMINOS Y ENSAYOS', 'LABORATORIO-DE HIDRÁULICA', 'LABORATORIO-DE INGENIERÍA SANITARIA Y AMBIENTAL',
        'LABORATORIO-DE MATERIALES', 'LABORATORIO-DE MATERIALES 2 (EX DECANA 5)', 'LABORATORIO-DE MECÁNICA DE FLUIDOS E INGENIERÍA DE MATERIALES',
        'LABORATORIO-DE MEDIOS AUDIOVISUALES', 'LABORATORIO-DE PRODUCCIÓN AUDIOVISUAL', 'LABORATORIO-DE PSICOLOGÍA', 'TALLER-AULA DE DISEÑO DE PINTURA Y ESCULTURA',
        'TALLER-DE DANZAS', 'TALLER-DE GASTRONOMÍA', 'TALLER-SALA DE FOTOGRAFÍA', 'TALLER-SALA DE LITIGACIÓN', 'AULA-101', 'AULA-104', 'AULA-109-A',
        'AULA-109-B', 'AULA-110', 'AULA-112', 'AULA-112-A'
    ],
    'aforo': [28, 28, 28, 28, 28, 21, 21, 40, 40, 12, 38, 45, 46, 35, 25, 50, 50, 27, 25, 12, 30, 12, 39, 40, 12, 56, 56, 44, 44, 39, 40, 44]
}

data_grupos = {
    'id_grupo': list(range(1, 36)),
    'nombre': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A'],
    'vacantes': [10, 15, 15, 15, 15, 15, 15, 15, 15, 15, 10, 15, 10, 15, 15, 15, 15, 15, 10, 15, 15, 15, 15, 15, 15, 15, 10, 15, 15, 15, 10, 15, 10, 15, 10],
    'idcurso': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

docentes_df = pd.DataFrame(data_docentes)
cursos_df = pd.DataFrame(data_cursos)
ambientes_df = pd.DataFrame(data_ambientes)
grupos_df = pd.DataFrame(data_grupos)

# Datos de entrada
profesores = docentes_df['nombres'].tolist()
tiempo_refrigerio = dict(zip(docentes_df['nombres'], docentes_df['tiempo_ref']))
cursos = cursos_df['nombre'].tolist()
horas_teoria = dict(zip(cursos_df['nombre'], cursos_df['horas_teoria']))
horas_practica = dict(zip(cursos_df['nombre'], cursos_df['horas_practica']))
tipo_curso = dict(zip(cursos_df['nombre'], cursos_df['tipo_curso']))
ambientes = ambientes_df['nombre'].tolist()
grupos = grupos_df['nombre'].tolist()
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
horas = ['8-10', '10-12', '12-14', '14-16', '16-18']

# Parámetros del algoritmo genético
tamano_poblacion = 100
generaciones = 1000
prob_mutacion = 0.1

# Generar individuo (horario)
def generar_individuo():
    horario = {}
    for dia in dias:
        for hora in horas:
            for idx, row in grupos_df.iterrows():
                grupo = row['nombre']
                curso = cursos_df[cursos_df['idcurso'] == row['idcurso']]['nombre'].values[0]
                if tipo_curso[curso] == 0:  # Curso presencial
                    ambiente = random.choice(ambientes[:-1])  # Excluimos "Aula Virtual"
                else:  # Curso virtual
                    ambiente = 'Aula Virtual'
                profesor = random.choice(profesores)
                horario[(dia, hora, grupo)] = (profesor, curso, ambiente)
    return horario

# Evaluar aptitud (fitness) del individuo
def evaluar_aptitud(individuo):
    aptitud = 0
    horarios_profesores = {prof: [] for prof in profesores}
    horas_asignadas = {prof: 0 for prof in profesores}
    
    for (dia, hora, grupo), (profesor, curso, ambiente) in individuo.items():
        if profesor in horarios_profesores:
            horarios_profesores[profesor].append((dia, hora))
            horas_asignadas[profesor] += 1
    
    for profesor, horarios in horarios_profesores.items():
        if len(horarios) != len(set(horarios)):
            aptitud -= 1
    
    horarios_ambientes = {amb: [] for amb in ambientes if amb != 'Aula Virtual'}
    
    for (dia, hora, grupo), (profesor, curso, ambiente) in individuo.items():
        if ambiente != 'Aula Virtual':
            if ambiente in horarios_ambientes:
                horarios_ambientes[ambiente].append((dia, hora))
    
    for ambiente, horarios in horarios_ambientes.items():
        if len(horarios) != len(set(horarios)):
            aptitud -= 1
    
    horarios_grupos = {grupo: [] for grupo in grupos}
    
    for (dia, hora, grupo), (profesor, curso, ambiente) in individuo.items():
        if grupo in horarios_grupos:
            horarios_grupos[grupo].append((dia, hora))
    
    for grupo, horarios in horarios_grupos.items():
        if len(horarios) != len(set(horarios)):
            aptitud -= 1
    
    for profesor, tiempo_ref in tiempo_refrigerio.items():
        if tiempo_ref > 0:
            tiempo_libre = 0
            for (dia, hora, grupo), (prof, curso, amb) in individuo.items():
                if prof == profesor:
                    if tiempo_libre < tiempo_ref:
                        tiempo_libre = 0
                    else:
                        tiempo_libre += 1
            if tiempo_libre < tiempo_ref:
                aptitud -= 1
    
    return aptitud

# Selección por torneo
def seleccion(poblacion, k=3):
    seleccionados = random.sample(poblacion, k)
    seleccionados.sort(key=lambda ind: evaluar_aptitud(ind), reverse=True)
    return seleccionados[0]

# Cruce de dos individuos
def cruce(padre1, padre2):
    punto_cruce = random.randint(0, len(padre1))
    hijo1 = {}
    hijo2 = {}
    
    for i, key in enumerate(padre1.keys()):
        if i < punto_cruce:
            hijo1[key] = padre1[key]
            hijo2[key] = padre2[key]
        else:
            hijo1[key] = padre2[key]
            hijo2[key] = padre1[key]
    
    return hijo1, hijo2

# Mutación de un individuo
def mutacion(individuo):
    for _ in range(random.randint(1, 5)):  # número de mutaciones
        dia = random.choice(dias)
        hora = random.choice(horas)
        idx = random.choice(grupos_df.index)
        grupo = grupos_df.loc[idx, 'nombre']
        curso = cursos_df[cursos_df['idcurso'] == grupos_df.loc[idx, 'idcurso']]['nombre'].values[0]
        if tipo_curso[curso] == 0:
            ambiente = random.choice(ambientes[:-1])  # Excluimos "Aula Virtual"
        else:
            ambiente = 'Aula Virtual'
        profesor = random.choice(profesores)
        individuo[(dia, hora, grupo)] = (profesor, curso, ambiente)
    return individuo

# Inicializar población
poblacion = [generar_individuo() for _ in range(tamano_poblacion)]

# Evolución
for generacion in range(generaciones):
    nueva_poblacion = []
    for _ in range(tamano_poblacion // 2):
        padre1 = seleccion(poblacion)
        padre2 = seleccion(poblacion)
        hijo1, hijo2 = cruce(padre1, padre2)
        if random.random() < prob_mutacion:
            hijo1 = mutacion(hijo1)
        if random.random() < prob_mutacion:
            hijo2 = mutacion(hijo2)
        nueva_poblacion.extend([hijo1, hijo2])
    
    poblacion = nueva_poblacion

# Mejor individuo
mejor_individuo = max(poblacion, key=evaluar_aptitud)

# Mostrar el mejor horario
for dia in dias:
    for hora in horas:
        for grupo in grupos:
            if (dia, hora, grupo) in mejor_individuo:
                print(f"{dia} {hora} {grupo}: {mejor_individuo[(dia, hora, grupo)]}")
