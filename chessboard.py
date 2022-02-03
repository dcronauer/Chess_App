
from multiprocessing.dummy import Event
from chess import *
from PIL import ImageTk, Image
import tkinter
from tkinter import Tk, ttk

def main():
    print("wea are here")
    #start gui
    player1 = "white"
    player2 = "black"
    turn = "white"
    myboard = Chess_GUI(player1, player2, turn)
    # set up main loop
    tkinter.mainloop()



class Chess_GUI:
    images = {}
    ids = {}
    player_turn = {}
    array_rows = [1,2,3,4,5,6,7,8]
    position_initial = []
    
    def __init__(self,player1, player2,turn):
        self.player1 = player1
        self.player2 = player2
        self.turn = turn
        self.main_window = tkinter.Tk()          
        self.main_window.geometry("800x850")
        self.main_window.title('Chess App')
        self.main_window.minsize(800,800)
        self.create_canvas()
        self.set_player_turn(self.player1, self.player2, turn)

        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.board.tag_bind("blackpiece","<ButtonPress-1>", self.select_piece)
        self.board.tag_bind("blackpiece", "<ButtonRelease-1>", self.drag_stop)
        self.board.tag_bind("blackpiece", "<B1-Motion>", self.drag)
        self.board.tag_bind("whitepiece","<ButtonPress-1>", self.select_piece)
        self.board.tag_bind("whitepiece", "<ButtonRelease-1>", self.drag_stop)
        self.board.tag_bind("whitepiece", "<B1-Motion>",  self.drag)

    def set_player_turn(self, player1, player2,turn):
        if player1 == "white":
            self.player_turn[0] = "whitepiece"
        else:
            self.player_turn[0] = "blackpiece"
        print(self.player_turn) 
        


    def select_piece(self,event):
        print(DICT_POSSIBLE_MOVES)
        self._drag_data["item"] = self.board.find_closest(event.x,event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        result = self._drag_data.get("item")
        print(result, 'this is the result')
        tags_return = self.board.gettags(result)
        piece_check = tags_return[0]
        print(tags_return[0])
        if piece_check != self.player_turn.get(0):
            print('we got to the test stage')
            return
        #print(tags_return, 'these are the tag returns')
        self.piece = self.ids[self._drag_data.get("item")]
        
        self.position_initial.append(self._drag_data["x"])
        self.position_initial.append(self._drag_data["y"])
        print(self.position_initial)
        
        color, type1, image, position = Pieces.get_piece(self.piece)
        print("grabbed",self._drag_data.get("item"),type1)
        if type1 == "pawn":
            self.piece.pawn_moves()
        elif type1 == "rook":
            self.piece.rook_moves()
        elif type1 == "bishop":
            self.piece.bishop_moves()
        elif type1 == "queen":
            self.piece.queen_moves()
        elif type1 == "king":
            self.piece.king_moves()
        elif type1 == "knight":
            self.piece.knight_moves()
        print(DICT_POSSIBLE_MOVES)
    def drag_stop(self, event):
        
        column_dict = { 0: 'A', 1: 'B', 2: 'C',3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
        row_dict = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
        
        self.piece = self.ids[self._drag_data.get("item")]
        self.id_image = self._drag_data.get("item")
        #print(self.position_initial,'initial cord result')
        
        
        print(self.ids)
        color, type, image, position = Pieces.get_piece(self.piece)
        print(position)
        initial_position = POSITION_CENTER[position]
        print(initial_position)
        moves = DICT_POSSIBLE_MOVES
       
        row = self._drag_data.get('y')
        column = self._drag_data.get('x')
        cords_dropped = self.board.coords(self.id_image)
        print(cords_dropped,"dropped cords")
        #print(row,column)
        row_int =int(row/100)
        column_int = int(column/100)
        #print(row_int,column_int)
        row_id = row_dict[row_int]
        column_id = column_dict[column_int]
        position_id = str(column_id) + str(row_id)
        print(position_id, 'this is the position id')
        snap_position_list = POSITION_CENTER[position_id]
        #print(snap_position_list)
        if position_id in DICT_POSSIBLE_MOVES:
            dict_board = Pieces.get_board_cord(Pieces)
            self.check = dict_board.get(position_id)
            castle_status_long = CASTLE_DICT_LONG.get(color)
            castle_status_short = CASTLE_DICT.get(color)
            print(castle_status_short, castle_status_long)
            if type == "king" and castle_status_short == "Short" and (position_id == "G1" or position_id == "G8"):
                if color == "white":
                    print("got to position if statement white")
                    
                    self.rook = Pieces.BOARD_CORDINATES.get('H1')
                    color_rook, type4, image4, position4 = Pieces.get_piece(self.rook)
                    print(color_rook, type4)
                    rook_id =Pieces.get_id(self.rook)
                    print(rook_id)
                    print(self.id_image, "just added check")
                    
                    
                    self.piece.set_move_position(position_id)
                    self.board.coords(self.id_image,snap_position_list[0],snap_position_list[1])
                    self.piece.set_move()
                    self.rook.set_move_position("F1")
                    self.board.coords(rook_id[0],550,750)
                    self.rook.set_move()
                elif color == "black":
                    self.rook = Pieces.BOARD_CORDINATES.get('H8')
                    color_rook, type4, image4, position4 = Pieces.get_piece(self.rook)
                    print(color_rook, type4)
                    rook_id =Pieces.get_id(self.rook)
                    print(rook_id)
                    print(self.id_image, "just added check")
                    
                    
                    self.piece.set_move_position(position_id)
                    self.board.coords(self.id_image,snap_position_list[0],snap_position_list[1])
                    self.piece.set_move()
                    self.rook.set_move_position("F8")
                    self.board.coords(rook_id[0],550,50)
                    self.rook.set_move()
            if type == "king" and castle_status_long == "Long" and (position_id == "C1" or position_id == "C8"):    
                if color == "white":
                    print("got to position if statement white")
                    
                    self.rook = Pieces.BOARD_CORDINATES.get('A1')
                    color_rook, type4, image4, position4 = Pieces.get_piece(self.rook)
                    print(color_rook, type4)
                    rook_id =Pieces.get_id(self.rook)
                    print(rook_id)
                    print(self.id_image, "just added check")
                    
                    
                    self.piece.set_move_position(position_id)
                    self.board.coords(self.id_image,snap_position_list[0],snap_position_list[1])
                    self.piece.set_move()
                    self.rook.set_move_position("D1")
                    self.board.coords(rook_id[0],350,750)
                    self.rook.set_move()
                elif color == "black":
                    self.rook = Pieces.BOARD_CORDINATES.get('A8')
                    color_rook, type4, image4, position4 = Pieces.get_piece(self.rook)
                    print(color_rook, type4)
                    rook_id =Pieces.get_id(self.rook)
                    print(rook_id)
                    print(self.id_image, "just added check")
                    
                    
                    self.piece.set_move_position(position_id)
                    self.board.coords(self.id_image,snap_position_list[0],snap_position_list[1])
                    self.piece.set_move()
                    self.rook.set_move_position("F8")
                    self.board.coords(rook_id[0],350,50)
                    self.rook.set_move()    
                

            
            
            if self.check != False:
                
                color1, type1, image1, position1 = Pieces.get_piece(self.check)
                #piece to die currently in spot that opposing piece could take
                self.id_image2, piece = self.check.get_id()
                print(self.id_image2)
                self.ids.pop(self.id_image2)
                self.images.pop(piece)
                self.board.delete(self.id_image2)
                Pieces.kill_piece(piece)


            self.piece.set_move_position(position_id)
            self.board.coords(self.id_image,snap_position_list[0],snap_position_list[1])
            self.piece.set_move()
            
            if self.player_turn.get(0) == "whitepiece":
                self.player_turn[0] = "blackpiece"
            else:
                self.player_turn[0] = "whitepiece"
            print(self.player_turn[0])
            
        else:
            #self.board.move(self.image,row, column)
            self.board.coords(self.id_image,initial_position)
            self.piece.set_move_position(position)
            
           
        print(self.board.coords(self.id_image),'cord result final')
        row_pawn = Pieces.get_row(self.piece)
        print(row_pawn, "row_pawn")
        print(type)
        if type == "pawn" and (row_pawn == "8" or row_pawn == "1"):
                print("got inside promote if")
                self.promote_pawn(self.piece)

        DICT_POSSIBLE_MOVES.clear()
        self.position_initial.clear()
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0
        CASTLE_DICT["black"] = False
        CASTLE_DICT["white"] = False
        CASTLE_DICT_LONG["black"] = False
        CASTLE_DICT_LONG["white"] = False
        print(self.player_turn[0])
    def drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.board.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def promote_pawn(self,promote_piece):
        print('got to promote pawn')
        color1, type1, image1, position1 = Pieces.get_piece(promote_piece)
        #piece to die currently in spot that opposing piece could take
        self.id_image, piece = Pieces.get_id(promote_piece)
        print(self.id_image)
        self.ids.pop(self.id_image)
        self.images.pop(piece)
        self.board.delete(self.id_image)
        Pieces.kill_piece(piece)
        print(Pieces.BOARD_CORDINATES)


    def create_canvas(self):
        
        x = 0
        y = 0
        width = 100
        height = 100
        # self.main_window.grid_columnconfigure(0,weight=1)
        # self.main_window.grid_rowconfigure(0,weight=1)
        # self.main_window.grid_rowconfigure(1,weight=1)

        self.board_frame = ttk.Frame(self.main_window)
        self.board_frame.pack(side="top")
        self.frame = ttk.Frame(self.main_window)
        self.frame.pack(side="bottom")
        self.my_label = ttk.Label(self.frame, text="")
        self.my_label.pack()
        # self.board_frame.grid(row=0,column=0,sticky="nsew")
       
        # self.board_frame.grid_rowconfigure(0,weight=1)
        # self.board_frame.grid_columnconfigure(0,weight=1)
        
        # self.frame2 = ttk.Frame(self.main_window)
        # self.frame2.grid(row=1,column=0, sticky="nsew")
        # self.frame2.grid_rowconfigure(1,weight=1)
        # self.frame2.grid_columnconfigure(0,weight=1)
        
        
        #self.rect = self.board.Canvas.create_rectangle(0,0,100,100,fill="red")
        self.board = tkinter.Canvas(self.main_window, bg = "grey",width=800,height=800)
        #self.board.grid(column=0,row=0, sticky="nsew")
        self.board.pack()
        
        
       
        for i in self.array_rows:
            
            if i % 2 != 0:
                #print(i,x,y,height,width)
                x,y, height,width = self.draw_squares(x,y,height,width,i)
                
                #print(i,x,y,height,width)
            elif i % 2 == 0:
                
                x = 100
                width = 200
                #print(i,x,y,height,width)
                x,y, height,width = self.draw_squares(x,y,height,width,i)
                #print(i,x,y,height,width)
        self.create_pieces()        
    
    def draw_squares(self,x,y,height,width,l):
        
        for i in range(4):
            
            self.board.create_rectangle(x,y,width,height,fill="red")
            
            x += 200
            width +=200
        if l % 2 != 0: 
            x = 100
            width = 200
        elif l % 2 == 0:
            x = 0
            width = 100

        for i in range(4):
            self.board.create_rectangle(x,y,width,height,fill="black")
            x += 200
            width += 200
        
        
        x = 0
        width = 100
        y += 100
        height += 100

        return x, y, height, width   
    def create_piece_promote(self,item):
        piece = Pieces(list[0],list[1],list[2])
        color1, type1, image1, position1 = Pieces.get_piece(piece)
        if type1 == "pawn" and color1 =="black":
            piece.starting_row = 7
        elif type1 == "pawn" and color1 == "white":
            piece.starting_row = 2
        key_value_string = color1 + type1
        count = DICT_COUNT_PIECES.get(key_value_string,0)
        key_value_pair = {key_value_string: count + 1}
        DICT_PIECES[key_value_string + str(count)] = piece
        DICT_PIECE_REVERSE[piece] = key_value_string + str(count + 1)
        DICT_COUNT_PIECES.update(key_value_pair)
        count_piece = DICT_COUNT_PIECES.get(key_value_string)
        Pieces.set_piece_number(piece, count_piece)
        
        piece.set_position()
        
        #self.image = Image.open(piece.image)
        self.piece_image = ImageTk.PhotoImage(file=piece.image)

        list1 = POSITION_CENTER[piece.position]
        x = list1[0]
        y = list1[1]
        
        # self.label = ttk.Label(self.frame2,image = self.piece_image)
        # self.label.grid(row = total, column=0)
        if color1 == "black":
            tag_string ="blackpiece"
        elif color1 == "white":
            tag_string = "whitepiece"
        self.id = self.board.create_image(x,y,anchor="center",image=self.piece_image,tags=(tag_string,"piece"))
        piece.set_id(self.id)
        self.ids[self.id] = piece
        piece.set_board_image(self.piece_image)
        self.images[piece] = self.piece_image
        
                
                

                
        
        print(DICT_COUNT_PIECES)
        
        

       
        



    def create_pieces(self):  
        total = 0
        for item in PIECE_DICTIONARY:
            list = PIECE_DICTIONARY[item]
            
            for i in range(list[3]):
                piece = Pieces(list[0],list[1],list[2])
                color1, type1, image1, position1 = Pieces.get_piece(piece)
                if type1 == "pawn" and color1 =="black":
                    piece.starting_row = 7
                elif type1 == "pawn" and color1 == "white":
                    piece.starting_row = 2
                key_value_string = color1 + type1
                count = DICT_COUNT_PIECES.get(key_value_string,0)
                key_value_pair = {key_value_string: count + 1}
                DICT_PIECES[key_value_string + str(count)] = piece
                DICT_PIECE_REVERSE[piece] = key_value_string + str(count + 1)
                DICT_COUNT_PIECES.update(key_value_pair)
                count_piece = DICT_COUNT_PIECES.get(key_value_string)
                Pieces.set_piece_number(piece, count_piece)
                
                piece.set_position()
                
                #self.image = Image.open(piece.image)
                self.piece_image = ImageTk.PhotoImage(file=piece.image)

                list1 = POSITION_CENTER[piece.position]
                x = list1[0]
                y = list1[1]
                
                # self.label = ttk.Label(self.frame2,image = self.piece_image)
                # self.label.grid(row = total, column=0)
                if color1 == "black":
                    tag_string ="blackpiece"
                elif color1 == "white":
                    tag_string = "whitepiece"
                self.id = self.board.create_image(x,y,anchor="center",image=self.piece_image,tags=(tag_string,"piece"))
                piece.set_id(self.id)
                self.ids[self.id] = piece
                piece.set_board_image(self.piece_image)
                self.images[piece] = self.piece_image
               
                
                

                
                total += 1
        print(DICT_COUNT_PIECES)
    

            
if __name__ == '__main__':
    main()
