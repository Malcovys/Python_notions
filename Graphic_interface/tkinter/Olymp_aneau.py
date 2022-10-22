from tkinter import Tk, Canvas, Button, BOTTOM



def draw_cicle(start_cordonates, end_coordonates):
    canvas.create_oval(start_cordonates, end_coordonates, width=2)

# This fonction will change one of one array value on incretation
def increment_array(array,incrementeBy):
    for i in range(len(array)):
        array[i] += incrementeBy

# On met len() car i prend les valeurs dans range()
# Ex: for i in range([10,20]) --> i = 10 et i = 20
def decrement_array(array, decrementeBy):
    for i in range(len(array)):
        array[i] -= decrementeBy

# The coodinates for the circle is x and y for the start and end
start_coordonates = [60.5,60.5]
end_coordonates = [439.5,439.5]
circleDistance = 40

root = Tk()
canvas = Canvas(root, bg='white',height=500,width=500 )
canvas.pack()

quit_button = Button(root, text='Quit', command=root.destroy)
quit_button.pack(side=BOTTOM) # down position


for i in range(5):
    draw_cicle(start_coordonates,end_coordonates)
    increment_array(start_coordonates,circleDistance)
    decrement_array(end_coordonates,circleDistance)

root.mainloop()