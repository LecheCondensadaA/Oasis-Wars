import pygame
#ctrl+c, ctrl+v en Lore, Menu, victoria y derrota (si usamos el mismo codigo en las 4 pantallas jsjsjs)
def Instrucciones(ventana):
    ventana.blit(pygame.image.load("Imagenes/Instrucciones.png"), [0, 0])
    pygame.display.flip()

    Funcionando = True
    while Funcionando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Funcionando = False
            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                if tecla_presionada == "space":
                    from Pantalla_Menu import Menu_Principal
                    Menu_Principal(ventana)
    pygame.quit()