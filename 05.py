import turtle
import math
import random

# ---------------------------------------
# Configuración de pantalla
# ---------------------------------------
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.width(2)

# Dibujar sin animación
turtle.tracer(0, 0)

# ---------------------------------------
# Función distancia euclideana
# ---------------------------------------
def distancia(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# ---------------------------------------
# Parámetros globales
# ---------------------------------------
repeticiones = 12
segmentos = 6

# ---------------------------------------
# Loop principal
# ---------------------------------------
for _ in range(repeticiones):

    # Generar puntos aleatorios
    p1 = (random.randint(-300, 300), random.randint(-300, 300))
    p2 = (random.randint(-300, 300), random.randint(-300, 300))

    # Calcular distancia
    d_total = distancia(p1, p2)

    # Dibujar segmento base
    t.penup()
    t.goto(p1)
    t.pendown()
    t.goto(p2)

    # Subdividir segmento
    dx = (p2[0] - p1[0]) / segmentos
    dy = (p2[1] - p1[1]) / segmentos

    radio = d_total / (segmentos * 8)

    # Dibujar círculos en subdivisiones
    for i in range(segmentos + 1):

        x = p1[0] + dx * i
        y = p1[1] + dy * i

        t.penup()
        t.goto(x, y - radio)
        t.pendown()
        t.circle(radio)

t.hideturtle()

# Mostrar resultado final
turtle.update()
turtle.mainloop()
