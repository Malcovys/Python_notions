from tkinter import Tk,Canvas,Button,BOTTOM,mainloop

def draw_circle():
    global start_coodonates,end_coordonates
    canvas.create_oval(start_coodonates,end_coordonates,outline='red',width=2)


start_coodonates=[50,80]
end_coordonates=[450,480]

root=Tk()
canvas=Canvas(root,bg='white',height=500,width=500)
canvas.pack()

quit_button=Button(root,text='Quit',command=root.destroy)
quit_button.pack(side=BOTTOM)

draw_circle()
#coordinates palces
mainloop()

