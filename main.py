# PROYECTO TRIVIA
import random
import time

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

puntaje = random.randint(0, 11)
print(GREEN + "Bienvenido a mi TRIVIA")
print("Pondremos a prueba tus conocimientos")
nombre = input("Ingresa tu nombre: ")
print(
    "\n Hola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta: \n"
)
puntajeHistorial = []
listaHistorial = []
print("Tienes", puntaje, " puntos para iniciar." + RESET)
print("Iniciando trivia ...")
puntajeHistorial.append(puntaje)
listaHistorial.append("suerte")
for num_carga in range(5, 0, -1):
    print(num_carga)
    time.sleep(1)
print(" ")
intentos = 0
x = True
while x == True:
    print(GREEN + "1) ¿En qué año se descubrió américa?" + RESET)
    print("a. 2000")
    print("b. 1564")
    print("c. 1645")
    print("d. 1492")
    time.sleep(2)
    respuesta_1 = input("Ingrese la respuesta: ")
    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input(
            "Debes responder a, b, c, d. Ingrese nuevamente tu respuesta: ")

    if respuesta_1 == "d":
        print(BLUE + "Muy bien\n" + RESET)
        puntaje += 5
        puntajeHistorial.append(5)
        listaHistorial.append("Pregunta 1")
    else:
        print(RED + "Incorrecto\n" + RESET)
        puntaje -= 2
        puntajeHistorial.append(-2)
        listaHistorial.append("Pregunta 1")
    print(GREEN + "2) ¿Quién fue el primer Inca?" + RESET)
    print("a. Miguel Grau")
    print("b. Manco Cápac")
    print("c. José Olaya")
    print("d. Francisco Pizarro")
    time.sleep(2)
    respuesta_2 = input("Ingrese la respuesta: ")
    while respuesta_2 not in ("a", "b", "c", "d"):
        respuesta_2 = input(
            "Debes responder a, b, c, d. Ingrese nuevamente tu respuesta: ")
    if respuesta_2 == "b":
        print(BLUE + "Muy bien\n" + RESET)
        puntaje += 5
        puntajeHistorial.append(5)
        listaHistorial.append("Pregunta 2")
    else:
        print(RED + "Incorrecto\n" + RESET)
        puntaje -= 2
        puntajeHistorial.append(-2)
        listaHistorial.append("Pregunta 2")
    print(GREEN +
          "3) ¿Quién cantó por primera vez el Himno Nacional del Perú?" +
          RESET)
    print("a. Mark Zuckerberg")
    print("b. José de San Martín")
    print("c. Rosa Merino")
    print("d. Ollanta Humala")
    time.sleep(2)
    respuesta_3 = input("Ingrese la respuesta: ")
    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input(
            "Debes responder a, b, c, d. Ingrese nuevamente tu respuesta: ")
    if respuesta_3 == "c":
        print(BLUE + "Muy bien\n" + RESET)
        puntaje += 5
        puntajeHistorial.append(5)
        listaHistorial.append("Pregunta 3")
    else:
        print(RED + "Incorrecto\n" + RESET)
        puntaje -= 2
        puntajeHistorial.append(-2)
        listaHistorial.append("Pregunta 3")
    print(GREEN + "4) ¿Indique uno de los lenguajes de bajo nivel? \n" + RESET)
    print("a. Python")
    print("b. Java")
    print("c. PHP")
    print("d. Assembler\n")
    time.sleep(2)
    respuesta_4 = input("Ingrese la respuesta: ")
    while respuesta_4 not in ("a", "b", "c", "d"):
        respuesta_4 = input(
            "Debes responder a, b, c, d. Ingrese nuevamente tu respuesta: ")

    if respuesta_4 == "a":
        print(RED + "Incorrecto!", nombre,
              "Python es un lenguaje de alto nivel" + RESET)
        puntaje -= 2
        puntajeHistorial.append(-2)
        listaHistorial.append("Pregunta 4")
    elif respuesta_4 == "b":
        print(RED + "Incorrecto!", nombre,
              "Java es un lenguaje de alto nivel" + RESET)
        puntaje -= 2
        puntajeHistorial.append(-2)
        listaHistorial.append("Pregunta 4")
    elif respuesta_4 == "c":
        print(RED + "Incorrecto!", nombre,
              "PHP es un lenguaje de alto nivel" + RESET)
        puntaje -= 2
        puntajeHistorial.append(-2)
        listaHistorial.append("Pregunta 4")
    else:
        print(BLUE + "Muy bien", nombre, "!" + RESET)
        puntaje += 5
        puntajeHistorial.append(5)
        listaHistorial.append("Pregunta 4")
    if respuesta_1 == "d" and respuesta_2 == "b" and respuesta_3 == "c" and respuesta_4 == "d":
        print("Respondiste bien a todas las preguntas")
        repetir = input(
            "Escriba SI para realizar de nuevo, caso contrario presione cualquier tecla para cancelar: "
        ).upper()
        if repetir != "SI":
            print("Usted está finalizando la TRIVIA ...")
            time.sleep(3)
            x = False
    else:
        puntaje2 = random.randint(-20, 20)
        print(
            "¡TUVISTE ERRORES!, tienes que responder correctamente para finalizar la TRIVIA "
        )
        print("Probando suerte, para tu puntaje adicional...")
        time.sleep(2)
        print("Tienes", puntaje2, "puntos adicionales")
        input("Presiona Enter para continuar ...")
        puntajeHistorial.append(puntaje2)
        listaHistorial.append("suerte")
        puntaje += puntaje2
    intentos += 1

print(" ")
print("=========================== RESULTADOS =============================")
print("Gracias", nombre, " por jugar mi trivia, alcanzaste", puntaje,
      " puntos, en ", intentos, "intentos.")
print("HISTORIAL ")
for m in range(0, len(puntajeHistorial)):
    print("Se obtuvo: ", puntajeHistorial[m], " puntos por ",
          listaHistorial[m])
