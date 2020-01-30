import tkinter
from gui import Gui
''' 
Launch the program. root creates the object that the Gui will use.
Once we close the gui, the program will stop.

'''

root = tkinter.Tk()
root.geometry("300x100")
root.title("Bloquear Webs")
Gui(root)
root.mainloop()
