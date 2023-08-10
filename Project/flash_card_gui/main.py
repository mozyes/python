from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


# data portion
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orginal_data = pandas.read_csv("data/french_words.csv")
    to_learn = orginal_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=foreground_img)
    flip_timer = window.after(3000, func=flip_card)


# flip portion
def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=background_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn", index=False)
    next_card()


# UI portion
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526, highlightthickness=0)
foreground_img = PhotoImage(file="images/card_front.png")
background_img = PhotoImage(file="images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 263, image=foreground_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 48, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 48, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

correct_img = PhotoImage(file="images/right.png")
known_button = Button(image=correct_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

window.mainloop()
