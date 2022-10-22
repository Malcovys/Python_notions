#importation all tkinter class
#class are generate objects
from tkinter import*

#Creat istance with 'Tk()' class instantiation
#fen_1 is graphic object
fen_1 = Tk()#creat diff type of graphic window

#creat widget object with 'Label()' class instantiation
#'Label()' is used for print messages or informations in graphic windows
text_1 = Label(fen_1, text = 'Hello everibody !', fg = 'red')#fargrond=fg
text_1.pack()
bout_1 = Button(fen_1, text = 'Exit', command = fen_1.destroy)
bout_1.pack() 
mainloop()#garde la fren ouverte