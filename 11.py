import turtle

# ---------------------------------------
# FUNCIÓN: GENERADOR DE FRACTAL (ÁRBOL)
# ---------------------------------------
def create_system(axiom, turtle_pen, distance, angle, iterations):

    # Regla de producción:
    # cada 'F' genera una estructura ramificada
    rules = {
        "F": "F[+F]F[-F]F"
    }

    # ---------------------------------------
    # 1. GENERACIÓN DE LA CADENA (REESCRITURA)
    # ---------------------------------------
    # Se parte del axioma inicial
    string = axiom

    # Se aplica la regla varias veces (crecimiento recursivo)
    for _ in range(iterations):
        new_string = ""
        for letter in string:
            # Sustituir según regla o mantener símbolo
            new_string += rules.get(letter, letter)
        string = new_string

    print(string)  # puede crecer exponencialmente

    # ---------------------------------------
    # 2. INTERPRETACIÓN (DIBUJO)
    # ---------------------------------------
    # Se usa una pila para manejar bifurcaciones
    stack = []

    for letter in string:

        if letter == "F":
            # avanzar (dibujar rama)
            turtle_pen.forward(distance)

        elif letter == "+":
            # girar a la derecha
            turtle_pen.right(angle)

        elif letter == "-":
            # girar a la izquierda
            turtle_pen.left(angle)

        elif letter == "[":
            # guardar estado actual (posición y dirección)
            position = turtle_pen.position()
            heading = turtle_pen.heading()
            stack.append((position, heading))

        elif letter == "]":
            # recuperar estado previo (volver a bifurcación)
            position, heading = stack.pop()
            turtle_pen.penup()
            turtle_pen.goto(position)
            turtle_pen.setheading(heading)
            turtle_pen.pendown()

# ---------------------------------------
# CONFIGURACIÓN DE PANTALLA
# ---------------------------------------
screen = turtle.Screen()
screen.setup(1920, 1080)

pen = turtle.Turtle()
pen.speed(0)  # velocidad máxima

# Acelerar render
screen.tracer(1000)

# Estética
screen.bgcolor('black')
pen.pencolor('white')

# Posición inicial (parte inferior, apuntando hacia arriba)
pen.up()
pen.goto(0, -500)
pen.left(90)
pen.down()

# ---------------------------------------
# EJECUCIÓN
# ---------------------------------------
# Genera un fractal tipo árbol con 6 iteraciones
create_system("F", pen, 1, 35, 6)

# Mantener ventana abierta
screen.mainloop()