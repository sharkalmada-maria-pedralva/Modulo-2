from tkinter import *
from tkinter import messagebox

agenda = Tk()
agenda.title("Agenda")
agenda.geometry("500x590")

title = Label(agenda, text="Agenda", font=("Times 10", 24))
title.place(x=230, y= 50)

nome = Label(agenda, text="Nome:", font=("Times 10", 15))
nome.place(x=70, y=120)
nome1 = Entry(agenda, font="Times 10")
nome1.place(width=230, height=20, x=170, y=125)

tele = Label(agenda, text="Telefone:", font=("Times 10", 15))
tele.place(x=70, y=170)
tele1 = Entry(agenda, font="Times 10")
tele1.place(width=230, height=20, x=170, y=175)

ende = Label(agenda, text="Endereço:", font=("Times 10", 15))
ende.place(x=70, y=220)
ende1 = Entry(agenda, font="Times 10")
ende1.place(width=230, height=20, x=170, y=225)

dis = Label(agenda, text="Distrito:", font=("Times 10", 15))
dis.place(x=70, y=270)
dis1 = Entry(agenda, font="Times 10")
dis1.place(width=80, height=20, x=170, y=275)

pais = Label(agenda, text="País:", font=("Times 10", 15))
pais.place(x=260, y=270)
pais1 = Entry(agenda, font="Times 10")
pais1.place(width=80, height=20, x=320, y=275)

email = Label(agenda, text="Email:", font=("Times 10", 15))
email.place(x=70, y=320)
email1 = Entry(agenda, font="Times 10")
email1.place(width=230, height=20, x=170, y=325)

add = Button(text="Adicionar", font=("Times 10", 12), width=10, height=2)
add.place(x=170, y=370)

pesq = Button(text="Pesquisar", font=("Times 10", 12), width=10, height=2)
pesq.place(x=300, y=370)

agenda.mainloop()