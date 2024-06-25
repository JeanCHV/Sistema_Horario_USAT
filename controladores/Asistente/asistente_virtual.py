from flask import jsonify
import re
respuestas_programadas = {
    "hola": "¡Hola! ¿En qué puedo ayudarte?",
    "cómo estás": "Estoy bien, gracias por preguntar.",
    "qué hora es": "Actualmente son las 10:00 AM.",
    # Agrega más respuestas programadas según necesites
}

def normalizar_texto(texto):
    # Convierte a minúsculas y elimina caracteres especiales
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto

def obtener_respuesta(peticion):
    peticion_normalizada = normalizar_texto(peticion)
    respuesta = respuestas_programadas.get(peticion_normalizada, "Lo siento, no entendí tu pregunta.")
    return jsonify({"respuesta": respuesta})
