import pygame, sys


#main window
window = pygame.display.set_mode((400,400))

# spaceholders 
play_space=pygame.Rect(125,50,150,300)
hold_space = pygame.Rect(50,50,50,50)
score_space = pygame.Rect(150,10,100,30) 
next_piece_space = pygame.Rect(300,50,50,50) 

# clock
clock = pygame.time.Clock()

# screen update timer
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,500)

#game loop
while True: 

    for event in pygame.event.get():
        # close event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # main window filling 
    window.fill((94,219,167))

    # drawing surfaces
    pygame.draw.rect(window,(0,0,0),play_space)
    pygame.draw.rect(window,(0,0,0),hold_space)
    pygame.draw.rect(window,(0,0,0),score_space)
    pygame.draw.rect(window,(0,0,0),next_piece_space)

    # update & update frequency
    pygame.display.update()
    clock.tick(30)