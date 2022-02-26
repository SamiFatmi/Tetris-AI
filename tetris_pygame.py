import pygame, sys


window = pygame.display.set_mode((200,200))
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,500)


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    window.fill((94,219,167))

    pygame.display.update()
    clock.tick(30)