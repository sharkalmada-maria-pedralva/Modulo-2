from tkinter import *
from tkinter import ttk

def click1():
    button1.config(text="X")
def click2():
    button2.config(text="X")
def click3():
    button3.config(text="X")
def click4():
    button4.config(text="X")
def click5():
    button5.config(text="X")
def click6():
    button6.config(text="X")
def click7():
    button7.config(text="X")
def click8():
    button8.config(text="X")
def click9():
    button9.config(text="X")


root = Tk()
root.title("Jogo")
root.geometry('450x480')
button1 = Button(root, text="", height=10, width=20, command=click1)
button1.grid(row=0, column=0)

button2 = Button(root, text="", height=10, width=20, command=click2)
button2.grid(row=0, column=1)

button3 = Button(root, text="", height=10, width=20, command=click3)
button3.grid(row=0, column=2)

button4 = Button(root, text="", height=10, width=20, command=click4)
button4.grid(row=1, column=0)

button5 = Button(root, text="", height=10, width=20,  command=click5)
button5.grid(row=1, column=1)

button6 = Button(root, text="", height=10, width=20,  command=click6)
button6.grid(row=1, column=2)

button7 = Button(root, text="", height=10, width=20,  command=click7)
button7.grid(row=2, column=0)

button8 = Button(root, text="", height=10, width=20,  command=click8)
button8.grid(row=2, column=1)

button9 = Button(root, text="", height=10, width=20,  command=click9)
button9.grid(row=2, column=2)


root.mainloop()