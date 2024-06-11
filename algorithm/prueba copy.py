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

# Obtener datos de los controladores
DOCENTES = controlador_docente.get_docentes()
AMBIENTES = controlador_ambiente.get_ambientes()
CURSOS = controlador_cursos.get_cursos()
GRUPOS = controlador_grupo.get_grupo()
DISPONIBILIDAD_DOCENTES = controlador_docente_disponibilidad.get_disponibilidad()
CURSO_AMBIENTE = controlador_curso_ambiente.get_curso_ambiente()
CURSO_DOCENTE = controlador_curso_docente.get_curso_docente()

# Constantes
NUM_PROFESORES = len(DOCENTES)
NUM_CURSOS = len(CURSOS)
NUM_AULAS = len(AMBIENTES)
HORAS = [f"{h:02d}:00" for h in range(7, 23)]
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

# Función para generar una población inicial
def generar_poblacion(tamano):
    poblacion = []
    for _ in range(tamano):
        horario = []
        for curso in CURSOS:
            grupos_del_curso = [g for g in GRUPOS if g['idcurso'] == curso['idcurso']]
            for grupo in grupos_del_curso:
                docentes_del_curso = [cd['idpersona'] for cd in CURSO_DOCENTE if cd['idcurso'] == curso['idcurso']]
                if docentes_del_curso:
                    profesor = random.choice(docentes_del_curso)
                else:
                    profesor = random.randint(0, NUM_PROFESORES - 1)
                dia = random.choice(DIAS)
                hora_inicio = random.choice(HORAS)
                duracion = curso["horas_teoria"] + curso["horas_practica"]
                hora_fin_hora = int(hora_inicio.split(':')[0]) + duracion
                if hora_fin_hora > 22:
                    hora_fin_hora = 22
                hora_fin = f"{hora_fin_hora:02d}:00"
                ambiente = random.choice([ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == curso['idcurso']]) if any(ca['idcurso'] == curso['idcurso'] for ca in CURSO_AMBIENTE) else random.randint(0, NUM_AULAS - 1)
                horario.append((profesor, curso['idcurso'], ambiente, dia, hora_inicio, hora_fin, grupo['id_grupo']))
        poblacion.append(horario)
    return poblacion

# Función para calcular la aptitud (fitness) de un horario
def calcular_fitness(horario):
    fitness = 0
    profesor_horas = {profesor['idpersona']: 0 for profesor in DOCENTES}
    
    for dia in DIAS:
        horas_ocupadas = {profesor['idpersona']: [] for profesor in DOCENTES}
        for (profesor, curso, aula, d, hora_inicio, hora_fin, grupo) in horario:
            if d == dia:
                horas_ocupadas_total = next((c["horas_teoria"] + c["horas_practica"] for c in CURSOS if c['idcurso'] == curso), 0)
                
                horas_disponibles = obtener_horas_disponibles(profesor, d)
                if hora_inicio not in horas_disponibles or len(horas_ocupadas[profesor]) + horas_ocupadas_total > len(horas_disponibles):
                    fitness -= 1
                else:
                    if any(hora in horas_ocupadas[profesor] for hora in range(int(hora_inicio.split(':')[0]), int(hora_fin.split(':')[0]))):
                        fitness -= 1
                    else:
                        horas_ocupadas[profesor].extend(range(int(hora_inicio.split(':')[0]), int(hora_fin.split(':')[0])))
                        
                if profesor in profesor_horas:
                    profesor_horas[profesor] += horas_ocupadas_total

    for profesor, horas in profesor_horas.items():
        max_horas = next((d['cantHoras'] for d in DOCENTES if d['idpersona'] == profesor), None)
        if max_horas and horas > max_horas:
            fitness -= (horas - max_horas)
    
    return fitness

# Función para obtener las horas disponibles de un profesor en un día
def obtener_horas_disponibles(profesor, dia):
    horas_disponibles = []
    for disponibilidad in DISPONIBILIDAD_DOCENTES:
        if disponibilidad["idpersona"] == profesor and disponibilidad["dia"] == dia:
            hora_inicio = int(disponibilidad["hora_inicio"].split(':')[0])
            hora_fin = int(disponibilidad["hora_fin"].split(':')[0])
            horas_disponibles.extend([f"{h:02d}:00" for h in range(hora_inicio, hora_fin)])
    return horas_disponibles

# Función de selección
def seleccion(poblacion):
    poblacion = sorted(poblacion, key=lambda x: calcular_fitness(x), reverse=True)
    return poblacion[:5]

# Función de cruce
def cruce(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[:punto_cruce:]
    return hijo1, hijo2

# Función de mutación
def mutacion(individuo):
    if individuo:
        i = random.randint(0, len(individuo) - 1)
        curso = individuo[i][1]
        docentes_del_curso = [cd['idpersona'] for cd in CURSO_DOCENTE if cd['idcurso'] == curso]
        profesor = random.choice(docentes_del_curso) if docentes_del_curso else random.randint(0, NUM_PROFESORES - 1)
        dia = random.choice(DIAS)
        hora_inicio = random.choice(HORAS)
        duracion = next((c["horas_teoria"] + c["horas_practica"] for c in CURSOS if c['idcurso'] == curso), 0)
        hora_fin_hora = int(hora_inicio.split(':')[0]) + duracion
        if hora_fin_hora > 22:
            hora_fin_hora = 22
        hora_fin = f"{hora_fin_hora:02d}:00"
        ambiente = random.choice([ca['idambiente'] for ca in CURSO_AMBIENTE if ca['idcurso'] == curso]) if any(ca['idcurso'] == curso for ca in CURSO_AMBIENTE) else random.randint(0, NUM_AULAS - 1)
        grupo = individuo[i][6]
        individuo[i] = (profesor, curso, ambiente, dia, hora_inicio, hora_fin, grupo)

# Algoritmo genético
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
    
    mejores_individuos = sorted(poblacion, key=calcular_fitness, reverse=True)[:5]
    
    resultado = {
        "Generacion": 99,
        "Mejor_fitness": calcular_fitness(mejores_individuos[0]),
        "Horarios": []
    }
    
    for mejor_individuo in mejores_individuos:
        horario = []
        for (profesor, curso, aula, dia, hora_inicio, hora_fin, grupo) in mejor_individuo:
            nombre_docente = next((d["nombres"] for d in DOCENTES if d["idpersona"] == profesor), "Desconocido")
            apellidos_docente = next((d["apellidos"] for d in DOCENTES if d["idpersona"] == profesor), "")
            nombre_curso = next((c["nombre"] for c in CURSOS if c["idcurso"] == curso), "Desconocido")
            nombre_aula = next((a["nombre"] for a in AMBIENTES if a["idambiente"] == aula), "Aula desconocida")
            nombre_grupo = next((g["nombre"] for g in GRUPOS if g["id_grupo"] == grupo), "Grupo desconocido")
            
            horario.append({
                "Docente": f"{nombre_docente} {apellidos_docente}",
                "Curso": nombre_curso,
                "Aula": nombre_aula,
                "Dia": dia,
                "Hora_inicio": hora_inicio,
                "Hora_fin": hora_fin,
                "Grupo": nombre_grupo
            })
        resultado["Horarios"].append(horario)
    
    return resultado

# Ejecutar el algoritmo y obtener la mejor generación en formato JSON
mejor_horario = algoritmo_genetico()
print(json.dumps(mejor_horario, indent=4, ensure_ascii=False))
