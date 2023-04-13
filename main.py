from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# Creating the window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Reading the csv data
data = pandas.read_csv("./data/french_words.csv")

# converting the dataframe to a list of dictionaries
data_dict = data.to_dict(orient="records")


word = {}


# getting random entry from list of dictionaries
def get_random_row():
    global word, flip_timer
    window.after_cancel(flip_timer)
    try:
        df = pandas.read_csv("data/words_to_learn.csv")
        data_dicti = df.to_dict('records')
        word = random.choice(data_dicti)
        return_to_original()
        canvas.itemconfig(word_text, text=word["French"], fill="black")
        canvas.itemconfig(title_text, text="French", fill="black")
        flip_timer = window.after(3000, flip_card)
    except FileNotFoundError:
        word = random.choice(data_dict)
        return_to_original()
        canvas.itemconfig(word_text, text=word["French"], fill="black")
        canvas.itemconfig(title_text, text="French", fill="black")

        flip_timer = window.after(3000, flip_card)


# Changing the card to show the English translation

def flip_card():
    global word
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    english_word = word["English"]
    canvas.itemconfig(word_text, text=english_word, fill="white")


# create the words to learn file
def create_known_words():
    global data_dict, word
    data_dict.remove(word)
    data_frame = pandas.DataFrame(data_dict)
    data_frame.to_csv("data/words_to_learn.csv", index=False)


# modify words to learn file
def modify_known_words():
    global word
    df = pandas.read_csv("data/words_to_learn.csv")
    data_dicti = df.to_dict('records')
    data_dicti.remove(word)
    new_df = pandas.DataFrame(data_dicti)
    new_df.to_csv("data/words_to_learn.csv", index=False)


def green_click():
    try:
        modify_known_words()
        get_random_row()
    except FileNotFoundError:
        create_known_words()
        get_random_row()


def return_to_original():
    canvas.itemconfig(canvas_image, image=card_front)


# Setting up the card UI
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
flip_timer = window.after(3000, flip_card)
canvas_image = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Setting up the buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=get_random_row)
wrong.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=green_click)
right.grid(column=1, row=1)

get_random_row()

window.mainloop()
