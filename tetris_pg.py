
from pygame.constants import KEYDOWN, K_UP, K_DOWN,K_RIGHT,K_LEFT
import pygame, sys, random 
from pygame.math import Vector2


class ELEMENT():
    def __init__(self) -> None:
        self.position = Vector2(9,4)
        self.type = random.choice(["T","S","Z","L","L2","O","I"])
        self.body_size = Vector2(5,5)
        self.orientation = 1
        self.body = self.decide_body()

    def decide_body(self):
        if self.type == "T":
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
        elif self.type == "S":
            if self.orientation in [1,3]  :
                self.body = [Vector2(1,0),Vector2(2,0),Vector2(0,1),Vector2(1,1)]
                self.body_size = Vector2(3,2)
            else : 
                self.body = [Vector2(0,0),Vector2(0,1),Vector2(1,1),Vector2(1,2)]
                self.body_size = Vector2(2,3)
        elif self.type == "Z": 
            if self.orientation in [1,3] :
                self.body = [Vector2(0,0),Vector2(1,0),Vector2(1,1),Vector2(2,1)]
                self.body_size = Vector2(3,2)
            else : 
                self.body = [Vector2(1,0),Vector2(1,1),Vector2(0,1),Vector2(0,2)]
                self.body_size = Vector2(2,3)
        elif self.type == "L":
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
        elif self.type == "L2":
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
        elif self.type == "O":
            self.body = [Vector2(0,0),Vector2(0,1),Vector2(1,0),Vector2(1,1)]
            self.body_size = Vector2(2,2)
        elif self.type == "I":
            if self.orientation in [1,3] :
                self.body = [Vector2(0,1),Vector2(0,2),Vector2(0,3),Vector2(0,0)]
                self.body_size = Vector2(4,1)
            else : 
                self.body = [Vector2(1,0),Vector2(2,0),Vector2(3,0),Vector2(0,0)]
                self.body_size = Vector2(1,4)
        return self.body

    
    def draw_element(self):
        for box in self.body : 
            box_rect = pygame.Rect((self.position.x +box.x)*cell_size,(self.position.y+box.y)*cell_size,cell_size,cell_size)
            pygame.draw.rect(window,pygame.Color("yellow"),box_rect)



class GAME():
    def __init__(self) -> None:
        self.score = 0 
        self.element = ELEMENT()
        self.space = [ [ 0 for _ in range(width)] for __ in range(height)]

    def draw_game(self):
        self.draw_space()
        self.element.draw_element()

    def update(self):
        self.element.position.y += 1
        self.check_collisions()
        self.check_cleared_lines()

    def draw_space(self):
        for x in range(width):
            for y in range(height):
                if self.space[y][x]==1:
                    single_space_rect = pygame.Rect((x+5)*cell_size,(y+5)*cell_size,cell_size,cell_size)
                    pygame.draw.rect(window,pygame.Color("black"),single_space_rect)

    def check_collisions(self):
        collision = False
        for box in self.element.body: 
            if box.y+self.element.position.y-5 == 19 or self.space[int(box.y+self.element.position.y+1-5)][int(box.x+self.element.position.x-5)] == 1 : 
                collision = True 
        
        for x in range(10):
            if self.space[0][x] == 1:
                self.game_over()


        if collision : 
            self.merge_to_space()
            self.element = ELEMENT()

    def check_cleared_lines(self):
        for y in range(20):
            if self.space[y] == [1,1,1,1,1,1,1,1,1,1] :
                for line_index in range(y,1,-1):
                    self.space[line_index] = self.space[line_index-1]
            self.score += 1

    
    def merge_to_space(self):
        for box in self.element.body :
            self.space[int(box.y+self.element.position.y-5)][int(box.x+self.element.position.x - 5)]=1


    def rotate(self):
        if self.element.orientation == 4 :
            self.element.orientation = 1 
        else :
            self.element.orientation += 1
        
        self.element.decide_body()
        
        collision = False
        for box in self.element.body : 
            if box.y + self.element.position.y - 5 >= 19 or box.x + self.element.position.x -5 <0 or box.x + self.element.position.x -5 >9 or self.space[int(box.y + self.element.position.y - 5)][int(box.x + self.element.position.x - 5)] == 1 :
                collision = True 

        if collision : 
            if self.element.orientation == 1 : 
                self.element.orientation = 4 
            else :
                self.element.orientation -= 1
            self.element.decide_body()
            

    def move_right(self):
        tight = False
        for box in self.element.body : 
            if box.x + self.element.position.x - 5 == 9  or self.space[int(box.y + self.element.position.y - 5 )][int(box.x + self.element.position.x - 5)+1] ==1:
                tight = True

        if not tight : 
            self.element.position.x+=1
                
    def move_left(self):
        tight = False
        for box in self.element.body : 
            if box.x + self.element.position.x - 5 == 0  or self.space[int(box.y + self.element.position.y - 5 )][int(box.x + self.element.position.x - 5)-1] ==1:
                tight = True

        if not tight : 
            self.element.position.x-=1

    def bring_down(self):

        if self.element.position.y == 5 :
            self.element.position.y +=1 

        while self.element.position.y != 5 :
            self.element.position.y +=1 
            self.check_collisions()

    def game_over(self):
        pygame.quit()
        sys.exit()








# settings 

cell_size = 20
width = 10 
height = 20 



pygame.init()

clock = pygame.time.Clock()


main_game = GAME()

window = pygame.display.set_mode((width*cell_size*2,height*cell_size*1.5))
playing_area = pygame.Surface((cell_size*width,cell_size*height))
playing_area_rect = pygame.Rect(0.5*width*cell_size,0.25*height*cell_size,width*cell_size,height*cell_size)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,500)


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE :
            main_game.update()
        
        if event.type == KEYDOWN :
            if event.key == K_UP: 
                main_game.rotate()
            if event.key == K_DOWN: 
                main_game.bring_down()
            if event.key == K_RIGHT: 
                main_game.move_right()
            if event.key == K_LEFT: 
                main_game.move_left()


    window.fill((94,219,167))
    pygame.draw.rect(window,(57,220,244),playing_area_rect)
    main_game.draw_game()

    pygame.display.update()
    clock.tick(30)


    
    