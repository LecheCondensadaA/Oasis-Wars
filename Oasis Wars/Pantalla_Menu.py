import pygame
import sys

def Menu_Principal(ventana):
    ventana.blit(pygame.image.load("Imagenes/Menu_Principal.png"), [0, 0])
    pygame.display.set_caption("Oasis Wars")
    pygame.display.flip()
#funcion donde detecta los cuadrados interactivos para seleccionar en el menu... en pocas palabras, la funcion del menu XD
    Funcionando = True
    while Funcionando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Funcionando = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if 210 <= mouse_x <= 210 + 250 and \
                       640 <= mouse_y <= 640 + 50:
                        from Pantalla_Lore import Lore
                        Lore(ventana)

                    if 540 <= mouse_x <= 540 + 250 and \
                       640 <= mouse_y <= 640 + 50:
                        from Pantalla_Instrucciones import Instrucciones
                        Instrucciones(ventana)

                    if 930 <= mouse_x <= 930 + 100 and \
                       640 <= mouse_y <= 640 + 50:
                        sys.exit()

            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                if tecla_presionada == "space":
                    print("alusen al sent") #easter egg que quisimos añadir (ademas chiste interno de la seccion 2 xd)
    pygame.quit()