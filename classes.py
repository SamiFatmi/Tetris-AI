from audioop import reverse
from multiprocessing.dummy import current_process
from turtle import position
import pygame, random
from pygame.math import Vector2
import operator

class ELEMENT:
    """ Will contain element shapes and colors and functions for drawing the elements"""
    def __init__(self) -> None:
        self.position = Vector2(4,-1)
        self.orientation = 1
        self.element_name = random.choice(["L","J","I","O","S","Z","T"])
        self.body = self.element_body()
        self.color = self.element_color()

    def draw_element(self):
        from tetris_pygame import window # place here to avoid the circular import error 
        from tetris_pygame import square_size, main_window_size
        for element in self.body : 
            if element[1] + self.position[1] > -1 :
                element_rect = pygame.Rect(int(main_window_size*0.625/2)+(self.position[0]+element[0])*square_size,int(main_window_size*0.25/2)+(self.position[1]+element[1])*square_size,square_size,square_size)
                pygame.draw.rect(window,self.color,element_rect)


    def element_body(self): #decide the element body depending on what element and what orientation it is 
        if self.element_name == "T":
            if self.orientation == 1 :
                self.body = [Vector2(-1,0),Vector2(0,0),Vector2(0,-1),Vector2(1,0)]
                self.body_size = Vector2(3,2)
            elif self.orientation == 2: 
                self.body = [Vector2(0,-1),Vector2(0,0),Vector2(0,1),Vector2(1,0)]
                self.body_size = Vector2(2,3)
            elif self.orientation == 3 :
                self.body = [Vector2(-1,0),Vector2(0,0),Vector2(0,1),Vector2(1,0)]
                self.body_size = Vector2(3,2)
            elif self.orientation == 4:
                self.body = [Vector2(-1,0),Vector2(0,-1),Vector2(0,0),Vector2(0,1)]
                self.body_size = Vector2(2,3)
        elif self.element_name == "S":
            if self.orientation in [1,3] :
                self.body = [Vector2(-1,1),Vector2(0,1),Vector2(0,0),Vector2(1,0)]
                self.body_size = Vector2(3,2)
            else : 
                self.body = [Vector2(0,-1),Vector2(0,0),Vector2(1,0),Vector2(1,1)]
                self.body_size = Vector2(2,3)
        elif self.element_name == "Z": 
            if self.orientation in [1,3] :
                self.body = [Vector2(-1,0),Vector2(0,0),Vector2(0,1),Vector2(1,1)]
                self.body_size = Vector2(3,2)
            else : 
                self.body = [Vector2(0,1),Vector2(0,0),Vector2(1,0),Vector2(1,-1)]
                self.body_size = Vector2(2,3)
        elif self.element_name == "L":
            if self.orientation == 1 :
                self.body = [Vector2(-1,1),Vector2(-1,0),Vector2(0,0),Vector2(1,0)]
                self.body_size = Vector2(2,3)
            elif self.orientation == 2: 
                self.body = [Vector2(-1,-1),Vector2(0,-1),Vector2(0,0),Vector2(0,1)]
                self.body_size = Vector2(3,2)
            elif self.orientation == 3 :
                self.body = [Vector2(-1,0),Vector2(0,0),Vector2(1,0),Vector2(1,-1)]
                self.body_size = Vector2(2,3)
            elif self.orientation == 4:
                self.body = [Vector2(0,-1),Vector2(0,0),Vector2(0,1),Vector2(1,1)]
                self.body_size = Vector2(3,2)
        elif self.element_name == "J":
            if self.orientation == 1 :
                self.body = [Vector2(-1,0),Vector2(0,0),Vector2(1,0),Vector2(1,1)]
                self.body_size = Vector2(2,3)
            elif self.orientation == 2: 
                self.body = [Vector2(-1,1),Vector2(0,-1),Vector2(0,0),Vector2(0,1)]
                self.body_size = Vector2(3,2)
            elif self.orientation == 3 :
                self.body = [Vector2(-1,-1),Vector2(-1,0),Vector2(0,0),Vector2(1,0)]
                self.body_size = Vector2(2,3)
            elif self.orientation == 4:
                self.body = [Vector2(0,-1),Vector2(0,0),Vector2(0,1),Vector2(1,-1)]
                self.body_size = Vector2(3,2)
        elif self.element_name == "O":
            self.body = [Vector2(0,0),Vector2(0,1),Vector2(1,0),Vector2(1,1)]
            self.body_size = Vector2(2,2)
        elif self.element_name == "I":
            if self.orientation in [1,3] :
                self.body = [Vector2(0,-2),Vector2(0,-1),Vector2(0,0),Vector2(0,1)]
                self.body_size = Vector2(4,1)
            else : 
                self.body = [Vector2(-2,0),Vector2(-1,0),Vector2(0,0),Vector2(1,0)]
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
        elif self.element_name == "J":
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
        self.held_element = 0
        self.space = [ [ (0,0,0) for _ in range(10)] for __ in range(20)]
        self.score = 0
        self.game_over = False

    def draw_game(self):
        from tetris_pygame import main_window_size, square_size,window,grid_color,grid_thickeness,game_space_color,hold_space_color,score_background_color,next_piece_space_color,play_space,hold_space,score_space,next_piece_space,stroke_space,stroke_color,stroke_thickeness


        # drawing surfaces
        pygame.draw.rect(window,stroke_color,stroke_space)
        pygame.draw.rect(window,game_space_color,play_space)
        pygame.draw.rect(window,hold_space_color,hold_space,stroke_thickeness)
        pygame.draw.rect(window,score_background_color,score_space,stroke_thickeness)
        pygame.draw.rect(window,next_piece_space_color,next_piece_space,stroke_thickeness)

        #draw space 
        for x in range(10):
            for y in range(20):
                if self.space[y][x] != (0,0,0) :
                    box_rect = pygame.Rect(int(main_window_size*0.625/2)+x*square_size,int(main_window_size*0.25/2)+y*square_size,square_size,square_size)
                    pygame.draw.rect(window,self.space[y][x],box_rect)

        #draw current element
        self.current_element.draw_element()

        #draw next element 
        self.next_element.position = Vector2(14,4) # position is for test
        self.next_element.draw_element()

        #draw held element 
        if self.held_element != 0 :
            self.held_element.position = Vector2(-5,4) # position is for test
            self.held_element.draw_element()

        #drawing the grid
        for x in range(int(main_window_size*0.625/2), int(main_window_size*0.625/2)+10*square_size, square_size):
            for y in range(int(main_window_size*0.25/2), int(main_window_size*0.25/2)+20*square_size, square_size):
                rect = pygame.Rect(x, y, square_size, square_size)
                pygame.draw.rect(window, grid_color, rect,grid_thickeness)

        #writing Score and HOLD and NEXT
        pygame.font.init()
        score_font = pygame.font.SysFont('Times New Roman', 30)
        score_textsurface = score_font.render(f"Score : {self.score}", False, (0, 0, 0))
        next_font = pygame.font.SysFont('Times New Roman', 30)
        next_textsurface = next_font.render('Next', False, (0, 0, 0))
        hold_font = pygame.font.SysFont('Times New Roman', 30)
        hold_textsurface = hold_font.render('Hold', False, (0, 0, 0))

        window.blit(score_textsurface,(main_window_size//2.5,main_window_size//25))
        window.blit(next_textsurface,(main_window_size*0.8,main_window_size//7.5))
        window.blit(hold_textsurface,(main_window_size//9,main_window_size//7.5))

    def update_game(self):
        self.check_collisions()
        self.check_cleared_lines()
        self.check_game_over()
        self.current_element.position += Vector2(0,1)

    def move_right(self):
        move = True 
        for box in self.current_element.body : 
            if box[1] + self.current_element.position[1] >= 0 and (box[0]+self.current_element.position[0] == 9 or self.space[int(self.current_element.position[1] + box[1])][int(self.current_element.position[0] + box[0]+1)] != (0,0,0)):
                move = False
                break 
        if move :    
            self.current_element.position += Vector2(1,0)

    def move_left(self):
        move = True 
        for box in self.current_element.body : 
            if box[1] + self.current_element.position[1] >= 0 and (box[0]+self.current_element.position[0] == 0 or self.space[int(self.current_element.position[1] + box[1])][int(self.current_element.position[0] + box[0]-1)] != (0,0,0)):
                move = False
                break 
        if move :  
            self.current_element.position += Vector2(-1,0)
        return move

    def move_down(self):
        move = True 
        for box in self.current_element.body : 
            if self.current_element.position[1] + box[1] == 19 or self.space[int(self.current_element.position[1] + box[1]+1)][int(self.current_element.position[0] + box[0])] != (0,0,0):
                move = False 
                break
        
        if move :
            self.current_element.position += Vector2(0,1)
        return move

    def rotate(self):
        current_oriention = self.current_element.orientation
        self.current_element.orientation = self.current_element.orientation + 1 if self.current_element.orientation <4 else 1
        self.current_element.body = self.current_element.element_body()

        clear = True 
        for box in self.current_element.body : 
            if box[1] + self.current_element.position[1] >= 0 and (self.current_element.position[0] + box[0] >9 or self.current_element.position[0] + box[0] < 0 or self.space[int(self.current_element.position[1] + box[1])][int(self.current_element.position[0] + box[0])]!=(0,0,0)):
                clear = False 
                break 
        
        if not clear : 
            right_clear = True 
            # check right :
            for box in self.current_element.body : 
                if box[0]+self.current_element.position[0]+1>9 or self.space[int(box[1]+self.current_element.position[1])][int(box[0]+self.current_element.position[0]+1)]!=(0,0,0):
                    right_clear = False
                    break
            left_clear = True
            for box in self.current_element.body : 
                if box[0]+self.current_element.position[0]-1<0 or self.space[int(box[1]+self.current_element.position[1])][int(box[0]+self.current_element.position[0]-1)]!=(0,0,0):
                    left_clear = False
                    break

            if right_clear:
                self.move_right()
                out = False
                for box in self.current_element.body :
                    if self.current_element.position[0] + box[0] < 0 or self.space[int(self.current_element.position[1] + box[1])][int(self.current_element.position[0] + box[0])]!=(0,0,0):
                        out = True
                        break 

                if out : #double checking for the I elements when on the left side of the screen
                    right_clear = True 
                    for box in self.current_element.body : 
                        if box[0]+self.current_element.position[0]+1>9 or self.space[int(box[1]+self.current_element.position[1])][int(box[0]+self.current_element.position[0]+1)]!=(0,0,0):
                            right_clear = False
                            break
                    
                    if right_clear:
                        self.move_right()
                    else: 
                        self.current_element.orientation = current_oriention
                        self.current_element.body = self.current_element.element_body()

            elif left_clear:
                self.move_left()     
            else:
                self.current_element.orientation = current_oriention
                self.current_element.body = self.current_element.element_body()
        


    def bring_down(self):
        move = True 
        while move : 
            move = True 
            for box in self.current_element.body : 
                if self.current_element.position[1] + box[1] == 19 or self.space[int(self.current_element.position[1] + box[1]+1)][int(self.current_element.position[0] + box[0])] != (0,0,0):
                    move = False 
                    break
            
            if move :
                self.current_element.position += Vector2(0,1)


    def hold(self):
        if self.held_element == 0 : 
            self.held_element = self.current_element
            self.current_element = self.next_element 
            self.current_element.position = Vector2(4,-1)
            self.next_element = ELEMENT() 
        else : 
            element = self.current_element 
            self.current_element = self.held_element
            self.current_element.position = element.position
            self.held_element = element

    def merge_element_to_space(self):
        for box in self.current_element.body : 
            self.space[int(self.current_element.position[1] + box[1])][int(self.current_element.position[0] + box[0])] = self.current_element.color

        self.next_element.position = Vector2(4,-1)
        self.current_element = self.next_element
        self.next_element = ELEMENT()

    def check_collisions(self):
        for box in self.current_element.body : 
            if (box[1]+self.current_element.position[1])>-1 and (self.current_element.position[1] + box[1] == 19 or self.space[int(self.current_element.position[1] + box[1]+1)][int(self.current_element.position[0] + box[0])] != (0,0,0)):
                self.merge_element_to_space()
                break
    
    def clear_line(self,i):
        for line_index in range(i,0,-1):
            self.space[line_index]=self.space[line_index-1][:]

    def check_cleared_lines(self):
        line_to_clear = True 

        while line_to_clear: 
            for i,line in enumerate(self.space): 
                clear = True 
                for box in line : 
                    if box == (0,0,0):
                        clear = False 
                        break
                
                if clear : 
                    self.score += 1
                    self.clear_line(i)
                    break

            if not clear : 
                line_to_clear = False
    
    def check_game_over(self):
        if self.space[0]!=[(0,0,0) for _ in range(10)]:
            self.game_over = True 


        
class AI: 
    def __init__(self) -> None:
        self.game = GAME()
        self.weights = [random.random() for _ in range(4)]
        self.current_best_orientation = 0
        self.current_best_x = 0 
        self.current_best_y = 0 
        self.check = True 

    def update(self):
        if self.check :
            self.decide_best_position()
        self.move_to()
        self.game.update_game()

    def move_right(self):
        self.game.move_right()

    def decide_best_position(self):
        # find possible orientations
        if self.game.current_element.element_name in ["L","J","T"]:
            possible_orientations = [1,2,3,4]
        elif self.game.current_element.element_name in ["S","Z","I"]:
            possible_orientations = [1,2]
        else : 
            possible_orientations = [1]

        positions_scores = []
        for orientation in possible_orientations:
            # find right and left limit
            self.game.current_element.orientation = orientation
            self.game.current_element.body = self.game.current_element.element_body()

            right_limit = int(9 - self.game.current_element.body[-1][0]) 
            left_limit =  int(- self.game.current_element.body[0][0] )

            # find each possible positions 
            available_positions = []
            for position in range(left_limit,right_limit+1,1):
                found = False
                for height in range(0,19):
                    for box in self.game.current_element.body:
                        if 0 <= box[1]+height <= 19  and (box[1]+height == 19 or self.game.space[int(box[1]+height-1)][int(box[0]+position)]!= (0,0,0)):
                            available_positions.append([orientation,position,height])
                            print(position,height)
                            found = True
                            break 
                    if found : 
                        break


        #calculate score based on cleared line, bumpiness, created holes
        for possible_position in available_positions: 

            orientation = possible_position[0]
            x = possible_position[1]
            y = possible_position[2]

            #copying space and placing the item in it to calculate the score
            hypothetical_space = [ self.game.space[i][:] for i in range(len(self.game.space))]
            for box in self.game.current_element.body: 
                hypothetical_space[int(box[1]+y)][int(box[0]+x)] = (100,100,100)

            #calculate score
            bumpiness = self.bumpiness(hypothetical_space)
            cleared_lines = self.cleared_lines(hypothetical_space)
            created_holes = self.holes(hypothetical_space)
            height = self.height(hypothetical_space)
            score = self.weights[0]*bumpiness + self.weights[1]*cleared_lines + self.weights[2]*created_holes + self.weights[3]*created_holes

            #add score and position details to list
            positions_scores.append([score,orientation,x,y])
        
        #find out the best decision
        positions_scores = sorted(positions_scores,key=operator.itemgetter(0), reverse=True)
        
        #assign to self 
        self.current_best_orientation = positions_scores[0][1]
        self.current_best_x = positions_scores[0][2]

        self.check = False
        
    

    def bumpiness(self,space):
        current_height=0
        previous_height = 0 
        bumpiness=0

        for column in range(10):
            previous_height=current_height
            for y in range(20):
                if space[y][column]!=(0,0,0):
                    current_height = 19-y
                    break 
            bumpiness += abs(current_height-previous_height)

        return bumpiness
            
    def cleared_lines(self,space):
        cleared_lines = 0
        for line in space:
            cleared = True
            for box in line : 
                if box == (0,0,0):
                    cleared = False
                    break
            if cleared : 
                cleared_lines += 1
          
        return cleared_lines  

    def holes(self,space):
        holes = 0
        for column in range(10):
            found_top = False     
            for y in range(20):
                if not found_top and space[y][column]!=(0,0,0):
                    found_top=True 
                elif space[y][column]==(0,0,0) :
                    holes+=1
                    
        return holes 


    def height(self,space):
        height = 0 
        for column in range(10):
            for y in range(20):
                if space[y][column]!=(0,0,0):
                    height += 19-y
                    break 
        return height


    def move_to(self):
        if self.game.current_element.orientation != self.current_best_orientation : 
            self.game.rotate()
        elif self.game.current_element.position[0] < self.current_best_x :  
            self.game.move_right()
        elif self.game.current_element.position[0] > self.current_best_x :
            self.game.move_left()
        else :
            self.game.bring_down()
            self.check = True



     
