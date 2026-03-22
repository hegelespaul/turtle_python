import turtle
import math  # Librería para funciones matemáticas (seno, coseno, etc.)

# Configuración de la ventana
screen = turtle.Screen()
screen.setup(800, 600)       
screen.bgcolor("black")      

# Crear la tortuga (cursor de dibujo)
t = turtle.Turtle()
t.speed(0)       
t.width(2)       
t.color("lime")  

t.penup()  

for x in range(-400, 400):

    # Cálculo de la posición en Y usando suma de funciones seno
    # Cada término tiene distinta frecuencia y amplitud:
    # - 80 * sin(x * 0.02) → onda principal (más suave)
    # - 40 * sin(x * 0.05) → variación intermedia
    # - 20 * sin(x * 0.1)  → detalle fino (alta frecuencia)
    y = (
        80 * math.sin(x * 0.02) +
        40 * math.sin(x * 0.05) +
        20 * math.sin(x * 0.1)
    )
    
    t.goto(x, y)

    t.pendown()

t.hideturtle()

turtle.mainloop()