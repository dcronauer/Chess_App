import tkinter
from chess import *
from tkinter import *





def main():
    print("wea are here")
    #start gui
    myboard = Chess_GUI()
    # set up main loop
    tkinter.mainloop()
class Chess_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()          
        self.main_window.geometry("300x300")
        self.main_window.title('Chess App')
        self.main_window.minsize(300,300)
        

if __name__ == '__main__':
    main()
