import turtle
import math
import random

# ---------------------------------------
# Configuración
# ---------------------------------------
screen = turtle.Screen()
screen.setup(1000, 700)
screen.bgcolor("#0b0f1a")  # cielo oscuro

turtle.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)
t.width(2)

# ---------------------------------------
# Función de sistema (modulación de ondas)
# ---------------------------------------
def sistema(x, fase):

    base = 120 * math.sin(x * 0.003 + fase)

    detalle1 = 60 * math.sin(x * 0.01 + fase * 1.5)
    detalle2 = 30 * math.cos(x * 0.02 - fase * 0.8)

    textura = 15 * math.sin(x * 0.08 + math.sin(x * 0.01))

    distorsion = 10 * math.sin(x * 0.002 + base * 0.01)

    return base + detalle1 + detalle2 + textura + distorsion

# ---------------------------------------
# Dibujar múltiples capas
# ---------------------------------------
capas = 250

for capa in range(capas):

    t.penup()

    offset_y = 0 + capa/capas 
    fase = capa * 0.8

    # color degradado
    color = (
        0.1 + capa / capas * 0.4,  # rojo
        0.3 + capa / capas * 0.5,  # verde
        0.2 + capa / capas * 0.6   # azul
    )

    turtle.colormode(1.0)
    t.color(color)

    # inicio
    t.goto(-500, offset_y)
    t.pendown()

    for x in range(-500, 500):
        y = sistema(x, fase) + offset_y
        t.goto(x, y)

    # cerrar forma para relleno
    t.goto(500, -350)
    t.goto(-500, -350)
    t.goto(-500, sistema(-500, fase) + offset_y)

    t.begin_fill()
    t.end_fill()


# ---------------------------------------
# Render final
# ---------------------------------------
t.hideturtle()
turtle.update()
turtle.mainloop()