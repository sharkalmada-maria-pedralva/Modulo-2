from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Choose a number")
frm = ttk.Frame(root, padding=200)
frm.grid()
ttk.Label(frm, text="Choose:").grid(column=1, row=0)
ttk.Button(frm, text="1", command=root.destroy).grid(column=1, row=2)
ttk.Button(frm, text="2", command=root.destroy).grid(column=1, row=3)
root.mainloop()