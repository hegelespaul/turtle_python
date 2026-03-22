import turtle
import math

# ---------------------------------------
# Configuración de pantalla centrada
# ---------------------------------------
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.width(2)

# ---------------------------------------
# Parámetros principales
# ---------------------------------------
diametro = 160
radio = diametro / 2
lados = 80  # número de polígonos alrededor

centro = (0, 0)

# ---------------------------------------
# Círculo central
# ---------------------------------------
t.penup()
t.goto(0, -radio)
t.pendown()
t.circle(radio)

# ---------------------------------------
# Polígonos tangentes
# ---------------------------------------
angulo = 360 / lados
lado_poligono = diametro / 1.6

for i in range(lados):

    theta = math.radians(i * angulo)

    # punto tangente sobre la circunferencia
    x = radio * math.cos(theta)
    y = radio * math.sin(theta)

    t.penup()
    t.goto(x, y)
    t.setheading(i * angulo)
    t.pendown()

    # dibujar cuadrado tangente
    for _ in range(4):
        t.forward(lado_poligono)
        t.left(90)

t.hideturtle()
turtle.mainloop()
