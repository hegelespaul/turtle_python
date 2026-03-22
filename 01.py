import turtle

# ---------------------------------------
# Configuración de pantalla
# ---------------------------------------
screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.width(3)

# ---------------------------------------
# 1. Línea recta (forward)
# ---------------------------------------
t.penup()
t.goto(-200, 0)
t.pendown()
t.forward(150)   # dibuja una línea

# ---------------------------------------
# 2. Giro y polígono (ángulo)
# ---------------------------------------
t.penup()
t.goto(0, 0)
t.pendown()

for _ in range(4):   # cuadrado
    t.forward(80)
    t.left(90)       # giro de 90 grados

# ---------------------------------------
# 3. Círculo
# ---------------------------------------
t.penup()
t.goto(200, -40)
t.pendown()
t.circle(40)         # radio del círculo

# ---------------------------------------
# Final
# ---------------------------------------
t.hideturtle()
turtle.mainloop()
