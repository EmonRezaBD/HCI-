#Import the required library
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


#Create an instance of tkinter frame
win= Tk()
#Set the geometry
win.geometry("1000x1000")

###########################MAIN CANVAS RELATED CODES STARTS#####################
canvas= Canvas(win, width=400, height= 400)
canvas.grid(columnspan=4, rowspan=4)
canvas.pack(side = "left", fill = "both", expand = True)
img1= PhotoImage(file="./mongodb.png")
img2= PhotoImage(file="./continue.png")
img3= PhotoImage(file="./show.png")
image_container =canvas.create_image(0,0, anchor="nw",image=img1)
###########################MAIN CANVAS RELATED CODES ENDS#####################

###########################CUT IMG CANVAS RELATED CODES STARTS#####################
canvas2= Canvas(win, width=400, height= 400,bg='red')
canvas2.pack(side = "right", fill = "both", expand = True)
###########################CUT IMG CANVAS RELATED CODES ENDS#####################

#########################IMAGE BUTTON CODE STARTS###############################
def update_image():
    #Open an Image in a Variable
    #use os.listdir and get an image file path array

    canvas.itemconfig(image_container,image=img2)

#Create a button to update the canvas image
button= ttk.Button(win, text="Update",command=lambda:update_image())
button.pack()
#########################IMAGE BUTTON CODE ENDS###############################

# binding the mouse events

########################IMAGE DRAWING ANDCUTTING CODES START#############
x1=0
y1=0
x2=0
y2=0
print('Looping')
myRectangle=None

def leftclick(event):    
    global x1
    global y1 
    x1=event.x
    y1=event.y
    print(f'left click x1={x1} y1={y1}')
    

def onLeftDrag(event):
    print(f'dragging : x={event.x} y={event.y}')


def rightclick(event):    
    global myRectangle    
    canvas.delete(myRectangle)
    print(f'Deleted the rectangle')

def onLeftClickRelease(event):
    print(f'x2={event.x} y2={event.y}')
    global x2
    global y2
    global myRectangle
    x2=event.x
    y2=event.y
    myRectangle=canvas.create_rectangle(x1, y1, x2, y2)
    print(f'A rectangle has been created={myRectangle}')
    print(f'A rectangle has been created={(x1,y1,x2,y2)}')

    # saving the canvas image
    # save postscipt image 
    filename='tempImageFile'
    canvas.postscript(file = filename + '.png') 
    

canvas.bind("<Button-1>", leftclick)
canvas.bind("<Button-3>", rightclick)
canvas.bind('<B1-Motion>', onLeftDrag) 
canvas.bind('<ButtonRelease-1>', onLeftClickRelease)
#Add image to the canvas
########################IMAGE DRAWING ANDCUTTING CODES START#############
win.mainloop()