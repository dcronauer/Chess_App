


from turtle import position
import chessboard
import sys

#import pygame
DICT_COLUMNS = {'A': 1,'B': 2,'C': 3,'D': 4,'E': 5,'F': 6,'G': 7, 'H': 8}
DICT_ROWS = {1: 1,2: 2,3: 3,4: 4,5: 5,6: 6,7: 7,8: 8}
DICT_COLUMNS_REVERSED = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
DICT_POSSIBLE_MOVES = {}
DICT_PIECES = {}
DICT_PIECE_REVERSE = {}
PIECE_DICTIONARY = {'whitepawn': ['white', 'pawn', 'images/white_p.png',8],  'whiteknight': ['white', 'knight','images/white_n.png',2], 'whitebishop': ['white', 'bishop','images/white_b.png',2], 'whiterook': ['white', 'rook','images/white_r.png',2], 'whitequeen': ['white', 'queen','images/white_q.png',1], 'whiteking': ['white', 'king','images/white_k.png',1], \
    'blackpawn': ['black','pawn','images/black_p.png',8], 'blackknight': ['black', 'knight','images/black_n.png',2], 'blackbishop': ['black', 'bishop','images/black_b.png',2], 'blackrook': ['black', 'rook','images/black_r.png',2], 'blackqueen': ['black', 'queen','images/black_q.png',1], 'blackking': ['black', 'king','images/black_k.png',1]}
DICT_COUNT_PIECES = {}
#  BOARD_CORDINATES = {'A1': 'whiterook1', 'A2': 'whitepawn1', 'A3': None , 'A4': None, 'A5': None, 'A6': None, 'A7': 'blackpawn1', 'A8': 'blackrook1', 'B1': 'wn1', 'B2': 'whitepawn2' , 'B3': None, 'B4': None, 'B5': None, 'B6': None, 'B7': 'blackpawn2', 'B8': 'blackknight1', 'C1': 'whitebishop1', 'C2': 'whitepawn3', 
#  'C3': None, 'C4': None, 'C5': None, 'C6': None, 'C7': 'blackpawn3', 'C8': 'blackbishop1', 'D1': "whitequeen1", 'D2': 'whitepawn4', 'D3': None, 'D4': None, 'D5': None, 'D6': None, 'D7': 'blackpawn4', 'D8': 'blackqueen1', 'E1': 'whiteking1', 'E2': 'whitepawn5', 'E3': None, 'E4': None, 'E5': None, 'E6': None, 
#  'E7': 'blackpawn5', 'E8': 'blackking1', 'F1': 'whitebishop2', 'F2': 'whitepawn6', 'F3': None, 'F4': None, 'F5': None, 'F6': None, 'F7': 'blackpawn6', 'F8': 'blackbishop2', 'G1': 'wn2', 'G2': 'whitepawn7', 'G3': None, 'G4': None, 'G5': None, 'G6': None, 'G7': 'blackpawn7', 'G8': 'bn2', 'H1': 'whiterook2', 'H2': 'whitepawn8', 
#  'H3': None, 'H4': None, 'H5': None, 'H6': None, 'H7': 'blackpawn8', 'H8': 'blackrook2'}
POSITION_START = {'whiterook1': 'A1', 'whitepawn1': 'A2', 'blackpawn1': 'A7', 'blackrook1': 'A8', 'whiteknight1': 'B1', 'whitepawn2': 'B2', 'blackpawn2': 'B7', 'blackknight1': 'B8', 'whitebishop1': 'C1', 'whitepawn3': 'C2', 'blackpawn3': 'C7', 'blackbishop1': 'C8', 'whitequeen1': 'D1', 'whitepawn4': 'D2', 'blackpawn4': 'D7', 'blackqueen1': 'D8', 
'whiteking1': 'E1', 'whitepawn5': 'E2', 'blackpawn5': 'E7', 'blackking1': 'E8', 'whitebishop2': 'F1', 'whitepawn6': 'F2', 'blackpawn6': 'F7', 'blackbishop2': 'F8', 'whiteknight2': 'G1', 'whitepawn7': 'G2', 'blackpawn7': 'G7', 'blackknight2': 'G8', 'whiterook2': 'H1', 'whitepawn8': 'H2', 'blackpawn8': 'H7', 'blackrook2': 'H8'}
POSITION_CENTER = {'A1': [50, 750], 'A2': [50, 650], 'A3': [50, 550], 'A4': [50, 450], 'A5': [50, 350], 'A6': [50, 250], 'A7': [50, 150], 'A8': [50, 50], 'B1': [150, 750], 'B2': [150, 650], 'B3': [150, 550], 'B4': [150, 450], 'B5': [150, 350], 'B6': [150, 250], 'B7': [150, 150], 'B8': [150, 50], 'C1': [250, 750], 'C2': [250, 650], 'C3': [250, 550], 'C4': [250, 450], 'C5': [250, 350], 'C6': [250, 250], 'C7': [250, 150], 'C8': [250, 50], 'D1': [350, 750], 'D2': [350, 650], 'D3': [350, 550], 'D4': [350, 450], 'D5': [350, 350], 'D6': [350, 250], 'D7': [350, 150], 'D8': [350, 50], 'E1': [450, 750], 'E2': [450, 650], 'E3': [450, 550], 'E4': [450, 450], 'E5': [450, 350], 'E6': [450, 250], 'E7': [450, 150], 'E8': [450, 50], 'F1': [550, 750], 'F2': [550, 650], 'F3': [550, 550], 'F4': [550, 450], 'F5': [550, 350], 'F6': [550, 250], 'F7': [550, 150], 'F8': [550, 50], 'G1': [650, 750], 'G2': [650, 650], 'G3': [650, 550], 'G4': [650, 450], 'G5': [650, 350], 'G6': [650, 250], 'G7': [650, 150], 'G8': [650, 50], 'H1': [750, 750], 'H2': [750, 650], 'H3': [750, 550], 'H4': [750, 450], 'H5': [750, 350], 'H6': [750, 250], 'H7': [750, 150], 'H8': [750, 50]}
CASTLE_DICT = {"white": False, "black": False}
CASTLE_DICT_LONG = {"white": False, "black": False}
POSITION_START_2 = {'whiterook1': 'A1', 'whitepawn1': 'A2', 'blackpawn1': 'A7', 'blackrook1': 'A8', 'wn1': 'B1', 'whitepawn2': 'B2', 'blackpawn2': 'B7', 'blackknight1': 'B8', 'whitebishop1': 'C1', 'whitepawn3': 'C2', 'blackpawn3': 'C7', 'blackbishop1': 'C8', 'whitequeen1': 'D1', 'whitepawn4': 'D2', 'blackpawn4': 'D7', 'blackqueen1': 'D8', 
'whiteking1': 'E1', 'whitepawn5': 'E2', 'blackpawn5': 'E7', 'blackking1': 'E8', 'whitebishop2': 'F1', 'whitepawhiteknight6': 'F2', 'blackpawn6': 'F7', 'blackbishop2': 'F8', 'whiteknigth2': 'G1', 'whitepawn7': 'G2', 'blackpawn7': 'G7', 'blackknight2': 'G8', 'whiterook2': 'H1', 'whitepawn8': 'H2', 'blackpawn8': 'H7', 'blackrook2': 'H8'}
black_piece_dict = {}
white_piece_dict = {}
class Pieces:
    BOARD_CORDINATES = {'A1': False, 'A2': False, 'A3': False , 'A4': False, 'A5': False, 'A6': False, 'A7': False, 'A8': False, 'B1': False, 'B2': False , 'B3': False, 'B4': False, 'B5': False, 'B6': False, 'B7': False, 'B8': False, 'C1': False, 'C2': False, 
 'C3': False, 'C4': False, 'C5': False, 'C6': False, 'C7': False, 'C8': False, 'D1': False, 'D2': False, 'D3': False, 'D4': False, 'D5': False, 'D6': False, 'D7': False, 'D8': False, 'E1': False, 'E2': False, 'E3': False, 'E4': False, 'E5': False, 'E6': False, 
 'E7': False, 'E8': False, 'F1': False, 'F2': False, 'F3': False, 'F4': False, 'F5': False, 'F6': False, 'F7': False, 'F8': False, 'G1': False, 'G2': False, 'G3': False, 'G4': False, 'G5': False, 'G6': False, 'G7': False, 'G8': False, 'H1': False, 'H2': False, 
 'H3': False, 'H4': False, 'H5': False, 'H6': False, 'H7': False, 'H8': False}
    
    def __init__(self, color, type, image, piece_number = None, position = None, destroyed = False, kill = False, moved = False,cordinates=None, 
    id=None, starting_row = None,board_image = None,name = None):
        self.color = color
        self.type = type
        self.image = image
        self.destroy = destroyed
        self.position = position
        self.kill = kill
        self.moved = moved
        self.cordinates = cordinates
        self.id = id
        self.starting_row = None
        self.board_image = board_image
        self.piece_number = piece_number
        self.name = name
        
    #accessor
    def get_piece(self):
        return (self.color,self.type,self.image, self.position)
    
    def get_id(self):
        return self.id, self
    def get_color(self):
        return self.color
    
    def get_row(self):
        return self.starting_row
    
    def get_board_cord(self):
        print(self.BOARD_CORDINATES)
        return self.BOARD_CORDINATES
    def get_moved(self):
        return self.moved
    def get_position(self):
        return self.position
    def get_row(self):
        row = self.position[1]
        return row
    def get_piece_number(self):
        return self.piece_number
    #mutator
    def set_piece_number(self,number):
        self.piece_number = number
        

    def set_position(self):
        color1, type1, image, position = Pieces.get_piece(self)
        number = Pieces.get_piece_number(self)
        block = color1 + type1 + str(number)
        
        self.position = POSITION_START.get(block)
        
        self.BOARD_CORDINATES[self.position] = self
    def set_promote_position(self,position):
        color1, type1, image, ignore = Pieces.get_piece(self)
        number = Pieces.get_piece_number(self)
        block = color1 + type1 + str(number)
        
        self.position = position
        
        self.BOARD_CORDINATES[self.position] = self

    def set_move_position(self,position_id):
        print(self.position,"before change")
        self.BOARD_CORDINATES[self.position] = False
        self.position = position_id
        print(self.position)

        self.BOARD_CORDINATES[self.position] = self
        
    def set_move(self):
        self.moved = True
        print("moved is true")

    def set_id(self,id):
        self.id = id 
    
    def set_board_image(self,board_image):
        self.board_image = board_image
    
    #this function will run through the possible moves of each piece. 
   

    #promote pawn
   
    #movement functions by piece    
    def rook_moves(self):
        position = self.position
        max_range = 8
        row = int(position[1])
        column = position[0]
        starting_row = DICT_ROWS[row]
        starting_column = DICT_COLUMNS[column]
        self.above(starting_row, column, max_range, position)
        self.below(starting_row, column, position,max_range)
        self.left(starting_row,starting_column,max_range,position)
        self.right(starting_row, starting_column, max_range, position)   
        
        
    def pawn_moves(self,enpassant,turn_num,en_passant_dict):
        print (en_passant_dict)
        print(turn_num)
        if self.moved == False:
            max_range = 2
        else:
            max_range =1
        position = self.position
        row = int(position[1])
        column = position[0]
        starting_column = DICT_COLUMNS[column]
        if self.starting_row == 2:
            #check left side for enpassant
            if starting_column - 1 >= 1:
                left_column = starting_column -1
                column_string = DICT_COLUMNS_REVERSED.get(left_column)
                position_left = column_string + str(row)
                print(position_left, "this is the position next to the pawn")
                self.check = self.BOARD_CORDINATES.get(position_left)
                print(self.check)
                enpassant_position = en_passant_dict.get(turn_num,"none")
                print(enpassant_position)
                if self.check != False and enpassant_position == position_left:
                        string_en_passant = column_string + str(row +1)
                        DICT_POSSIBLE_MOVES[ string_en_passant] =  string_en_passant
            #check right side for enpassant
            if starting_column + 1 <= 8 and enpassant:
                right_column = starting_column + 1
                column_string = DICT_COLUMNS_REVERSED.get(right_column)
                position_right = column_string + str(row)
                print(position_right, "this is the position next to the pawn")
                self.check = self.BOARD_CORDINATES.get(position_right)
                print(self.check)
                enpassant_position = en_passant_dict.get(turn_num,"none")
                if self.check != False and enpassant_position == position_right:
                        string_en_passant = column_string + str(row +1)
                        DICT_POSSIBLE_MOVES[ string_en_passant] =  string_en_passant

            for i in range(max_range):
                
                if i == 0:
                    max_range = 1
                    self.left_diagonal(row,column,starting_column,position,max_range)
                    self.right_diagonal(row,column,starting_column,position,max_range)
                row += 1
                column1 = DICT_COLUMNS_REVERSED[starting_column]
                string = column1 + str(row)    
                self.check = self.BOARD_CORDINATES.get(string)
                
                if self.check != False:
                 pass      
                elif self.check == False:
                  DICT_POSSIBLE_MOVES[string] = string 

        if self.starting_row == 7:
              #check left side for enpassant
            if starting_column - 1 >= 1 and enpassant:
                left_column = starting_column -1
                column_string = DICT_COLUMNS_REVERSED.get(left_column)
                position_left = column_string + str(row)
                print(position_left, "this is the position next to the pawn")
                self.check = self.BOARD_CORDINATES.get(position_left)
                print(self.check)
                enpassant_position = en_passant_dict.get(turn_num,"none")
                if self.check != False and enpassant_position == position_left: 
                        string_en_passant = column_string + str(row  - 1)
                        DICT_POSSIBLE_MOVES[ string_en_passant] =  string_en_passant
            #check right side for enpassant
            if starting_column + 1 <= 8 and enpassant:
                right_column = starting_column + 1
                column_string = DICT_COLUMNS_REVERSED.get(right_column)
                position_right = column_string + str(row)
                print(position_right, "this is the position next to the pawn")
                self.check = self.BOARD_CORDINATES.get(position_right)
                print(self.check)
                enpassant_position = en_passant_dict.get(turn_num,"none")
                if self.check != False and enpassant_position == position_right:
                        string_en_passant = column_string + str(row - 1)
                        DICT_POSSIBLE_MOVES[ string_en_passant] =  string_en_passant
            for i in range(max_range):
                if i == 0:
                    max_range = 1
                    self.left_diagonal(row,column,starting_column,position,max_range)
                    self.right_diagonal(row,column,starting_column,position,max_range)
                    
                row -=1
                column1 = DICT_COLUMNS_REVERSED[starting_column]
                string = column1 + str(row)    
                self.check = self.BOARD_CORDINATES.get(string)
                   
                if self.check != False:
                    pass      
                elif self.check == False:
                    DICT_POSSIBLE_MOVES[string] = string  
        
    
    def bishop_moves(self):
        max_range = 8
        position = self.position
        print(position)
        row = int(position[1])
        column = position[0]
        starting_column = DICT_COLUMNS[column]
        print('got to bishop method')     
        self.left_diagonal(row,column,starting_column,position,max_range)
        self.right_diagonal(row,column,starting_column,position,max_range)
          
    def queen_moves(self):
        max_range = 8
        position = self.position
        row = int(position[1])
        column = position[0]
        starting_column = DICT_COLUMNS[column]
        starting_row = DICT_ROWS[row]
        print('got to queen method')     
        
        self.above(starting_row, column, max_range, position)
        self.below(starting_row, column, position,max_range)
        self.left(starting_row,starting_column,max_range,position)
        self.right(starting_row, starting_column, max_range, position) 
        self.left_diagonal(row,column,starting_column,position,max_range)
        self.right_diagonal(row,column,starting_column,position,max_range)
    
    def king_moves(self):
        max_range = 1
        self.castle_check_short()
        self.castle_check_long()
        position = self.position
        row = int(position[1])
        column = position[0]
        starting_column = DICT_COLUMNS[column]
        starting_row = DICT_ROWS[row]
        self.above(starting_row, column, max_range, position)
        self.below(starting_row, column, position,max_range)
        self.left(starting_row,starting_column,max_range,position)
        self.right(starting_row, starting_column, max_range, position) 
        self.left_diagonal(row,column,starting_column,position,max_range)
        self.right_diagonal(row,column,starting_column,position,max_range)
    
    def knight_moves(self):
        
        position = self.position
        
        row = int(position[1])
        column = position[0]
        starting_column = DICT_COLUMNS[column]
        starting_row = DICT_ROWS[row]
        #self.lower_left(position, starting_column, starting_row)
        #self.lower_right(position, starting_column, starting_row)
        self.upper_left(position, starting_column, starting_row)
        self.upper_right(position, starting_column, starting_row)
        self.lower_left(position, starting_column, starting_row)
        self.lower_right(position, starting_column, starting_row)
        
    def castle_check_short(self):
        color, type1, image, position = Pieces.get_piece(self)
        if self.moved == False:
            if self.BOARD_CORDINATES.get('H1') != False:
                self.piece_white = self.BOARD_CORDINATES.get('H1')
                color1, type2, image1, position1 = Pieces.get_piece(self.piece_white)
                rook_moved = self.piece_white.moved
               
            if self.BOARD_CORDINATES.get('H8') != False:
                self.piece_black = self.BOARD_CORDINATES.get('H8')
                color2, type3, image2, position2 = Pieces.get_piece(self.piece_black)
                rook_moved_black = self.piece_black.moved
                
            if color == "white":
                if self.BOARD_CORDINATES.get('F1') == False and self.BOARD_CORDINATES.get('G1') == False \
                    and type2 == "rook" and rook_moved == False:
                    DICT_POSSIBLE_MOVES['G1'] = "G1"
                    CASTLE_DICT[color] = "Short"
            elif color == "black":
                if self.BOARD_CORDINATES.get('F8') == False and self.BOARD_CORDINATES.get('G8') == False \
                    and type3 == "rook" and rook_moved_black == False:
                    DICT_POSSIBLE_MOVES['G8'] = "G8"
                    CASTLE_DICT[color] = "Short"
                 
    def castle_check_long(self):        
        color, type1, image, position = Pieces.get_piece(self)
        if self.moved == False:
            if self.BOARD_CORDINATES.get('A1') != False:
                self.piece_white = self.BOARD_CORDINATES.get('A1')
                color1, type2, image1, position1 = Pieces.get_piece(self.piece_white)
                rook_moved = self.piece_white.moved
            if self.BOARD_CORDINATES.get('A8') != False:
                self.piece_black = self.BOARD_CORDINATES.get('A8')
                color2, type3, image2, position2 = Pieces.get_piece(self.piece_black)
                rook_moved_black = self.piece_black.moved
            
            if color == "white":
                if self.BOARD_CORDINATES.get('D1') == False and self.BOARD_CORDINATES.get('C1') == False \
                    and self.BOARD_CORDINATES.get("B1") == False and type2 == "rook" and rook_moved == False:
                    DICT_POSSIBLE_MOVES['C1'] = "C1"
                    CASTLE_DICT_LONG[color] = "Long"
            elif color == "black":
                if self.BOARD_CORDINATES.get('D8') == False and self.BOARD_CORDINATES.get('C8') == False \
                    and self.BOARD_CORDINATES.get("B8") == False and type3 == "rook" and rook_moved_black == False:
                    DICT_POSSIBLE_MOVES['C8'] = "C8"
                    CASTLE_DICT_LONG[color] = "Long"

    def upper_right(self,position,starting_column, starting_row):
        color, type, image, position = Pieces.get_piece(self)
        two_one_row = starting_row + 2
        two_one_column = DICT_COLUMNS_REVERSED.get(starting_column + 1,"z")
        two_one_string = two_one_column + str(two_one_row)
        self.check = self.BOARD_CORDINATES.get(two_one_string)
        if self.check == False:
            DICT_POSSIBLE_MOVES[two_one_string] = two_one_string
        elif self.check != None:
            color1, type1, image1, position1 = Pieces.get_piece(self.check)
                
            if color != color1:
                DICT_POSSIBLE_MOVES[two_one_string] = two_one_string
        
        one_two_row = starting_row + 1
        one_two_column = DICT_COLUMNS_REVERSED.get(starting_column +2, "z")
        one_two_string = one_two_column + str(one_two_row)
        self.check = self.BOARD_CORDINATES.get(one_two_string)
        if self.check == False:
            DICT_POSSIBLE_MOVES[one_two_string] = one_two_string
        elif self.check != None:
            color1, type1, image1, position1 = Pieces.get_piece(self.check)
                
            if color != color1:
                DICT_POSSIBLE_MOVES[one_two_string] = one_two_string
    
    def upper_left(self,position,starting_column, starting_row):
        color, type, image, position = Pieces.get_piece(self)
        two_one_row = starting_row + 2
        two_one_column = DICT_COLUMNS_REVERSED.get(starting_column - 1,"z")
        two_one_string = two_one_column + str(two_one_row)
        self.check = self.BOARD_CORDINATES.get(two_one_string)
        if self.check == False:
            DICT_POSSIBLE_MOVES[two_one_string] = two_one_string
        elif self.check != None:
            color1, type1, image1, position1 = Pieces.get_piece(self.check)  
                
            if color != color1:
                DICT_POSSIBLE_MOVES[two_one_string] = two_one_string
        
        one_two_row = starting_row + 1
        one_two_column = DICT_COLUMNS_REVERSED.get(starting_column-2, "z")
        one_two_string = one_two_column + str(one_two_row)
        
        self.check = self.BOARD_CORDINATES.get(one_two_string)
        if self.check == False:
            DICT_POSSIBLE_MOVES[one_two_string] = one_two_string
        elif self.check != None:
            color1, type1, image1, position1 = Pieces.get_piece(self.check)
                
            if color != color1:
                DICT_POSSIBLE_MOVES[one_two_string] = one_two_string
    def lower_right(self,position,starting_column, starting_row):
        color, type, image, position = Pieces.get_piece(self)
        two_one_row = starting_row - 2
        two_one_column = DICT_COLUMNS_REVERSED.get(starting_column + 1,"z")
        two_one_string = two_one_column + str(two_one_row)
        self.check = self.BOARD_CORDINATES.get(two_one_string)
        if self.check == False:
            DICT_POSSIBLE_MOVES[two_one_string] = two_one_string
        elif self.check != None:
            color1, type1, image1, position1 = Pieces.get_piece(self.check)
                
            if color != color1:
                DICT_POSSIBLE_MOVES[two_one_string] = two_one_string
        
        one_two_row = starting_row - 1
        one_two_column = DICT_COLUMNS_REVERSED.get(starting_column +2, "z")
        one_two_string = one_two_column + str(one_two_row)

        self.check = self.BOARD_CORDINATES.get(one_two_string)
        if self.check == False:
            DICT_POSSIBLE_MOVES[one_two_string] = one_two_string
        elif self.check != None:
            color1, type1, image1, position1 = Pieces.get_piece(self.check)
                
            if color != color1:
                DICT_POSSIBLE_MOVES[one_two_string] = one_two_string
    def lower_left(self,position,starting_column, starting_row):
        color, type, image, position = Pieces.get_piece(self)
        two_one_row = starting_row - 2
        two_one_column = DICT_COLUMNS_REVERSED.get(starting_column - 1,"z")
        two_one_string = two_one_column + str(two_one_row)
        self.check = self.BOARD_CORDINATES.get(two_one_string)
        if self.check == False:
            DICT_POSSIBLE_MOVES[two_one_string] = two_one_string
        elif self.check != None:
            color1, type1, image1, position1 = Pieces.get_piece(self.check)
                
            if color != color1:
                DICT_POSSIBLE_MOVES[two_one_string] = two_one_string
        
        one_two_row = starting_row - 1
        one_two_column = DICT_COLUMNS_REVERSED.get(starting_column-2, "z")
        one_two_string = one_two_column + str(one_two_row)
        self.check = self.BOARD_CORDINATES.get(one_two_string)
        if self.check == False:
            DICT_POSSIBLE_MOVES[one_two_string] = one_two_string
        elif self.check != None:
            color1, type1, image1, position1 = Pieces.get_piece(self.check)
                
            if color != color1:
                DICT_POSSIBLE_MOVES[one_two_string] = one_two_string    
    def left_diagonal(self,row, column, starting_column,position,max_range):
        row_descending = row
        row_ascending = row
        lower_column = starting_column
        upper_column = starting_column
        color, piece_type, image, position = Pieces.get_piece(self)
        while lower_column > 1 and row_descending <=8 and row_descending >1 and max_range > 0:
            if piece_type == "pawn" and color == "white":
                break
            lower_column -= 1
            row_descending -=1 
            if piece_type == "king":
                max_range -= 1
            column1 = DICT_COLUMNS_REVERSED[lower_column]
            string = column1 + str(row_descending)
            self.check = self.BOARD_CORDINATES.get(string)
            
            if self.check != False:
                color1, type1, image1, position1 = Pieces.get_piece(self.check)
                if color == color1:
                    break
                else:
                    DICT_POSSIBLE_MOVES[column1+str(row_descending)] = column1+str(row_descending)
                    break
            elif self.check == False:
                if piece_type == "pawn":
                    break
                DICT_POSSIBLE_MOVES[column1+str(row_descending)] = column1+str(row_descending)
        max_range += 1
        while upper_column > 1 and row_ascending <8 and row_ascending>=1 and max_range > 0:
            if piece_type == "pawn" and color == "black":
                break
            upper_column -= 1
            row_ascending += 1 
            if piece_type == "king":
                max_range -= 1
            column1 = DICT_COLUMNS_REVERSED[upper_column]
            string = column1 + str(row_ascending)
            self.check = self.BOARD_CORDINATES.get(string)
            
            if self.check != False:
                color1, type1, image1, position1 = Pieces.get_piece(self.check)
                if color == color1:
                    break
                else:
                    DICT_POSSIBLE_MOVES[column1+str(row_ascending)] = column1+str(row_ascending)
                    break
            elif self.check == False:
                if piece_type == "pawn":
                    break
                DICT_POSSIBLE_MOVES[column1+str(row_ascending)] = column1+str(row_ascending)
           
    def right_diagonal(self,row, column, starting_column,position,max_range):
        row_descending = row
        row_ascending = row
        lower_column = starting_column
        upper_column = starting_column
        color, piece_type, image, position = Pieces.get_piece(self)
        while lower_column < 8 and row_descending <=8 and row_descending >1 and max_range > 0:
            if piece_type == "pawn" and color == "white":
                break
            lower_column += 1
            row_descending -=1 
            if piece_type == "king":
                max_range -= 1
           
            column1 = DICT_COLUMNS_REVERSED[lower_column]
            string = column1 + str(row_descending)
            self.check = self.BOARD_CORDINATES.get(string)
            
            if self.check != False:
                color1, type1, image1, position1 = Pieces.get_piece(self.check)
                if color == color1:
                    break
                else:
                    DICT_POSSIBLE_MOVES[column1+str(row_descending)] = column1+str(row_descending)
                    break
            elif self.check == False:
                if piece_type == "pawn":
                    break
                DICT_POSSIBLE_MOVES[column1+str(row_descending)] = column1+str(row_descending)
        max_range += 1
        while upper_column < 8 and row_ascending <8 and row_descending >=1 and max_range > 0:
            if piece_type == "pawn" and color == "black":
                break
            upper_column += 1
            row_ascending += 1 
            if piece_type == "king":
                max_range -= 1
            column1 = DICT_COLUMNS_REVERSED[upper_column]
            string = column1 + str(row_ascending)
            self.check = self.BOARD_CORDINATES.get(string)
            
            if self.check != False:
                color1, type1, image1, position1 = Pieces.get_piece(self.check)
                if color == color1:
                    break
                else:
                    DICT_POSSIBLE_MOVES[column1+str(row_ascending)] = column1+str(row_ascending)
                    break
            elif self.check == False:
                if piece_type == "pawn":
                    break
                DICT_POSSIBLE_MOVES[column1+str(row_ascending)] = column1+str(row_ascending) 


    def above(self,starting_row, column, max_range,position):
        king_range = max_range
        color, piece_type, image,position = Pieces.get_piece(self)
        if piece_type == "king":
            max_range = 8
        #test, test1, test2, test3, test4
        while max_range > starting_row and king_range > 0:
            starting_row +=1
            string = str(column) + str(starting_row)
            king_range -= 1
            self.check = self.BOARD_CORDINATES.get(string)
            if self.check != False:
                color1, type1, image1, position1 = Pieces.get_piece(self.check)
                if color == color1: 
                    break
                else:
                  DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
                  break  
            elif self.check == False:
                DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
    def below(self,starting_row,column, position,max_range):
        king_range = max_range
        color, type_piece, image, position = Pieces.get_piece(self)
        while starting_row > 1 and king_range > 0:
            starting_row -= 1
            king_range -= 1
            string = column + str(starting_row)
           
            self.check = self.BOARD_CORDINATES.get(string)
           
            #color1, type1, image1, position1 = Pieces.get_piece(self.check)
            if self.check != False:
                color1, type1, image1, position1 = Pieces.get_piece(self.check)
                if color == color1: 
                    break
                else:
                    DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
                    break  
            
            else:
                DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
    def left(self,starting_row, starting_column, max_range, position):
        king_range = max_range
        color, type, image, position = Pieces.get_piece(self)
        while starting_column > 1 and king_range > 0:
            starting_column -=1
            king_range -=1
            column = DICT_COLUMNS_REVERSED[starting_column]
            string = column + str(starting_row)
            self.check = self.BOARD_CORDINATES.get(string)
            if self.check != False:
                color1, type1, image1, position1 = Pieces.get_piece(self.check)
                if color == color1: 
                    break
                else:
                    DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
                    break  
            
            else:
                DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
            # if self.BOARD_CORDINATES.get(column+str(starting_row)) != False:
            #     break
            # else:
            #     DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
    def right(self,starting_row, starting_column, max_range, position):
        king_range = max_range
        color, type, image, position = Pieces.get_piece(self)
        while starting_column <8 and king_range >0:
            starting_column += 1
            king_range -= 1
            column = DICT_COLUMNS_REVERSED[starting_column]
            column = DICT_COLUMNS_REVERSED[starting_column]
            string = column + str(starting_row)
            self.check = self.BOARD_CORDINATES.get(string)
            if self.check != False:
                color1, type1, image1, position1 = Pieces.get_piece(self.check)
                if color == color1: 
                    break
                else:
                    DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
                    break  
            
            else:
                DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
            # if self.BOARD_CORDINATES.get(column+str(starting_row)) != False:
            #     break
            # else:
            #     DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
    def kill_piece(self):
        self.BOARD_CORDINATES[self.position] = False
        self.position = False
        self.destroyed = True

        piece = self.name
        print(self.name,"name check")
        white = white_piece_dict.pop(piece,"none")
        black = black_piece_dict.pop(piece,"none")
        print(black,white)
        
# def create_pieces():
#     total = 0
#     for item in PIECE_DICTIONARY:
#         list = PIECE_DICTIONARY[item]
#         for i in range(list[3]):
#             piece = Pieces(list[0],list[1],list[2])
            
#             total += 1
#             DICT_PIECES[item+str(i+1)] = piece
#             DICT_PIECE_REVERSE[piece] = item + str(i+1)
#             img = chessboard.tk.PhotoImage(file=list[2])
#             board.create_image(100,100, image=img)
            
# def create_board_cordinates():
#     letters =['A','B','C','D','E','F','G','H']    
#     for letter in letters:
#         for i in range(1,9):
#             BOARD_CORDINATES[letter+str(i)] = None
#     print(BOARD_CORDINATES)
# def reverse_piece_cord():
#     REVERSED_DICTIONARY = {value : key for (key, value) in BOARD_CORDINATES.items()}
#     print(REVERSED_DICTIONARY)
       

def populate_board():
    for item in DICT_PIECES:
        value = DICT_PIECES[item]
        value.set_position(value,item)
           
def create_cordinates():
     print('here')
     letters =['A','B','C','D','E','F','G','H'] 
     dict_test = {}
     x = 50
     y = 750
     for letter in letters:
        for i in range(1,9):
            dict_test[letter + str(i)] = [x,y]
            y -= 100
        y = 750
        x += 100
     print(dict_test)

def main():
 
     instance = chessboard.Chess_GUI()  
        
     chessboard.tkinter.mainloop()
     
if __name__ == "__main__":    
    main()
        
