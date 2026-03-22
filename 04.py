import turtle
import random

# ---------------------------------------
# Configuración de pantalla
# ---------------------------------------
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")

# Desactiva la animación
turtle.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)

# ---------------------------------------
# Parámetros
# ---------------------------------------
radio = 30
pasos = 2000

x, y = 0, 0

for _ in range(pasos):

    t.width(random.uniform(0.1, 2))

    t.penup()
    t.goto(x, y)

    angulo = random.uniform(0, 360)
    t.setheading(angulo)

    t.pendown()
    t.forward(radio)

    x, y = t.position()

    t.penup()
    t.goto(x, y - radio)
    t.setheading(0)
    t.pendown()
    t.circle(radio)

t.hideturtle()

# Renderiza todo de una vez
turtle.update()

turtle.mainloop()
