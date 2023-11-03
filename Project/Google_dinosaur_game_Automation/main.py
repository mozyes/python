import pyautogui
import time
from PIL import ImageGrab, ImageOps

# Define constants for screen coordinates and colors
dino_x = 1
dino_y = 618
ground_box_x = 146
ground_box_y = 618
dino_box_x = 170
dino_box_y = 570
collision_color = (83, 83, 83)


# Function to check for ground obstacles
def is_obstacle():
    ground_box = (ground_box_x, ground_box_y, ground_box_x + 80, ground_box_y + 134)
    image = ImageGrab.grab(ground_box)
    gray_image = ImageOps.grayscale(image)
    color = gray_image.getpixel((40, 67))
    return color != collision_color


# Function to check if the dinosaur is still alive
def is_dinosaur_alive():
    dino_box = (dino_box_x, dino_box_y, dino_box_x + 130, dino_box_y + 139)
    image = ImageGrab.grab(dino_box)
    gray_image = ImageOps.grayscale(image)
    color = gray_image.getpixel((65, 69))
    return color != collision_color


# Main game automation loop
while is_dinosaur_alive():
    if is_obstacle():
        pyautogui.keyDown('space')
        time.sleep(0.2) 

    else:
        time.sleep(0.05)  
