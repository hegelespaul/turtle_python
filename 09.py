import numpy as np
import turtle

# ---------------------------------------
# Definición de estados y transiciones
# ---------------------------------------

# Estados posibles del sistema
states = ['A', 'B', 'C']

# Posibles transiciones (de un estado a otro)
# Ejemplo: 'AB' significa pasar de A → B
transitions = [
    ['AA', 'AB', 'AC'],  # desde A
    ['BA', 'BB', 'BC'],  # desde B
    ['CA', 'CB', 'CC']   # desde C
]

# Probabilidades asociadas a cada transición
# Cada fila corresponde a un estado actual
probabilities = [
    [0.33, 0.33, 0.34],  
    [0.33, 0.34, 0.33],    
    [0.34, 0.33, 0.33]   
]

# ---------------------------------------
# Función que genera la cadena de Markov
# ---------------------------------------
def trend(iteration):

    current = 'A'  # estado inicial
    secuencia = [current]  # lista donde guardamos la secuencia generada
    i = 0

    # Generar la cadena paso a paso
    while i < iteration:

        # Dependiendo del estado actual, se elige la transición
        # usando probabilidades
        if current == 'A':
            change = np.random.choice(transitions[0], p=probabilities[0])
        elif current == 'B':
            change = np.random.choice(transitions[1], p=probabilities[1])
        elif current == 'C':
            change = np.random.choice(transitions[2], p=probabilities[2])
        else:
            break

        # El nuevo estado es la segunda letra de la transición
        current = change[1]

        # Se guarda en la secuencia
        secuencia.append(current)

        i += 1

    return secuencia

# ---------------------------------------
# Configuración de pantalla
# ---------------------------------------
width = 1920
height = 1080

screen = turtle.Screen()
screen.setup(width, height)

# Quitar bordes de ventana (pantalla completa)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

# ---------------------------------------
# Loop principal de dibujo
# ---------------------------------------
for time in range(1000):

    # Generar una cadena larga de estados
    chain = trend(100000)
    print(chain)

    # Limpiar pantalla en cada iteración
    screen.clear()
    screen.tracer(10)  # controla velocidad de render
    screen.bgcolor('black')

    # Crear "pluma"
    pen = turtle.Turtle()
    pen.pencolor('white')
    pen.speed(10)

    # ---------------------------------------
    # Traducción de estados a movimiento
    # ---------------------------------------
    for letter in chain:

        if letter == 'A':
            # Giro a la izquierda y avanzar
            pen.left(90)
            pen.forward(5)

        elif letter == 'B':
            # Giro a la derecha y avanzar
            pen.right(90)
            pen.forward(5)

        elif letter == 'C':
            # Giro fuerte y retroceso
            pen.left(180)
            pen.backward(5)

# Mantener ventana abierta
turtle.mainloop()