import imghdr
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
    images = {}
    ids = {}
    array_rows = [1,2,3,4,5,6,7,8]
    
    def __init__(self):
        self.main_window = tkinter.Tk()          
        self.main_window.geometry("800x850")
        self.main_window.title('Chess App')
        self.main_window.minsize(800,800)
        self.create_canvas()
        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.board.tag_bind("piece","<ButtonPress-1>", self.select_piece)
        self.board.tag_bind("piece", "<ButtonRelease-1>", self.drag_stop)
        self.board.tag_bind("piece", "<B1-Motion>", self.drag)
             
    def select_piece(self,event):
        self._drag_data["item"] = self.board.find_closest(event.x,event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        self.piece = self.ids[self._drag_data.get("item")]
        print("grabbed",self._drag_data.get("item"),self.piece)
    def drag_stop(self, event):
        """End drag of an object"""
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0
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
 
    def create_pieces(self):  
        total = 0
        for item in PIECE_DICTIONARY:
            list = PIECE_DICTIONARY[item]
            
            for i in range(list[3]):
                piece = Pieces(list[0],list[1],list[2])
                
                DICT_PIECES[item+str(i+1)] = piece
                DICT_PIECE_REVERSE[piece] = item + str(i+1)
                piece.set_position()
                
                #self.image = Image.open(piece.image)
                self.piece_image = ImageTk.PhotoImage(file=piece.image)

                list1 = POSITION_CENTER[piece.position]
                x = list1[0]
                y = list1[1]
                
                # self.label = ttk.Label(self.frame2,image = self.piece_image)
                # self.label.grid(row = total, column=0)
                self.id = self.board.create_image(x,y,anchor="center",image=self.piece_image,tags=("piece",))
                piece.set_id(self.id)
                self.ids[self.id] = piece

                self.images[piece] = self.piece_image
                
                total += 1
        print(BOARD_CORDINATES)
    

            
if __name__ == '__main__':
    main()
