import pygame
import funcionesjuego
import random

pygame.init()

#Resolucion
ancho_ventana = 1280
alto_ventana = 720

#imagenes... sprites
imagen_agua = pygame.image.load("Imagenes/agua.png")

#crea la ventana
ventana = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Imagenes/Oasis Wars")

#lista y los oasis aleatorios
agua_izquierda = []
agua_derecha = []
funcionesjuego.generar_oasis_aleatorios(agua_izquierda, agua_derecha)

#listas de celdas impactadas y oasis destruidos
celdas_impactadas_enemigo = []
oasis_destruidos_enemigo = []
celdas_fallidas_enemigo = []

celdas_impactadas_jugador = []
oasis_destruidos_jugador = []
celdas_fallidas_jugador = []

#para que funcione la mira
class mira(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Imagenes/mira.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocidad = 40

    def mover(self, dx, dy, limites):
        nuevo_x = self.rect.x + dx * self.velocidad
        nuevo_y = self.rect.y + dy * self.velocidad
        
        if limites.left <= nuevo_x < limites.right and limites.top <= nuevo_y < limites.bottom:
            self.rect.x = nuevo_x
            self.rect.y = nuevo_y

    def reset_posicion(self, x, y):
        self.rect.topleft = (x, y)

# sprite de la mira y sus movimientos con flechas
mira = mira(20, 60)
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(mira)

#limites del tablero
limites_tablero_jugador = pygame.Rect(20, 60, 600, 600)

#disparo del bot (que dispara de forma aleatoria)
def disparo_bot():
    while True:
        x_grid = random.randint(0, 15 - 1)
        y_grid = random.randint(0, 15 - 1)
        if (y_grid, x_grid) not in celdas_impactadas_jugador and (y_grid, x_grid) not in celdas_fallidas_jugador:
            impactado = funcionesjuego.disparar(x_grid, y_grid, agua_izquierda, celdas_impactadas_jugador, oasis_destruidos_jugador)
            if not impactado:
                celdas_fallidas_jugador.append((y_grid, x_grid))
            break

# Función principal de OASIS!!!
def juego():
    corriendo = True
    turno_jugador = True
    pygame.display.set_caption("Oasis Wars")
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN and turno_jugador:
                if evento.key == pygame.K_w:
                    mira.mover(0, -1, limites_tablero_jugador)
                if evento.key == pygame.K_s:
                    mira.mover(0, 1, limites_tablero_jugador)
                if evento.key == pygame.K_a:
                    mira.mover(-1, 0, limites_tablero_jugador)
                if evento.key == pygame.K_d:
                    mira.mover(1, 0, limites_tablero_jugador)
                if evento.key == pygame.K_SPACE:
                    x_grid = (mira.rect.x - 20) // 40
                    y_grid = (mira.rect.y - 60) // 40
                    if 0 <= x_grid < 15 and 0 <= y_grid < 15:
                        impactado = funcionesjuego.disparar(x_grid, y_grid, agua_derecha, celdas_impactadas_enemigo, oasis_destruidos_enemigo)
                        if not impactado:
                            celdas_fallidas_enemigo.append((y_grid, x_grid))
                        turno_jugador = False
                    mira.reset_posicion(20, 60)
        

        #En el turno del bot
        if not turno_jugador:
            disparo_bot()
            turno_jugador = True

        # Verifica si el juego ha terminado
        if len(oasis_destruidos_enemigo) == len(agua_derecha):
            from Pantalla_Victoria import Victoria
            Victoria(ventana)
            corriendo=True
        if len(oasis_destruidos_jugador) == len(agua_izquierda):
            from Pantalla_Derrota import Derrota
            Derrota(ventana)
            corriendo = True

        #blit de fondo
        ventana.blit(pygame.image.load("Imagenes/fondo.png"), [0, 0])

        #dibuja el tablero con los OASISSSS
        funcionesjuego.centrar_juego(ventana, agua_izquierda, agua_derecha, imagen_agua, ancho_ventana, alto_ventana, celdas_impactadas_enemigo, oasis_destruidos_enemigo, celdas_fallidas_enemigo, celdas_impactadas_jugador)

        #sprite de mira
        todos_los_sprites.draw(ventana)
        pygame.display.flip()

    pygame.quit()

juego()