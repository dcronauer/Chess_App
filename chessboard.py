from chess import *
from PIL import ImageTk, Image
import tkinter
from tkinter import Tk, ttk

def main():
    print("wea are here")
    #start gui
    myboard = Chess_GUI()
    # set up main loop
    tkinter.mainloop()


class Chess_GUI:
    
    array_rows = [1,2,3,4,5,6,7,8]
    
    def __init__(self):
        self.main_window = tkinter.Tk()          
        self.main_window.geometry("800x800")
        self.main_window.title('Chess App')
        self.main_window.minsize(800,800)
        self.create_canvas()
        self.create_pieces()
        
        
    def create_canvas(self):
        x = 0
        y = 0
        width = 100
        height = 100
        self.main_window.grid_columnconfigure(0,weight=1)
        self.main_window.grid_rowconfigure(0,weight=1)
        self.main_window.grid_rowconfigure(1,weight=1)

        self.board_frame = ttk.Frame(self.main_window)
        self.board_frame.grid(row=0,column=0,sticky="nsew")
       
        self.board_frame.grid_rowconfigure(0,weight=1)
        self.board_frame.grid_columnconfigure(0,weight=1)
        
        self.frame2 = ttk.Frame(self.main_window)
        self.frame2.grid(row=1,column=0, sticky="nsew")
        self.frame2.grid_rowconfigure(1,weight=1)
        self.frame2.grid_columnconfigure(0,weight=1)
        
        
        #self.rect = self.board.Canvas.create_rectangle(0,0,100,100,fill="red")
        self.board = tkinter.Canvas(self.main_window, bg = "black",width=800,height=800)
        self.board.grid(column=0,row=0, sticky="nsew")
        
        
       
        for i in self.array_rows:
            
            if i % 2 != 0:
                #print(i,x,y,height,width)
                x,y, height,width = self.draw_squares(x,y,height,width)
                
                #print(i,x,y,height,width)
            elif i % 2 == 0:
                
                x = 100
                width = 200
                #print(i,x,y,height,width)
                x,y, height,width = self.draw_squares(x,y,height,width)
                #print(i,x,y,height,width)
                
    def draw_squares(self,x,y,height,width):
        
        for i in range(4):
            
            self.board.create_rectangle(x,y,width,height,fill="red")
            
            x += 200
            width +=200
        x = 0
        width = 100
        y += 100
        height += 100
        return x, y, height, width   
 
    def create_pieces(self):
        
                
        total = 0
        for item in PIECE_DICTIONARY:
            list = PIECE_DICTIONARY[item]
            print(list)
            for i in range(list[3]):
                piece = Pieces(list[0],list[1],list[2])
                
                
                
                
                DICT_PIECES[item+str(i+1)] = piece
                DICT_PIECE_REVERSE[piece] = item + str(i+1)
                piece.set_position()
                self.image = Image.open(list[2])
                self.piece_image = ImageTk.PhotoImage(self.image)
                piece_identity = DICT_PIECE_REVERSE[piece]
                square = POSITION_START[piece_identity]
                list1 = POSITION_NW[square]
                x = list1[0]
                y = list1[1]
                print(x,y)

                # self.label = ttk.Label(self.frame2,image = self.piece_image)
                # self.label.grid(row = total, column=0)
                self.canvas_piece = self.board.create_image(x,y,anchor="nw",image=self.piece_image)
                
                
                total += 1
        print(total)
        print(BOARD_CORDINATES)


        

       
             

if __name__ == '__main__':
    main()
