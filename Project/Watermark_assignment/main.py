import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

screen = tk.Tk()
screen.withdraw()
filename = filedialog.askopenfilename(initialdir='/Users/USER/Downloads', title="select an Image:")

# print(filename)

def add_watermark(image, wm_text):
    opened_image = Image.open(image)
    image_width, image_height = opened_image.size

    draw = ImageDraw.Draw(opened_image)
    
    font_size = int(image_width/8)
    font = ImageFont.truetype('arial.ttf', font_size)

    x, y = int(image_width/2),  int(image_height/2)

    draw.text((x,y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    opened_image.show()

add_watermark(filename, "@mozyes")
