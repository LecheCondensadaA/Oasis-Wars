import pygame
#ctrl+c, ctrl+v en Lore, Menu, victoria y derrota (si usamos el mismo codigo en las 4 pantallas jsjsjs)
def Lore(ventana):
    ventana.blit(pygame.image.load("Imagenes/Lore.png"), [0, 0])
    pygame.display.flip()

    Funcionando = True
    while Funcionando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Funcionando = False
            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                if tecla_presionada == "space":
                    from Juego import juego
                    juego(ventana)
    pygame.quit()