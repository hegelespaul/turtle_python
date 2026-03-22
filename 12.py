import turtle

# ---------------------------------------
# FUNCIÓN: L-SYSTEM (simplificado)
# ---------------------------------------
def create_system(axiom, pen, distance, angle, iterations):

    string = axiom

    # ---------------------------------------
    # 1. GENERACIÓN DE CADENA
    # ---------------------------------------
    for _ in range(iterations):
        new_string = ""
        for letter in string:

            if letter == 'F':
                new_string += 'F-F+B'
            if letter == 'B':
                new_string += 'F+B+F'
            else:
                # regla por defecto
                new_string += letter + '-B+F+'

        string = new_string

    print(string)

    # ---------------------------------------
    # 2. DIBUJO
    # ---------------------------------------
    for letter in string:

        if letter == 'F':
            pen.forward(distance)

        elif letter == 'B':
            pen.backward(distance)

        elif letter == '+':
            pen.right(angle)

        elif letter == '-':
            pen.left(angle)

# ---------------------------------------
# SETUP
# ---------------------------------------
screen = turtle.Screen()
screen.setup(1920, 1080)
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.pencolor("white")

screen.tracer(1000)

# Posición inicial
pen.penup()
pen.goto(800, 0)
pen.pendown()

# ---------------------------------------
# EJECUCIÓN
# ---------------------------------------
create_system("F", pen, 5, 99, 7)

screen.mainloop()