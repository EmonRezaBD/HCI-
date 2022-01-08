# Import the required library
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageGrab


# Create an instance of tkinter frame
win = Tk()
win.title('Data Collection Tool')
# Set the geometry
win.geometry("1000x1000")

###########################MAIN CANVAS RELATED CODES STARTS#####################
canvas = Canvas(win, width=400, height=400, background='LightCyan3')
canvas.grid(columnspan=4, rowspan=4)
canvas.pack(side="left", fill="both", expand=True)
img1 = PhotoImage(file="./mongodb.png")
img2 = PhotoImage(file="./continue.png")
img3 = PhotoImage(file="./show.png")
image_container = canvas.create_image(0, 0, anchor="nw", image=img1)
###########################MAIN CANVAS RELATED CODES ENDS#####################

###########################CUT IMG CANVAS RELATED CODES STARTS#####################
canvas2 = Canvas(win, width=400, height=400,  background='LightCyan2')
canvas2.pack(side="right", fill="both", expand=True)
img4 = PhotoImage(file="./submit.png")
image_container2 = canvas2.create_image(0, 0, anchor="nw", image=img4)

###########################CUT IMG CANVAS RELATED CODES ENDS#####################

#########################IMAGE BUTTON CODE STARTS###############################


def update_image():
    # Open an Image in a Variable
    # use os.listdir and get an image file path array

    canvas.itemconfig(image_container, image=img2)


def cut_Image():
    # finding the co-ordinates
    global x1, y1, x2, y2
    print(f'x1={x1},y1={y1},x2={x2},y2={y2}')
    offsetX = 20
    offsetY = 20
    finalX1 = win.winfo_rootx()+canvas.winfo_x()+offsetX+x1
    finalY1 = win.winfo_rooty()+canvas.winfo_y()+offsetY+y1
    finalX2 = finalX1+x2+offsetX
    finalY2 = finalY1+y2+offsetY
    # temporarily saving the image in
    img = ImageGrab.grab().crop((finalX1, finalY1, finalX2, finalY2))
    img.save('Temp.png')
    global img4
    img4 = PhotoImage(file="./Temp.png")
    # showing the temporary image in the canvas 2


def updateWithTheCutImage():
    global img4
    canvas2.itemconfig(image_container2, image=img4)
    print('showing cur image')

# def getter(widget):
#     x=root.winfo_rootx()+widget.winfo_x()
#     print(x)
#     y=root.winfo_rooty()+widget.winfo_y()
#     print(y)
#     x1=x+widget.winfo_width()
#     print(x1)
#     y1=y+widget.winfo_height()
#     print(y1)
#     ImageGrab.grab().crop((x,y,x1,y1)).save("em.jpg")


# Create a button to update the canvas image
button = ttk.Button(win, text="Update", command=lambda: update_image())
button.pack()

# Create a button to update the canvas image
button1 = ttk.Button(win, text="Cut Image", command=lambda: cut_Image())
button1.pack()

# Create a button to update the canvas2 image
button2 = ttk.Button(win, text="Show Cut Image",
                     command=lambda: updateWithTheCutImage())
button2.pack()

#########################IMAGE BUTTON CODE ENDS###############################

#####Dropdown button code starts#################

# Change the label text


def show():
    label.config(text=clicked.get())


# Dropdown menu options
options = [
    "button",
    "icon",
    "checkboxes",
    "radio buttons",
    "TextView",
    "toggles",
    "search field",
    "slider"
]
clicked = StringVar()


# initial menu text
clicked.set("Select Type")

# Create Dropdown menu
drop = OptionMenu(win, clicked, *options)
drop.pack()

# Create button, it will change label text
button3 = Button(win, text="Submit Type", command=show).pack()

# Create Label
label = Label(win, text=" ")
label.pack()


################ Radio button Code #########################
def print_selection():
    l.config(text='you have selected ' + var.get())


var = StringVar()
l = ttk.Label(win, background='cyan', width=20,
              text='Choose the element intention')
l.pack()

r1 = ttk.Radiobutton(win, text='Clickable', variable=var,
                     value='A', command=print_selection)
r1.pack()
r2 = ttk.Radiobutton(win, text='Not sure', variable=var,
                     value='B', command=print_selection)
r2.pack()
r3 = ttk.Radiobutton(win, text='Non Clickable', variable=var,
                     value='C', command=print_selection)
r3.pack()


# binding the mouse events

########################IMAGE DRAWING ANDCUTTING CODES START#############
x1 = 0
y1 = 0
x2 = 0
y2 = 0
print('Looping')
myRectangle = None


def leftclick(event):
    global x1
    global y1
    x1 = event.x
    y1 = event.y
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
    x2 = event.x
    y2 = event.y
    myRectangle = canvas.create_rectangle(x1, y1, x2, y2)
    print(f'A rectangle has been created={myRectangle}')
    print(f'A rectangle has been created={(x1,y1,x2,y2)}')

    # saving the canvas image
    # save postscipt image
    filename = 'tempImageFile'
    canvas.postscript(file=filename + '.png')


canvas.bind("<Button-1>", leftclick)
canvas.bind("<Button-3>", rightclick)
canvas.bind('<B1-Motion>', onLeftDrag)
canvas.bind('<ButtonRelease-1>', onLeftClickRelease)
# Add image to the canvas
########################IMAGE DRAWING ANDCUTTING CODES START#############
win.mainloop()
