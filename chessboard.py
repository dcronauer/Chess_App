from chess import *
import tkinter
from tkinter import ttk

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
        
    def create_canvas(self):
        x = 0
        y = 0
        width = 100
        height = 100
        self.main_window.grid_columnconfigure(0,weight=1)
        self.main_window.grid_rowconfigure(0,weight=1)
        self.board_frame = ttk.Frame(self.main_window)
        self.board_frame.grid(row=0,column=0,sticky="nsew")
       
        self.board_frame.grid_rowconfigure(0,weight=1)
        self.board_frame.grid_columnconfigure(0,weight=1)
        
        #self.rect = self.board.Canvas.create_rectangle(0,0,100,100,fill="red")
        self.board = tkinter.Canvas(self.main_window, bg = "black",width=800,height=800)
        self.board.grid(column=0,row=0, sticky="nsew")
        
       
        for i in self.array_rows:
            
            if i % 2 != 0:
                print(i,x,y,height,width)
                x,y, height,width = self.draw_squares(x,y,height,width)
                
                print(i,x,y,height,width)
            elif i % 2 == 0:
                
                x = 100
                width = 200
                print(i,x,y,height,width)
                x,y, height,width = self.draw_squares(x,y,height,width)
                print(i,x,y,height,width)
                
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
          

       
             

if __name__ == '__main__':
    main()
