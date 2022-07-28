# https://docs.python.org/3/library/tkinter.html#the-packer
# Tkinter to make GUI application
# Just like javaFX

# Mac Lisa was early GUI computer
# Windows 95 came after way long time , apple sued microsoft

# Pirates of silicon valley

import tkinter  # already in python

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Aerial", 23, "bold"))
# Then we have to place the component

my_label.pack()  # it is packed and in center , side="bottom"
# http://tcl.tk/man/tcl8.6/TkCmd/pack.htm

# TO update the particular properties
my_label["text"] = "New text wow"
my_label.config(text="great using config")


def button_clicked():
    print("I got clicked")
    new_text =input.get()
    my_label.config(text="button clicked "+new_text)

button = tkinter.Button(text="Click", command=button_clicked)
button.pack()  # This is second so in line
# we can have event listener using command key argument as above

# Entry
# http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
input = tkinter.Entry(width=10)
input.pack()

# Now get the entry string
# print(input.get()) , In start the text entry field is empty so





window.mainloop()

# Setting options
# 1. during initialising
# 2. fred["fg"] = "red"
# 3. By config method for multiple keyword arguemnts
# fred.config(fg="red", bg="blue")

# http://tcl.tk/man/tcl8.6/TkCmd/entry.htm


# Tkinter has various layout managers
# pack place and grid
# pack start ffrom top and add below each , we can change side to left top botto and right
# Place is all about precise positioning , you set x and y value to the label like 0 0 for start , if not written then it will not show anything
# downside is that it is so specific
# Grid -> it is very simple one , divide whole screen it rows and column
# my_label.grid(column=0, row=0)
# grid system is relative to other labels , so if only one label then it always on top left , but if others are presnet then show good
# you can't mix up grid and pack in the same file , choose one
# padding in windows using padx pady using .config, same apply for the label and other stuff




