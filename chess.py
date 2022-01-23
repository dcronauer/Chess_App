
import sys
from turtle import position
#import pygame
DICT_COLUMNS = {'A': 1,'B': 2,'C': 3,'D': 4,'E': 5,'F': 6,'G': 7, 'H': 8}
DICT_ROWS = {1: 1,2: 2,3: 3,4: 4,5: 5,6: 6,7: 7,8: 8}
DICT_COLUMNS_REVERSED = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
DICT_POSSIBLE_MOVES = {}
DICT_PIECES = {}
DICT_PIECE_REVERSE = {}
PIECE_DICTIONARY = {'wp': ['white', 'pawn', 'path',8],  'wn': ['white', 'knight','path',2], 'wb': ['white', 'bishop','path',2], 'wr': ['white', 'rook','path',2], 'wq': ['white', 'queen','path',1], 'wk': ['white', 'king','path',1], \
    'bp': ['black','pawn','path',8], 'bn': ['black', 'knight','path',2], 'bb': ['black', 'bishop','path',2], 'br': ['black', 'rook','path',2], 'bq': ['black', 'queen','path',1], 'bk': ['black', 'king','path',1]}
BOARD_CORDINATES = {'A1': None, 'A2': None, 'A3': None , 'A4': None, 'A5': None, 'A6': None, 'A7': None, 'A8': None, 'B1': None, 'B2': None , 'B3': None, 'B4': None, 'B5': None, 'B6': None, 'B7': None, 'B8': None, 'C1': None, 'C2': None, 
 'C3': None, 'C4': None, 'C5': None, 'C6': None, 'C7': None, 'C8': None, 'D1': None, 'D2': None, 'D3': None, 'D4': None, 'D5': None, 'D6': None, 'D7': None, 'D8': None, 'E1': None, 'E2': None, 'E3': None, 'E4': None, 'E5': None, 'E6': None, 
 'E7': None, 'E8': None, 'F1': None, 'F2': None, 'F3': None, 'F4': None, 'F5': None, 'F6': None, 'F7': None, 'F8': None, 'G1': None, 'G2': None, 'G3': None, 'G4': None, 'G5': None, 'G6': None, 'G7': None, 'G8': None, 'H1': None, 'H2': None, 
 'H3': None, 'H4': None, 'H5': None, 'H6': None, 'H7': None, 'H8': None}
#  BOARD_CORDINATES = {'A1': 'wr1', 'A2': 'wp1', 'A3': None , 'A4': None, 'A5': None, 'A6': None, 'A7': 'bp1', 'A8': 'br1', 'B1': 'wn1', 'B2': 'wp2' , 'B3': None, 'B4': None, 'B5': None, 'B6': None, 'B7': 'bp2', 'B8': 'bn1', 'C1': 'wb1', 'C2': 'wp3', 
#  'C3': None, 'C4': None, 'C5': None, 'C6': None, 'C7': 'bp3', 'C8': 'bb1', 'D1': "wq1", 'D2': 'wp4', 'D3': None, 'D4': None, 'D5': None, 'D6': None, 'D7': 'bp4', 'D8': 'bq1', 'E1': 'wk1', 'E2': 'wp5', 'E3': None, 'E4': None, 'E5': None, 'E6': None, 
#  'E7': 'bp5', 'E8': 'bk1', 'F1': 'wb2', 'F2': 'wp6', 'F3': None, 'F4': None, 'F5': None, 'F6': None, 'F7': 'bp6', 'F8': 'bb2', 'G1': 'wn2', 'G2': 'wp7', 'G3': None, 'G4': None, 'G5': None, 'G6': None, 'G7': 'bp7', 'G8': 'bn2', 'H1': 'wr2', 'H2': 'wp8', 
#  'H3': None, 'H4': None, 'H5': None, 'H6': None, 'H7': 'bp8', 'H8': 'br2'}
POSITION_START = {'wr1': 'A1', 'wp1': 'A2', 'bp1': 'A7', 'br1': 'A8', 'wn1': 'B1', 'wp2': 'B2', 'bp2': 'B7', 'bn1': 'B8', 'wb1': 'C1', 'wp3': 'C2', 'bp3': 'C7', 'bb1': 'C8', 'wq1': 'D1', 'wp4': 'D2', 'bp4': 'D7', 'bq1': 'D8', 
'wk1': 'E1', 'wp5': 'E2', 'bp5': 'E7', 'bk1': 'E8', 'wb2': 'F1', 'wp6': 'F2', 'bp6': 'F7', 'bb2': 'F8', 'wn2': 'G1', 'wp7': 'G2', 'bp7': 'G7', 'bn2': 'G8', 'wr2': 'H1', 'wp8': 'H2', 'bp8': 'H7', 'br2': 'H8'}
class Pieces:
   
    
    def __init__(self, color, type, image, position = None, destroyed = False, kill = False, moved = False):
        self.color = color
        self.type = type
        self.image = image
        self.destroy = destroyed
        self.position = position
        self.kill = kill
        self.moved = moved
    #accessor
    def get_piece(self):
        return (self.color,self.type,self.image, self.position)
    def set_position(self, item,key):
        piece = Pieces.get_piece(item)
        self.position = POSITION_START[key]
        BOARD_CORDINATES[self.position] = self
    def rook_moves(self,position):
        max_range = 8
        row = int(position[1])
        column = position[0]
        starting_row = DICT_ROWS[row]
        starting_column = DICT_COLUMNS[column]
        above(starting_row, column, max_range, position)
        below(starting_row, column, position)
        left(starting_row,starting_column,max_range,position)
        right(starting_row, starting_column, max_range, position)   
        print(DICT_POSSIBLE_MOVES)
        
        #part that moves the piece have to take current position and make none. Then set new position and set board cordinates with new position for piece
        BOARD_CORDINATES[self.position] = None
        self.position = 'A5'
        BOARD_CORDINATES[self.position] = self
    def kill_piece(self):
        BOARD_CORDINATES[self.position]
        self.position = None
        self.destroyed = True

        

           
        
        


    
def above(starting_row, column, max_range,position):
    while max_range > starting_row:
        starting_row +=1
        DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)  
def below(starting_row,column, position):
    while starting_row > 1:
        starting_row -= 1
        DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
def left(starting_row, starting_column, max_range, position):
    while starting_column > 1:
        starting_column -=1
        column = DICT_COLUMNS_REVERSED[starting_column]
        DICT_POSSIBLE_MOVES[column +str(starting_row)] = column+str(starting_row)
def right(starting_row, starting_column, max_range, position):
    while starting_column <8:
        starting_column += 1
        column = DICT_COLUMNS_REVERSED[starting_column]
        DICT_POSSIBLE_MOVES[column +str(starting_row)] = column+str(starting_row)

def create_pieces():
    total = 0
    for item in PIECE_DICTIONARY:
        list = PIECE_DICTIONARY[item]
        for i in range(list[3]):
            piece = Pieces(list[0],list[1],list[2])
            
            total += 1
            DICT_PIECES[item+str(i+1)] = piece
            DICT_PIECE_REVERSE[piece] = item + str(i+1)
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
    
        



                
       

def main():
    create_pieces()
    populate_board()
    print(DICT_PIECES)
    print(DICT_PIECE_REVERSE)
    position = POSITION_START['br1']
    rook = DICT_PIECES["br1"]
    result = rook.get_piece()
    print(result)  
    rook.rook_moves(position)
    result = rook.get_piece()
    print(result)  
    #kill_piece(rook)
if __name__ == "__main__":    
    main()
        
