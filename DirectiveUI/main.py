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
    canvas = Canvas()
    window.create_rectangle(1,1,1,40,outline ="black",fill ="white",width = 2)    
    window.pack()

main(version)
Window()
