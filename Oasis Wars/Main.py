import pygame
import sys
from Pantalla_Menu import Menu_Principal

#define la funcion principal e.e
def main():
    pygame.init()
    Ventana = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Oasis Wars")
    Ventana.blit(pygame.image.load("Imagenes/Titulo.png"), [0, 0])
    pygame.display.flip() 
    pygame.time.Clock().tick(60)

    Funcionando = True
    while Funcionando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Funcionando = False
            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                if tecla_presionada == "space":
                    Menu_Principal(Ventana)

    pygame.quit()
    sys.exit()

main()
