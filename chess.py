
import sys
from turtle import position
#import pygame
DICT_PIECES = {}
PIECE_DICTIONARY = {'wp': ['white', 'pawn', 'path',8],  'wn': ['white', 'knight','path',2], 'wb': ['white', 'bishop','path',2], 'wr': ['white', 'rook','path',2], 'wq': ['white', 'queen','path',1], 'wk': ['white', 'king','path',1], \
    'bp': ['black','pawn','path',8], 'bn': ['black', 'knight','path',2], 'bb': ['black', 'bishop','path',2], 'br': ['black', 'rook','path',2], 'bq': ['black', 'queen','path',1], 'bk': ['black', 'king','path',1]}
BOARD_CORDINATES = {'A1': 'wr1', 'A2': 'wp1', 'A3': None , 'A4': None, 'A5': None, 'A6': None, 'A7': 'bp1', 'A8': 'br1', 'B1': 'wn1', 'B2': 'wp2' , 'B3': None, 'B4': None, 'B5': None, 'B6': None, 'B7': 'bp2', 'B8': 'bn1', 'C1': 'wb1', 'C2': 'wp3', 
 'C3': None, 'C4': None, 'C5': None, 'C6': None, 'C7': 'bp3', 'C8': 'bb1', 'D1': "wq1", 'D2': 'wp4', 'D3': None, 'D4': None, 'D5': None, 'D6': None, 'D7': 'bp4', 'D8': 'bq1', 'E1': 'wk1', 'E2': 'wp5', 'E3': None, 'E4': None, 'E5': None, 'E6': None, 
 'E7': 'bp5', 'E8': 'bk1', 'F1': 'wb2', 'F2': 'wp6', 'F3': None, 'F4': None, 'F5': None, 'F6': None, 'F7': 'bp6', 'F8': 'bb2', 'G1': 'wn2', 'G2': 'wp7', 'G3': None, 'G4': None, 'G5': None, 'G6': None, 'G7': 'bp7', 'G8': 'bn2', 'H1': 'wr2', 'H2': 'wp8', 
 'H3': None, 'H4': None, 'H5': None, 'H6': None, 'H7': 'bp8', 'H8': 'br2'}
POSITION_START = {'wr1': 'A1', 'wp1': 'A2', 'bp1': 'A7', 'br1': 'A8', 'wn1': 'B1', 'wp2': 'B2', 'bp2': 'B7', 'bn1': 'B8', 'wb1': 'C1', 'wp3': 'C2', 'bp3': 'C7', 'bb1': 'C8', 'wq1': 'D1', 'wp4': 'D2', 'bp4': 'D7', 'bq1': 'D8', 
'wk1': 'E1', 'wp5': 'E2', 'bp5': 'E7', 'bk1': 'E8', 'wb2': 'F1', 'wp6': 'F2', 'bp6': 'F7', 'bb2': 'F8', 'wn2': 'G1', 'wp7': 'G2', 'bp7': 'G7', 'bn2': 'G8', 'wr2': 'H1', 'wp8': 'H2', 'bp8': 'H7', 'br2': 'H8'}
class Pieces:
   
    
    def __init__(self, color, type, image, position = None, destroy = False, kill = False):
        self.color = color
        self.type = type
        self.image = image
        self.destroy = destroy
        self.position = position
        self.kill = kill
    #accessor
    def get_piece(self):
        return (self.color,self.type,self.image, self.position)
    def set_position(self, item,key):
        piece = Pieces.get_piece(item)
        self.position = POSITION_START[key]
        

def kill_piece(piece):
    print(piece)
    
    DICT_PIECES.pop(piece)
    #test = Pieces.DICT_PIECES[piece]
    #print('test',delete)
    
    print(DICT_PIECES)
   

def create_pieces():
    total = 0
    for item in PIECE_DICTIONARY:
        list = PIECE_DICTIONARY[item]
        for i in range(list[3]):
            piece = Pieces(list[0],list[1],list[2])
            
            total += 1
            DICT_PIECES[item+str(i+1)] = piece
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
    
    
main()
        
