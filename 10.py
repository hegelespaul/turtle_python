import turtle

# ---------------------------------------
# FUNCIÓN: GENERADOR DE FRACTAL (L-SYSTEM)
# ---------------------------------------
def create_system(axiom, turtle_pen, distance, angle, iterations):

    # Axioma: estado inicial (cadena base)
    string = axiom
    
    # ---------------------------------------
    # 1. GENERACIÓN DE LA CADENA (REESCRITURA)
    # ---------------------------------------
    # Se aplica la regla varias veces (iteraciones)
    for _ in range(iterations):
        new_string = ""
        for letter in string: 
            if letter == 'F':
                # Regla de producción:
                # cada F se sustituye por este patrón
                new_string += 'F-F++F-F'
            else:
                # otros símbolos se conservan
                new_string += letter
        
        # actualizar la cadena
        string = new_string
        
    print(string)  # puede ser muy larga
    
    # ---------------------------------------
    # 2. INTERPRETACIÓN (DIBUJO)
    # ---------------------------------------
    # Se traduce la cadena en movimientos de la tortuga
    for letter in string:
        if letter == 'F':
            # avanzar dibujando
            turtle_pen.forward(distance)
        elif letter == 'B':
            # retroceder (no se usa en este caso)
            turtle_pen.backward(distance)
        elif letter == '+':
            # girar a la derecha
            turtle_pen.right(angle)
        elif letter == '-':
            # girar a la izquierda
            turtle_pen.left(angle)

# ---------------------------------------
# CONFIGURACIÓN DE PANTALLA
# ---------------------------------------
screen = turtle.Screen()
screen.setup(1920,1080)

pen = turtle.Turtle()
pen.speed(0)  # velocidad máxima

# Acelerar render (menos animación)
screen.tracer(2)

# Estética
screen.bgcolor('black')
pen.pencolor('white')

# Posición inicial (lado izquierdo)
pen.up()
pen.goto(-1000,-200)
pen.down()

# ---------------------------------------
# EJECUCIÓN
# ---------------------------------------
# Genera un fractal geométrico con 7 iteraciones
create_system('F', pen, 1, 60, 7)

# Mantener ventana abierta
screen.mainloop()