from tkinter import *
from tkinter import ttk

version = 0.01

def main(number):
    print("Pizza Data Tracker " + str(number))

def menu():
    global window
    window = Tk()    
    window.geometry('1000x500')
    window.title("Data Tracker " + str(version))

main(version)