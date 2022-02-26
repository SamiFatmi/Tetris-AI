import pygame
from pygame.math import Vector2

class ELEMENT:
    """ Will contain element shapes and colors and functions for drawing the elements"""
    def __init__(self) -> None:
        self.position = (4,2)
        self.body = [Vector2(0,0),Vector2(0,1),Vector2(0,2),Vector2(0,3)]

    def draw_element(self):
        from tetris_pygame import window # place here to avoid the circular import error 
        from tetris_pygame import square_size, main_window_size
        for element in self.body : 
            element_rect = pygame.Rect(int(main_window_size*0.625/2)+(self.position[0]+element[0])*square_size,int(main_window_size*0.25/2)+(self.position[1]+element[1])*square_size,square_size,square_size)
            pygame.draw.rect(window,(0,0,0),element_rect)