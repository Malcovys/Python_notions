from tkinter import Tk,Canvas,Button,mainloop,LEFT,BOTTOM
from random import randrange

#---définition des fonctions gestionnaires d'événement:...
def switch_color():
    global line_color
    pallet = ['purple','cyan','maroon','green','red','blue','orange','yellow']
    color_switch = randrange(8) #genratrice de notre aléatoire de 0 à 7
    line_color = pallet[color_switch]

def drawline():#pb
    global x1, y1, x2, y2
    global line_color
    """tracé une ligne dans canevas"""
    canvas.create_line(x1,y1,x2,y2,width=2,fill=line_color)
    #modif next coordonées
    y2,y1 = y2+10,y1-10

"""def drawrectangle():
    global x1,y1,x2,y2,line_color
    canvas.create_rectangle(x1,y1,x2,y2,width=2,fill=line_color)
    y2,y1 = y2+10,y1-10

def drawarc():
    global x1,y1,x2,y2,line_color
    canvas.create_arc(x1,y1,x2,y2,width=2,fill=line_color)
    y2,y1 = y2+10,y1-10

def drawpolygon():
    global x1,y1,x2,y2,line_color
    canvas.create_polygon(x1,y1,x2,y2,width=2,fill=line_color)
    y2,y1 = y2+10,y1-10"""

def viewer():
    #ligne vertical
    x,y,a,b = 325,0,325,500
    canvas.create_line(x,y,a,b,width=2,fill='red')
    #ligne horizontal
    x,y,a,b = 0,250,650,250
    canvas.create_line(x,y,a,b,width=2,fill='red')

#main
 #line_coordonner
x1, y1, x2, y2 = 10, 390, 390, 10
line_color='dark green'

window = Tk()
canvas = Canvas(window,bg='dark grey',height=500,width=650)
canvas.pack(side=LEFT)#site donne la position dans la fenetre

quit_button = Button(window,text='Quit',command=window.quit)
quit_button.pack(side=BOTTOM) #'bottom' veux dire en bas

drawline_button = Button(window,text='Draw one line',command=drawline)
drawline_button.pack()

switch_color_button = Button(window,text='Another color',command=switch_color)
switch_color_button.pack()

viewer_button = Button(window,text='Viewer',command=viewer)
viewer_button.pack()
mainloop()