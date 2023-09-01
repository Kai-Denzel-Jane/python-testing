import colorama
import pygame


pygame.init()

window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Pygame Tests")



running = True


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    pygame.display.flip()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()

    pygame.draw.rect(window, (255, 0, 0), (0, 0, 50, 50))
    

