import turtle
import math

screen = turtle.Screen()
screen.setup(720, 600)
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)

t.width(2)

# -------- X Axis --------
t.penup()
t.color("white")
for x in range(-360, 360):
    y= 0
    t.goto(x, y)
    t.pendown()    

# -------- SENO (rojo) --------
t.color("red")
t.penup()

for x in range(-360, 360):
    y = 100 * math.sin(x * 0.02)
    t.goto(x, y)
    t.pendown()

# -------- COSENO (azul) --------
t.penup()
t.color("cyan")

for x in range(-360, 360):
    y = 100 * math.cos(x * 0.02)
    t.goto(x, y)  # desplazado hacia abajo
    t.pendown()

t.hideturtle()

turtle.update()
turtle.mainloop()