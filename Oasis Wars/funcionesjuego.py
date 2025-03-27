import pygame
import random

#color negro
negro = (0, 0, 0)

#Imagenes
agua_destruida = pygame.image.load("Imagenes/agua_destruida.png")
agua_impactada = pygame.image.load("Imagenes/agua_impactada.png")
arena_impactada = pygame.image.load("Imagenes/arena_impactada.png")

#funcion para que el agua no se pueda superponer
def para_que_no_se_superponga_el_agua(agua_nueva, lista_agua):
    for agua in lista_agua:
        for parte_agua in agua:
            if parte_agua in agua_nueva:
                return True
    return False

#funcion que genera el agua/oasis aleatoriamente
def generar_oasis_aleatorios(agua_izquierda, agua_derecha):
    agua_izquierda.clear()
    agua_derecha.clear()

    #generar los oasis
    def generar_oasis(oasis, longitud, cantidad):
        for i in range(cantidad): #hace que de vueltas hasta que de vueltas hasta que se generen todos los oasis
            while True: 
                fila = random.randint(0, 15 - 1)
                columna = random.randint(0, 15 - longitud)
                agua = [(fila, columna + j) for j in range(longitud)]

                if not para_que_no_se_superponga_el_agua(agua, oasis):
                    oasis.append(agua)
                    break

    #3 osasis de 4 celdas
    generar_oasis(agua_izquierda, 4, 3)
    generar_oasis(agua_derecha, 4, 3)

    #5 oasis de 3 celdas
    generar_oasis(agua_izquierda, 3, 5)
    generar_oasis(agua_derecha, 3, 5)

    #4 oasis de 2 celdas
    generar_oasis(agua_izquierda, 2, 4)
    generar_oasis(agua_derecha, 2, 4)

#funcion que dibuja el tablero
def dibujar_tablero(ventana, x_offset, y_offset):
    for fila in range(15):
        for columna in range(15):
            rect = pygame.Rect(x_offset + columna * 40, y_offset + fila *40, 40, 40)
            pygame.draw.rect(ventana, negro, rect, 1)

#función para dibujar los oasis
def dibujar_oasis(ventana, x_offset, y_offset, lista_agua, imagen_OASIS, celdas_impactadas, oasis_destruidos, celdas_fallidas):
    for agua in lista_agua:
        if agua in oasis_destruidos:
            for parte_agua in agua:
                fila, columna = parte_agua
                x = x_offset + columna * 40
                y = y_offset + fila * 40
                ventana.blit(agua_destruida, (x, y))

        else:
            for parte_agua in agua:
                fila, columna = parte_agua
                rect = pygame.Rect(x_offset + columna * 40, y_offset + fila * 40, 40, 40)
                if (fila, columna) in celdas_impactadas:
                    ventana.blit(agua_impactada, rect.topleft)
                else:
                    ventana.blit(imagen_OASIS, rect.topleft)
#cuando fallas un disparo
    for celda in celdas_fallidas:
        fila, columna = celda
        x = x_offset + columna * 40
        y = y_offset + fila * 40
        ventana.blit(arena_impactada, (x, y))

# Función para centrar el juego en la ventana
def centrar_juego(ventana, agua_izquierda, agua_derecha, imagen_OASIS, celdas_impactadas_enemigo, oasis_destruidos_enemigo, celdas_fallidas_enemigo, celdas_impactadas_jugador, oasis_destruidos_jugador, celdas_fallidas_jugador):

    # Dibuja el tablero del bot
    dibujar_tablero(ventana, 660, 60)

    # Dibuja el tablero derecho
    dibujar_tablero(ventana, 20, 60)

    # Dibuja los oasis del bot
    dibujar_oasis(ventana, 660, 60, agua_izquierda, imagen_OASIS, celdas_impactadas_jugador, oasis_destruidos_jugador, celdas_fallidas_jugador)

    # Dibuja los oasis derechos
    dibujar_oasis(ventana, 20, 60, agua_derecha, imagen_OASIS, celdas_impactadas_enemigo, oasis_destruidos_enemigo, celdas_fallidas_enemigo)

# Función para disparar
def disparar(x_grid, y_grid, oasis_enemigos, celdas_impactadas, oasis_destruidos):
    for agua in oasis_enemigos:
        if (y_grid, x_grid) in agua:
            celdas_impactadas.append((y_grid, x_grid))
            # Verificar si el oasis está destruido
            if all(celda in celdas_impactadas for celda in agua):
                oasis_destruidos.append(agua)
            return True
    return False