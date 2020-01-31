# A starter program for Python with Tkinter

from tkinter import *  # import Tkinter library
from random import randint
window = Tk()         # Create the application window
welcome = "Mood check"
firstmessage = "Type your first and last name "


def addToScore():
    message = txt.get()
    if message.lower() == "gerald bahati":
        if randint(1, 6) < 4:
            lbl2['text'] = "tired"
        else:
           lbl2['text'] = 'a little bit tired'
    else:
        lbl2['text'] = "happy and a little bit tired"


# Add a label with the text "Hello"
lbl2 = Label(window, text=firstmessage, font=("Arial Bold", 15))
lbl2.grid(column=0, row=1)
lbl1 = Label(window, text=welcome, font=("Arial Bold", 30))
lbl1.grid(column=0, row=0)

btn = Button(window, text="Click here ", command=addToScore)
btn.grid(column=0, row=3)

txt = Entry(window, width=10)
txt.grid(column=0, row=2)


window.mainloop()     # Keep the window open
