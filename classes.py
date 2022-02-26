import pygame, random
from pygame.math import Vector2

class ELEMENT:
    """ Will contain element shapes and colors and functions for drawing the elements"""
    def __init__(self) -> None:
        self.position = (4,2)
        self.orientation = 1
        self.element_name = random.choice(["L","L2","I","O","S","Z","T"])
        self.body = self.element_body()
        self.color = self.element_color()

    def draw_element(self):
        from tetris_pygame import window # place here to avoid the circular import error 
        from tetris_pygame import square_size, main_window_size
        for element in self.body : 
            element_rect = pygame.Rect(int(main_window_size*0.625/2)+(self.position[0]+element[0])*square_size,int(main_window_size*0.25/2)+(self.position[1]+element[1])*square_size,square_size,square_size)
            pygame.draw.rect(window,self.color,element_rect)

    def element_body(self): #decide the element body depending on what element it is and what orientation it is 
        if self.element_name == "T":
            if self.orientation == 1 :
                self.body = [Vector2(1,0),Vector2(0,1),Vector2(1,1),Vector2(2,1)]
                self.body_size = Vector2(3,2)
            elif self.orientation == 2: 
                self.body = [Vector2(1,0),Vector2(1,1),Vector2(1,2),Vector2(2,1)]
                self.body_size = Vector2(2,3)
            elif self.orientation == 3 :
                self.body = [Vector2(0,0),Vector2(1,0),Vector2(2,0),Vector2(1,1)]
                self.body_size = Vector2(3,2)
            elif self.orientation == 4:
                self.body = [Vector2(0,1),Vector2(1,0),Vector2(1,1),Vector2(1,2)]
                self.body_size = Vector2(2,3)
        elif self.element_name == "S":
            if self.orientation in [1,3]  :
                self.body = [Vector2(1,0),Vector2(2,0),Vector2(0,1),Vector2(1,1)]
                self.body_size = Vector2(3,2)
            else : 
                self.body = [Vector2(0,0),Vector2(0,1),Vector2(1,1),Vector2(1,2)]
                self.body_size = Vector2(2,3)
        elif self.element_name == "Z": 
            if self.orientation in [1,3] :
                self.body = [Vector2(0,0),Vector2(1,0),Vector2(1,1),Vector2(2,1)]
                self.body_size = Vector2(3,2)
            else : 
                self.body = [Vector2(1,0),Vector2(1,1),Vector2(0,1),Vector2(0,2)]
                self.body_size = Vector2(2,3)
        elif self.element_name == "L":
            if self.orientation == 1 :
                self.body = [Vector2(0,0),Vector2(0,1),Vector2(0,2),Vector2(1,2)]
                self.body_size = Vector2(2,3)
            elif self.orientation == 2: 
                self.body = [Vector2(0,0),Vector2(1,0),Vector2(2,0),Vector2(0,1)]
                self.body_size = Vector2(3,2)
            elif self.orientation == 3 :
                self.body = [Vector2(0,0),Vector2(1,0),Vector2(1,1),Vector2(1,2)]
                self.body_size = Vector2(2,3)
            elif self.orientation == 4:
                self.body = [Vector2(2,0),Vector2(0,1),Vector2(1,1),Vector2(2,1)]
                self.body_size = Vector2(3,2)
        elif self.element_name == "L2":
            if self.orientation == 1 :
                self.body = [Vector2(0,2),Vector2(1,0),Vector2(1,1),Vector2(1,2)]
                self.body_size = Vector2(2,3)
            elif self.orientation == 2: 
                self.body = [Vector2(0,0),Vector2(0,1),Vector2(1,1),Vector2(2,1)]
                self.body_size = Vector2(3,2)
            elif self.orientation == 3 :
                self.body = [Vector2(0,0),Vector2(0,1),Vector2(0,2),Vector2(1,0)]
                self.body_size = Vector2(2,3)
            elif self.orientation == 4:
                self.body = [Vector2(0,0),Vector2(1,0),Vector2(2,0),Vector2(2,1)]
                self.body_size = Vector2(3,2)
        elif self.element_name == "O":
            self.body = [Vector2(0,0),Vector2(0,1),Vector2(1,0),Vector2(1,1)]
            self.body_size = Vector2(2,2)
        elif self.element_name == "I":
            if self.orientation in [1,3] :
                self.body = [Vector2(0,1),Vector2(0,2),Vector2(0,3),Vector2(0,0)]
                self.body_size = Vector2(4,1)
            else : 
                self.body = [Vector2(1,0),Vector2(2,0),Vector2(3,0),Vector2(0,0)]
                self.body_size = Vector2(1,4)
        return self.body

    def element_color(self): 
        if self.element_name == "T":
            self.color = (160,0,240)
        elif self.element_name == "S":
            self.color = (0,240,0)
        elif self.element_name == "Z": 
            self.color = (240,0,0)
        elif self.element_name == "L":
            self.color = (240,160,0)
        elif self.element_name == "L2":
            self.color = (0,0,240)
        elif self.element_name == "O":
            self.color = (240,240,0)
        elif self.element_name == "I":
            self.color = (140,145,145)
        return self.color



class GAME:
    """ Will contain Game details such as space and space, will also contain methods
        for moving the elements, holding an element, checking collisions and clearing lines """

    def __init__(self) -> None:
        self.current_element = ELEMENT()
        self.next_element = ELEMENT() 
        self.held_element = ELEMENT()
        self.space = [ [ (0,0,0) for _ in range(10)] for __ in range(20)]
        self.score = 0

    def draw_game(self):
        from tetris_pygame import main_window_size, square_size,window,grid_color,grid_thickeness,game_space_color,hold_space_color,score_background_color,next_piece_space_color,play_space,hold_space,score_space,next_piece_space

        # drawing surfaces
        pygame.draw.rect(window,game_space_color,play_space)
        pygame.draw.rect(window,hold_space_color,hold_space)
        pygame.draw.rect(window,score_background_color,score_space)
        pygame.draw.rect(window,next_piece_space_color,next_piece_space)

        #draw space 
        for x in range(10):
            for y in range(20):
                if self.space[y][x] != (0,0,0) :
                    box_rect = pygame.Rect(int(main_window_size*0.625/2)+x*square_size,int(main_window_size*0.25/2)+y*square_size,square_size,square_size)
                    pygame.draw.rect(window,self.space[y][x],box_rect)

        #draw current element
        self.current_element.draw_element()

        #draw held and next elemets 
        self.next_element.position = Vector2(10,10) # position is for test
        self.next_element.draw_element()
        self.held_element.position = Vector2(-5,2) # position is for test
        self.held_element.draw_element()

        #drawing the grid
        for x in range(int(main_window_size*0.625/2), int(main_window_size*0.625/2)+10*square_size, square_size):
            for y in range(int(main_window_size*0.25/2), int(main_window_size*0.25/2)+20*square_size, square_size):
                rect = pygame.Rect(x, y, square_size, square_size)
                pygame.draw.rect(window, grid_color, rect,grid_thickeness)

    def update_game(self):
        self.current_element.position += Vector2(0,1)

    def move_right(self):
        self.current_element.position += Vector2(1,0)

    def move_left(self):
        self.current_element.position += Vector2(-1,0)

    def move_down(self):
        self.current_element.position += Vector2(0,1)

    def rotate(self):
        if self.current_element.orientation == 4 :
            self.current_element.orientation = 1 
        else : 
            self.current_element.orientation += 1
        
        self.current_element.body = self.current_element.element_body()

    def bring_down(self):
        pass 

    def hold(self):
        pass 


     
