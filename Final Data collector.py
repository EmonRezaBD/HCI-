# Import the required library
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageGrab
import os


# Get access to all the screen Images
# print('DEBUG')
screenImageNames = os.listdir('Screens')
#print(f'The contents of screens folder {screenImageNames}')

# Crating some global variables
x1 = 0
y1 = 0
x2 = 0
y2 = 0
myRectangle = None
screenCounter = -1
elementCounter = -1

# Creating the window
win = Tk()
win.title('Data Collection Tool')
win.geometry("1500x1500")
# Creating and inserting the canvas along with canvas container along with canvas img
canvas = Canvas(win, width=400, height=400, background='LightCyan3')
canvas.grid(columnspan=4, rowspan=4)
canvas.pack(side="left", fill="both", expand=True)
img1 = Image.open("white image.png")
img1 = img1.resize((200, 300))
img1 = ImageTk.PhotoImage(img1)
#img1 = img1.resize((400,800), Image.ANTIALIAS)
image_container = canvas.create_image(0, 0, anchor="nw", image=img1)

# Creating and inserting the canvas2 along with canvas container along with canvas img
canvas2 = Canvas(win, width=400, height=400,  background='LightCyan2')
canvas2.pack(side="right", fill="both", expand=True)
img2 = Image.open("white image.png")
img2 = img2.resize((200, 300))
img2 = ImageTk.PhotoImage(img2)
#img2 = img2.resize((400,800), Image.ANTIALIAS)
print(f'type of img2={type(img2)}')
image_container2 = canvas2.create_image(0, 0, anchor="nw", image=img2)

# Making the event lister functions and binding the event Listerners with Canvas 1


def leftclick(event):
    global myRectangle
    canvas.delete(myRectangle)
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


# Binding the listener functions
canvas.bind("<Button-1>", leftclick)
canvas.bind("<Button-3>", rightclick)
canvas.bind('<B1-Motion>', onLeftDrag)
canvas.bind('<ButtonRelease-1>', onLeftClickRelease)

# Placing the buttons
# this is the update button
buttonUpdate = ttk.Button(win, text="Update", command=lambda: update_image())
buttonUpdate.pack()
#button.place(relx=2, x=-2, y=2, anchor=NE)


def update_image():
    global myRectangle, screenCounter, img1, elementCounter
    # Deletes the rectangle
    canvas.delete(myRectangle)
    # update the screen counter
    screenCounter = screenCounter+1
    elementCounter = -1
    img1 = Image.open(f'Screens\{screenImageNames[screenCounter]}')
    img1 = img1.resize((200, 300))
    img1 = ImageTk.PhotoImage(img1)
    canvas.itemconfig(image_container, image=img1)


# this is the cut button
buttonCutImage = ttk.Button(win, text="Cut Image", command=lambda: cut_Image())
buttonCutImage.pack()


def cut_Image():
    # finding the co-ordinates
    global x1, y1, x2, y2
    print(f'x1={x1},y1={y1},x2={x2},y2={y2}')
    offsetX = 15
    offsetY = 20
    finalX1 = win.winfo_rootx()+canvas.winfo_x()+offsetX+x1
    finalY1 = win.winfo_rooty()+canvas.winfo_y()+offsetY+y1
    finalX2 = finalX1+x2+offsetX
    finalY2 = finalY1+y2+offsetY
    # temporarily saving the image in
    img = ImageGrab.grab().crop((finalX1, finalY1, finalX2, finalY2))
    img.save('Temp.png')

    # showing the temporary image in the canvas 2
# This is the show cut image button
button2 = ttk.Button(win, text="Show Cut Image",
                     command=lambda: updateWithTheCutImage())
button2.pack()


def updateWithTheCutImage():
    global imgTemp
    imgTemp = PhotoImage(file="./Temp.png")
    canvas2.itemconfig(image_container2, image=imgTemp)
    print('showing cur image')


# Dropdown menu options
options = ["button", "icon", "checkboxes", "radio buttons",
           "TextView", "toggles", "search field", "slider"]
clicked = StringVar()
# initial menu text
clicked.set("Select Type")
# Create Dropdown menu
dropDown = OptionMenu(win, clicked, *options)
dropDown.pack()

################# Radio button Code #########################


def print_selection():
    global l
    l.config(text=var.get())


# Creating the label
var = StringVar()
l = ttk.Label(win, background='cyan', width=23,
              text='Choose element intention')
l.place(x=10, y=10)
l.pack()

r1 = ttk.Radiobutton(win, text='Clickable', variable=var,
                     value='Clickable', command=print_selection)
r1.pack(side=LEFT, expand=True, fill=BOTH)
r2 = ttk.Radiobutton(win, text='Not sure', variable=var,
                     value='Not sure', command=print_selection)
r2.pack(side=LEFT, expand=True, fill=BOTH)
r3 = ttk.Radiobutton(win, text='Non Clickable', variable=var,
                     value='Non Clickable', command=print_selection)
r3.pack(side=LEFT, expand=True, fill=BOTH)


# Collect Data
buttonColectData = Button(win, text="COLLECT DATA",
                          command=lambda: colectData())
buttonColectData.pack()


def colectData():
    global elementCounter, screenCounter
    print("COLLECTING DATA")
    label.config(text=clicked.get())
    imgTemp = PhotoImage(file="./Temp.png")
    screenImage = PhotoImage(file=f'Screens\{screenImageNames[screenCounter]}')
    elementCounter = elementCounter+1
    imgTemp.write(
        filename=f'Elements\element{elementCounter}{screenCounter}.png', format="png")
    screenImage.write(
        filename=f'Elements\screen{screenCounter}.png', format="png")

    # X:INPUTS
    # ELEMENT NAME elem01
    # SCREEN NAME screen1
    ##### RUN TESERRACT CODE#######
    # text
    # x y h w (global)
    # Y:
    # clickability

    # pandas append []
    # .csv X,,Y\n


# Create Label
label = Label(win, text=" ")
label.pack()

# # Add image to the canvas
# ########################IMAGE DRAWING ANDCUTTING CODES START#############
win.mainloop()
