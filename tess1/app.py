import tkinter as tk
#import PyPDF2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'E:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300,bg='red')
canvas.grid(columnspan=3, rowspan=3)

#logo
#logo = Image.open('logo.png')
#logo = ImageTk.PhotoImage(logo)
#logo_label = tk.Label(image=logo)
#logo_label.image = logo
#logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select an image file on your computer to extract all its text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Image file", ".png"),("image file", ".webp")])
    img = Image.open(file)
    textMsg = tess.image_to_string(img)
    display01 = tk.Label(root, text='Extracted text is: '+textMsg, font="Raleway")
    display01.grid(columnspan=1, column=1, row=3)
    #image crop

    width, height = img.size

    #setting points
    left = 5
    top = height / 4
    right = 164
    bottom = 3 * height / 4

    #cropped
    img1 = img.crop(left, top, right, bottom)
    img1.show()

    
    # print(text)
    #   

    # if file:
    	# img = Image.open('iphone.webp')
    # 	text = tess.image_to_string(img)
    # 	print(text)
    # #     read_pdf = PyPDF2.PdfFileReader(file)
    #     page = read_pdf.getPage(0)
    #     page_content = page.extractText()

    #     #text box
    #     text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
    #     text_box.insert(1.0, page_content)
    #     text_box.tag_configure("center", justify="center")
    #     text_box.tag_add("center", 1.0, "end")
    #     text_box.grid(column=1, row=3)

    #     browse_text.set("Browse")

#browse button



browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=300,bg='blue')

def leftclick(event):
    print("left")
    print(f'x={event.x} y={event.y}')
canvas.bind("<Button-1>", leftclick)

#text = tess.image_to_string(img)
canvas.grid(columnspan=3)

root.mainloop()