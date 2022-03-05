import pygame, sys

# settings 
main_window_size= 800
square_size = int(main_window_size * 0.0375)
grid_thickeness = 1
stroke_thickeness = 4

#colors:
background_color = (215,238,245)
game_space_color = (255,255,255)
stroke_color = (255,0,0)
hold_space_color = (255,255,255)
score_background_color = (255,255,255)
next_piece_space_color = (255,255,255)
grid_color = (230,230,230)

#main window
window = pygame.display.set_mode((main_window_size,main_window_size))

#test element 
from classes import AI 
ai = AI()

# spaceholders 
play_space=pygame.Rect(int(main_window_size*0.625/2),int(main_window_size*0.25/2),10*square_size,20*square_size)
stroke_space = pygame.Rect(int(main_window_size*0.625/2)-stroke_thickeness,int(main_window_size*0.25/2)-stroke_thickeness,10*square_size+2*stroke_thickeness,20*square_size+2*stroke_thickeness)
hold_space = pygame.Rect(main_window_size//16,main_window_size//8,int(main_window_size*0.1875),main_window_size//4)
score_space = pygame.Rect(int(main_window_size*0.375),int(main_window_size*0.025),int(main_window_size*0.25),int(main_window_size*0.075)) 
next_piece_space = pygame.Rect(int(main_window_size*0.75),int(main_window_size*0.25/2),int(main_window_size*0.1875),main_window_size//4) 

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

        # game update
        if event.type == SCREEN_UPDATE and not ai.game.game_over: 
            ai.update()

        # user input
        """if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                ai.game.rotate()
            if event.key == K_DOWN:
                ai.game.move_down()
            if event.key == K_LEFT:
                ai.game.move_left()
            if event.key == K_RIGHT:
                ai.game.move_right()
            if event.key == K_SPACE:
                ai.game.bring_down()
            if event.key == K_RSHIFT:
                ai.game.hold()"""
        

    # main window filling 
    window.fill((0,0,0))

    # drawing the game
    ai.game.draw_game()

    # update & update frequency
    pygame.display.update()
    clock.tick(30)