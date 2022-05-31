import pygame

pygame.init()

janela = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption("o jogo lá da minhoca")
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
quit()
