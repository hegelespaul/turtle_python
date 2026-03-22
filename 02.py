import turtle

# Configuración de pantalla
screen = turtle.Screen()
screen.bgcolor("black")

# ---- Crear tortugas (pinceles independientes) ----
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

tortugas = [t1, t2, t3]

for t in tortugas:
    t.speed(0)

# ---------- Ejemplo 1: Mandala relleno (Tortuga 1) ----------
t1.penup()
t1.goto(-100, 120)
t1.pendown()
t1.width(2)

colors1 = ["red", "orange", "yellow"]

for i in range(18):
    t1.pencolor(colors1[i % 3])
    t1.fillcolor(colors1[(i + 1) % 3])
    t1.begin_fill()
    t1.circle(10)
    t1.end_fill()
    t1.left(20)

# ---------- Ejemplo 2: Estrella gruesa (Tortuga 2) ----------
t2.penup()
t2.goto(0, 120)
t2.pendown()
t2.width(4)

colors2 = ["cyan", "blue", "purple"]

for i in range(20):
    t2.pencolor(colors2[i % 3])
    for _ in range(5):
        t2.forward(30)
        t2.right(144)
    t2.right(18)

# ---------- Ejemplo 3: Roseta doble (Tortuga 3) ----------
t3.penup()
t3.goto(130, 120)
t3.pendown()
t3.width(2)

colors3 = ["lime", "green", "white"]

for i in range(36):
    t3.pencolor(colors3[i % 3])
    t3.forward(40)
    t3.backward(40)
    t3.right(10)

# ---------- Ejemplo 4: Flor coordinada (Tortuga 1 + 2) ----------
t1.penup()
t1.goto(-100, -80)
t1.setheading(0)
t1.pendown()

t2.penup()
t2.goto(-100, -80)
t2.setheading(180)
t2.pendown()

for i in range(12):
    t1.pencolor("magenta")
    t2.pencolor("white")
    
    t1.circle(25, 30)
    t2.circle(40, 30)
    
    t1.left(30)
    t2.right(60)

# ---------- Ejemplo 5: Espiral rellena (Tortuga 3) ----------
t3.penup()
t3.goto(80, -100)
t3.setheading(0)
t3.pendown()

for i in range(28):
    t3.pencolor("yellow")
    t3.fillcolor("orange")
    t3.begin_fill()
    t3.circle(i * 2)
    t3.end_fill()
    t3.left(15)

# Ocultar tortugas
for t in tortugas:
    t.hideturtle()

screen.mainloop()
