from itertools import count
import sys
#import pygame



class Pieces:
    PIECE_DICTIONARY = {'wp': ['white', 'pawn', 'path',8],  'wn': ['white', 'knight','path',2], 'wb': ['white', 'bishop','path',2], 'wr': ['white', 'rook','path',2], 'wq': ['white', 'queen','path',1], 'wk': ['white', 'king','path',1], \
    'bp': ['black','pawn','path',8], 'bn': ['black', 'knight','path',2], 'bb': ['black', 'bishop','path',2], 'br': ['black', 'rook','path',2], 'bq': ['black', 'queen','path',1], 'bk': ['black', 'king','path',1]}
    DICT_PIECES = {}
    def __init__(self, color, type, image, destroy = False, kill = False):
        self.color = color
        self.type = type
        self.image = image
        self.destroy = destroy
        self.kill = kill
    
        
    

    def create_pieces():
        total = 0
        for item in Pieces.PIECE_DICTIONARY:
            list = Pieces.PIECE_DICTIONARY[item]
            for i in range(list[3]):
                piece = Pieces(list[0],list[1],list[2])
                print(item)
                total += 1
                Pieces.DICT_PIECES[item+str(i+1)] = piece
        print(total)   
        print(Pieces.DICT_PIECES)

def main():
    Pieces.create_pieces()

main()
        
