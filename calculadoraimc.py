from tkinter import *
from tkinter import messagebox

def calcular():
    height = float(altura1.get())
    weight = float(peso1.get())
    imc = weight / (height**2)
    resultado.config(text=f"Imc: {imc}")



calculadora = Tk()
calculadora.title("Calculadora IMC")
calculadora.geometry("500x590")


title = Label(calculadora, text="Calculadora de IMC", font=("Times 10", 24))
title.place(x=100, y= 50)

peso = Label(calculadora, text="Peso(kg):", font=("Times 10", 15))
peso.place(x=70, y=120)
peso1 = Entry(calculadora, font="Times 10")
peso1.place(width=150, height=20, x=200, y=125)


altura = Label(calculadora, text="Altura(m):", font=("Times 10", 15))
altura.place(x=70, y=170)
altura1 = Entry(calculadora, font="Times 10")
altura1.place(width=150, height=20, x=200, y=175)

calc = Button(text="Calcular IMC", font=("Times 10", 12), width=15, height=1, command=calcular)
calc.place(x=200, y=220)

resultado = Label(calculadora, text="", font=("Times 10", 15))
resultado.place(x=70, y=270)


calculadora.mainloop()