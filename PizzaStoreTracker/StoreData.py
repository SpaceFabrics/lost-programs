from tkinter import *
from tkinter import ttk
import sys
import cv2
import pizza.jpg

version = 0.01

img = cv2.imread("pizza.jpg", cv2.IMREAD_ANYCOLOR)

def main(number):
    print("Pizza Data Tracker " + str(number))

def Window():
    global window
    window = Tk()    
    window.geometry('1000x500')
    window.title("Data Tracker " + str(version))

    cv2.imshow("Pizza", img)
    cv2.waitKey(0)

    Start()



    window.mainloop()

def Start():
    L1 = Label(window, text="Main Menu")
    L1.place(x=35, y=35)


main(version)
Window()
