import pygame, sys


# settings 
main_window_width = 400
main_window_height = 400
square_size = int(main_window_width * 0.0375)

#colors:
background_color = (94,219,167)
game_space_color = (255,255,255)
hold_space_color = (255,255,255)
score_background_color = (255,255,255)
next_piece_space_color = (255,255,255)


#main window
window = pygame.display.set_mode((main_window_width,main_window_height))

#test element 
from classes import ELEMENT # placed after window to avoid the circular import error
element = ELEMENT()

# spaceholders 
play_space=pygame.Rect(int(main_window_width*0.625/2),int(main_window_height*0.25/2),int(main_window_width * 0.375),int(main_window_width*0.75))
hold_space = pygame.Rect(int(main_window_width*0.125),int(main_window_height*0.25/2),int(main_window_width*0.625/5),int(main_window_width*0.625/5))
score_space = pygame.Rect(int(main_window_width*0.375),int(main_window_height*0.025),int(main_window_width*0.25),int(main_window_height*0.075)) 
next_piece_space = pygame.Rect(int(main_window_width*0.75),int(main_window_height*0.25/2),int(main_window_width*0.625/5),int(main_window_width*0.625/5)) 

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
    window.fill(background_color)

    # drawing surfaces
    pygame.draw.rect(window,game_space_color,play_space)
    pygame.draw.rect(window,hold_space_color,hold_space)
    pygame.draw.rect(window,score_background_color,score_space)
    pygame.draw.rect(window,next_piece_space_color,next_piece_space)

    # drawing the element 
    element.draw_element()

    # update & update frequency
    pygame.display.update()
    clock.tick(30)