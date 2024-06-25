import nltk
from nltk.chat.util import Chat, reflections

# Reflections y pairs de tu chatbot
reflections = {
  "ir": "fui",
  "hola": "holas",
  "local": "localidad"
}

pairs = [
    [
        r"se pone lento(.*)|el sistema esta lento(.*)",
        ["Lamentamos este inconveniente, por favor intenta reiniciar la aplicación y si el problema persiste, contacta al soporte técnico."]
    ],
    [
        r"(.*)fechas de pago(.*)",
        ["Las fechas de pago no están relacionadas con nuestro sistema de generación de horarios. Por favor, contacta a administración para más detalles."]
    ],
    [
        r"hola|hey|buenas",
        ["Hola, ¿cómo puedo ayudarte?"]
    ],
    [
        r"lo siento(.*)",
        ["No hay problema, soy un chatbot en proceso de aprendizaje. Por favor, vuelve a preguntar lo que necesitas."]
    ],
    [
        r"soy(.*)|mi nombre es (.*)",
        ["Un gusto conocerte %1, ¿cómo puedo asistirte en la generación de horarios?"]
    ],
    [
        r"tengo un problema con(.*)",
        ["Lamentamos los inconvenientes que estás teniendo con %1. ¿Podrías especificar más detalles del problema?"]
    ],
    [
        r"no puedo generar el horario(.*)|no puedo crear el horario(.*)|no puedo hacer el horario(.*)",
        ["Lamentamos este inconveniente. Por favor, asegúrate de haber seguido todos los pasos necesarios. Si el problema persiste, contacta al soporte técnico."]
    ],
    [
        r"necesito un nuevo servicio|(.*)nuevo servicio(.*)",
        ["Nuestro sistema se especializa en la generación de horarios de docentes. Si necesitas asistencia específica, contacta al soporte técnico."]
    ],
    [
        r"(.*)exportar datos(.*)",
        ["Para exportar datos, dirígete a la sección de 'Exportación' en el menú principal y sigue las instrucciones proporcionadas."]
    ],
    [
        r"(.*)(local|ciudad|lugar)(.*)?",
        ['Nuestro sistema es totalmente online y no requiere un local físico. Puedes acceder a él desde cualquier lugar con conexión a internet.']
    ],
    [
        r"(.*)tu nombre(.*)",
        ["Soy el asistente del sistema de generación de horarios. ¿En qué puedo ayudarte hoy?"]
    ],
    [
        r"adios",
        ["Adiós, cuídate. Nos vemos pronto :)", "Fue un placer ayudarte. Hasta luego :)"]
    ],
]
# Función para obtener respuesta del chatbot NLTK
def obtener_respuesta_nltk(peticion):
    chat = Chat(pairs, reflections)
    return chat.respond(peticion)
