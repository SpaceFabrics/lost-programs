from tkinter import *
from tkinter import ttk
import sys

version = 0.01

def main(number):
    print("Pizza Data Tracker " + str(number))

def Window():
    global window
    window = Tk()    
    window.geometry('1000x500')
    window.title("Data Tracker " + str(version))

    Start()
    app1()
    window.mainloop()

def Start():
    L1 = Label(window, text="Calculator")
    L1.place(x=65, y=150)

def app1():
    root = Tk()
    canvas = Canvas()
    root.mainloop()
    create_oval(x0, y0, x1, y1)

main(version)
Window()
