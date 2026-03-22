import turtle
import time
import random

# Dimensiones de la cuadrícula (número de celdas)
WIDTH = 20  
HEIGHT = 20

# Tamaño de cada celda en píxeles
CELL_SIZE = 20

# Crear la cuadrícula inicial con valores aleatorios (0 = muerto, 1 = vivo)
grid = [[random.choice([0, 1]) for _ in range(WIDTH)] for _ in range(HEIGHT)]
print(grid)

# Configuración de la ventana
screen = turtle.Screen()
screen.setup(WIDTH * CELL_SIZE + 20, HEIGHT * CELL_SIZE + 20)

# Desactiva la animación automática para controlar cuándo se dibuja
screen.tracer(0)

# Crear la tortuga que dibuja
t = turtle.Turtle()
t.hideturtle()  # Oculta el cursor
t.penup()       # Evita dibujar líneas al moverse


def draw_grid():
    """
    Dibuja la cuadrícula actual.
    Cada celda viva (1) se representa como un cuadrado negro.
    """
    t.clear()  # Borra el dibujo anterior

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x] == 1:  # Si la celda está viva
                # Posicionar la tortuga en la celda correspondiente
                t.goto(x * CELL_SIZE - WIDTH * CELL_SIZE / 2,
                       y * CELL_SIZE - HEIGHT * CELL_SIZE / 2)

                t.fillcolor('black')
                t.begin_fill()

                # Dibujar un cuadrado
                for _ in range(4):
                    t.forward(CELL_SIZE)
                    t.right(90)

                t.end_fill()

    screen.update()  # Actualiza la pantalla manualmente


def count_neighbors(x, y):
    """
    Cuenta cuántos vecinos vivos tiene una celda.
    Se consideran las 8 posiciones alrededor.
    """
    neighbors = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            # Evitar contar la propia celda
            if not (i == 0 and j == 0):
                nx, ny = x + i, y + j

                # Verificar que esté dentro de los límites
                if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                    neighbors += grid[ny][nx]

    return neighbors


def update_grid():
    """
    Calcula la siguiente generación de la cuadrícula
    según las reglas del Juego de la Vida.
    """
    global grid

    # Crear nueva cuadrícula vacía
    new_grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = count_neighbors(x, y)

            if grid[y][x] == 1:
                # Regla: sobrevive si tiene 2 o 3 vecinos
                if neighbors in [2, 3]:
                    new_grid[y][x] = 1
            else:
                # Regla: nace si tiene exactamente 3 vecinos
                if neighbors == 3:
                    new_grid[y][x] = 1

    # Actualizar la cuadrícula
    grid = new_grid


# Bucle principal de la simulación
while True:
    draw_grid()     # Dibujar estado actual
    update_grid()   # Calcular siguiente estado
    time.sleep(0.2) # Pausa para controlar velocidad