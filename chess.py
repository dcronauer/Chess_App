
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
PIECE_DICTIONARY = {'wp': ['white', 'pawn', 'images/white_p.png',8],  'wn': ['white', 'knight','images/white_n.png',2], 'wb': ['white', 'bishop','images/white_b.png',2], 'wr': ['white', 'rook','images/white_r.png',2], 'wq': ['white', 'queen','images/white_q.png',1], 'wk': ['white', 'king','images/white_k.png',1], \
    'bp': ['black','pawn','images/black_p.png',8], 'bn': ['black', 'knight','images/black_n.png',2], 'bb': ['black', 'bishop','images/black_b.png',2], 'br': ['black', 'rook','images/black_r.png',2], 'bq': ['black', 'queen','images/black_q.png',1], 'bk': ['black', 'king','images/black_k.png',1]}

#  BOARD_CORDINATES = {'A1': 'wr1', 'A2': 'wp1', 'A3': None , 'A4': None, 'A5': None, 'A6': None, 'A7': 'bp1', 'A8': 'br1', 'B1': 'wn1', 'B2': 'wp2' , 'B3': None, 'B4': None, 'B5': None, 'B6': None, 'B7': 'bp2', 'B8': 'bn1', 'C1': 'wb1', 'C2': 'wp3', 
#  'C3': None, 'C4': None, 'C5': None, 'C6': None, 'C7': 'bp3', 'C8': 'bb1', 'D1': "wq1", 'D2': 'wp4', 'D3': None, 'D4': None, 'D5': None, 'D6': None, 'D7': 'bp4', 'D8': 'bq1', 'E1': 'wk1', 'E2': 'wp5', 'E3': None, 'E4': None, 'E5': None, 'E6': None, 
#  'E7': 'bp5', 'E8': 'bk1', 'F1': 'wb2', 'F2': 'wp6', 'F3': None, 'F4': None, 'F5': None, 'F6': None, 'F7': 'bp6', 'F8': 'bb2', 'G1': 'wn2', 'G2': 'wp7', 'G3': None, 'G4': None, 'G5': None, 'G6': None, 'G7': 'bp7', 'G8': 'bn2', 'H1': 'wr2', 'H2': 'wp8', 
#  'H3': None, 'H4': None, 'H5': None, 'H6': None, 'H7': 'bp8', 'H8': 'br2'}
POSITION_START = {'wr1': 'A1', 'wp1': 'A2', 'bp1': 'A7', 'br1': 'A8', 'wn1': 'B1', 'wp2': 'B2', 'bp2': 'B7', 'bn1': 'B8', 'wb1': 'C1', 'wp3': 'C2', 'bp3': 'C7', 'bb1': 'C8', 'wq1': 'D1', 'wp4': 'D2', 'bp4': 'D7', 'bq1': 'D8', 
'wk1': 'E1', 'wp5': 'E2', 'bp5': 'E7', 'bk1': 'E8', 'wb2': 'F1', 'wp6': 'F2', 'bp6': 'F7', 'bb2': 'F8', 'wn2': 'G1', 'wp7': 'G2', 'bp7': 'G7', 'bn2': 'G8', 'wr2': 'H1', 'wp8': 'H2', 'bp8': 'H7', 'br2': 'H8'}
POSITION_CENTER = {'A1': [50, 750], 'A2': [50, 650], 'A3': [50, 550], 'A4': [50, 450], 'A5': [50, 350], 'A6': [50, 250], 'A7': [50, 150], 'A8': [50, 50], 'B1': [150, 750], 'B2': [150, 650], 'B3': [150, 550], 'B4': [150, 450], 'B5': [150, 350], 'B6': [150, 250], 'B7': [150, 150], 'B8': [150, 50], 'C1': [250, 750], 'C2': [250, 650], 'C3': [250, 550], 'C4': [250, 450], 'C5': [250, 350], 'C6': [250, 250], 'C7': [250, 150], 'C8': [250, 50], 'D1': [350, 750], 'D2': [350, 650], 'D3': [350, 550], 'D4': [350, 450], 'D5': [350, 350], 'D6': [350, 250], 'D7': [350, 150], 'D8': [350, 50], 'E1': [450, 750], 'E2': [450, 650], 'E3': [450, 550], 'E4': [450, 450], 'E5': [450, 350], 'E6': [450, 250], 'E7': [450, 150], 'E8': [450, 50], 'F1': [550, 750], 'F2': [550, 650], 'F3': [550, 550], 'F4': [550, 450], 'F5': [550, 350], 'F6': [550, 250], 'F7': [550, 150], 'F8': [550, 50], 'G1': [650, 750], 'G2': [650, 650], 'G3': [650, 550], 'G4': [650, 450], 'G5': [650, 350], 'G6': [650, 250], 'G7': [650, 150], 'G8': [650, 50], 'H1': [750, 750], 'H2': [750, 650], 'H3': [750, 550], 'H4': [750, 450], 'H5': [750, 350], 'H6': [750, 250], 'H7': [750, 150], 'H8': [750, 50]}

class Pieces:
    BOARD_CORDINATES = {'A1': False, 'A2': False, 'A3': False , 'A4': False, 'A5': False, 'A6': False, 'A7': False, 'A8': False, 'B1': False, 'B2': False , 'B3': False, 'B4': False, 'B5': False, 'B6': False, 'B7': False, 'B8': False, 'C1': False, 'C2': False, 
 'C3': False, 'C4': False, 'C5': False, 'C6': False, 'C7': False, 'C8': False, 'D1': False, 'D2': False, 'D3': False, 'D4': False, 'D5': False, 'D6': False, 'D7': False, 'D8': False, 'E1': False, 'E2': False, 'E3': False, 'E4': False, 'E5': False, 'E6': False, 
 'E7': False, 'E8': False, 'F1': False, 'F2': False, 'F3': False, 'F4': False, 'F5': False, 'F6': False, 'F7': False, 'F8': False, 'G1': False, 'G2': False, 'G3': False, 'G4': False, 'G5': False, 'G6': False, 'G7': False, 'G8': False, 'H1': False, 'H2': False, 
 'H3': False, 'H4': False, 'H5': False, 'H6': False, 'H7': False, 'H8': False}
    def __init__(self, color, type, image, position = None, destroyed = False, kill = False, moved = False,cordinates=None, id=None):
        self.color = color
        self.type = type
        self.image = image
        self.destroy = destroyed
        self.position = position
        self.kill = kill
        self.moved = moved
        self.cordinates = cordinates
        self.id = id
    
    #accessor
    def get_piece(self):
        return (self.color,self.type,self.image, self.position)
    
    def get_id(self):
        return self.id, self
    def get_color(self):
        return self.color
    
    #mutator
    def set_position(self):
        block = DICT_PIECE_REVERSE[self]
        self.position = POSITION_START[block]
        self.BOARD_CORDINATES[self.position] = self
    
    def set_move_position(self,position_id):
        print(self.position,"before change")
        self.BOARD_CORDINATES[self.position] = False
        self.position = position_id
        print(self.position)

        self.BOARD_CORDINATES[self.position] = self
        print(self.BOARD_CORDINATES)
    def set_move(self):
        self.moved = True
        print("moved is true")

    def set_id(self,id):
        self.id = id 

    def rook_moves(self):
        position = self.position
        max_range = 8
        row = int(position[1])
        column = position[0]
        starting_row = DICT_ROWS[row]
        starting_column = DICT_COLUMNS[column]
        self.above(starting_row, column, max_range, position)
        self.below(starting_row, column, position)
        self.left(starting_row,starting_column,max_range,position)
        self.right(starting_row, starting_column, max_range, position)   
        print(DICT_POSSIBLE_MOVES)
        
        
       
    def kill_piece(self):
        self.BOARD_CORDINATES[self.position]
        self.position = False
        self.destroyed = True
    def pawn_moves(self):
        if self.moved == False:
            max_range = 2
        else:
            max_range =1
        position = self.position
        row = int(position[1])
        column = position[0]
        for i in range(max_range):
            row += 1
            DICT_POSSIBLE_MOVES[column+str(row)] = column +str(row)
        print(DICT_POSSIBLE_MOVES)
            

    def above(self,starting_row, column, max_range,position):
        color, piece_type, image, position = Pieces.get_piece(self)
        print(color,piece_type)
        #test, test1, test2, test3, test4
        while max_range > starting_row:
            starting_row +=1
            string = str(column) + str(starting_row)
            print(string,"string")
            
            self.check = self.BOARD_CORDINATES.get(string)
            print(self.check)
        
            
            
            if self.check != False:
                color1, type1, image1, position1 = Pieces.get_piece(self.check)
                print(color1,'check!= loop')
                if color == color1: 
                    break
                else:
                  print("we got to adding black piece")
                  DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
                  break  
            elif self.check == False:
                DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
    def below(self,starting_row,column, position):
        color, type_piece, image, position = Pieces.get_piece(self)
        print(color)
        while starting_row > 1:
            starting_row -= 1
            string = column + str(starting_row)
            print(string,"string")
           
            self.check = self.BOARD_CORDINATES.get(string)
           
            #color1, type1, image1, position1 = Pieces.get_piece(self.check)
            if self.check != False:
                color1, type1, image1, position1 = Pieces.get_piece(self.check)
                print(color1)
                if color == color1: 
                    break
                else:
                    print('we got to adding black piece')
                    DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
                    break  
            
            else:
                DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
    def left(self,starting_row, starting_column, max_range, position):
        color, type, image, position = Pieces.get_piece(self)
        print(color)
        while starting_column > 1:
            starting_column -=1
            
            column = DICT_COLUMNS_REVERSED[starting_column]
            if self.BOARD_CORDINATES.get(column+str(starting_row)) != False:
                break
            else:
                DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)
    def right(self,starting_row, starting_column, max_range, position):
        color, type, image, position = Pieces.get_piece(self)
        print(color)
        while starting_column <8:
            starting_column += 1
            
            column = DICT_COLUMNS_REVERSED[starting_column]
            if self.BOARD_CORDINATES.get(column+str(starting_row)) != False:
                break
            else:
                DICT_POSSIBLE_MOVES[column+str(starting_row)] = column+str(starting_row)

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
#             chessboard.Chess_GUI.board.create_image(100,100, image=img)
            
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
        
