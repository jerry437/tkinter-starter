# A starter program for Python with Tkinter
# bruh sign out u stupid 
from tkinter import * # import Tkinter library
from tkinter import Menu
from tkinter.ttk import Progressbar
from tkinter import ttk
from ttkthemes import ThemedTk

window = ThemedTk(theme="itft1S")      # Create the application window

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
#radiobutton
rad1 = Radiobutton(window,text='First', value=3)
rad1.grid(column=3, row=0)
 
rad2 = Radiobutton(window,text='second', value=4)
rad2.grid(column=4, row=0)
#progressbar
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
 
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
 
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 70
bar.grid(column=0, row=1)
#menubar
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
menu.add_cascade(label='menu', menu=new_item)
window.config(menu=menu)

window.mainloop()     # Keep the window open
