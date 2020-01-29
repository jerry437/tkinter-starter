# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

# Add a label with the text "Hello"
firstLabel = Label(window, text="Hello", font=("Arial Bold", 50))
firstLabel.grid(column=0, row=0)

# Place the label in the window at 0, 0
secondLabel = Label(window, text = "This is a label") # Create the label
secondLabel.grid(column=1, row=0)
#imput box
txt = Entry(window,width=10)
txt.grid(column=1, row=1)
#buttons
btn = Button(window, text="Click Me")
btn.grid(column=2, row=0)
btn2 = Button(window, text="Click Me")
btn2.grid(column=2, row=1)





window.mainloop()     # Keep the window open
