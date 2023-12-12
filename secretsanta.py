import random
from tkinter import *
from tkinter import ttk

version = 0.51

def main(number):
    print("Secret Santa " + str(number))

def format():
    print("Givers:")
    
def quit():
    button = Button(window, text='Quit', width=25, command=window.destroy)
    button.pack(side = BOTTOM, pady = 5)   
    
def get_data():
    label.config(text= entry.get(), font= ('Helvetica 13'))

def show_msg():
    label= Label(window, text= "YOU CLICKED THE BUTTON!", font= ('aerial 18 bold'))
    label.pack(pady= 20)

def headings():
    L1 = Label(window, text="First Family")
    L1.place(x=35, y=35)
    L2 = Label(window, text="Second Family")
    L2.place(x=160, y=35)
    L3 = Label(window, text="Third Family")
    L3.place(x=290, y=35)
    heading1 = Label(window, text="Givers")
    heading1.place(x=600, y=35)
    heading2 = Label(window, text="Getters")
    heading2.place(x=800, y=35)

def list_creation():
    global names
    names = ['hi']

list_creation()

def entry1():
    global new_name
    slot1 = 30
    slot2 = 400
    global entry
    entry = Entry(window, bd =2)
    entry.place(x=slot1, y=slot2)
    entry.focus_set()

def participants():
    new_name = entry.get()
    names.append(new_name)
    print(names)

def name_positions():
    first_name1 = Label(window, text= names[1])
    first_name1.place(x=55,y=65)
    first_name2 = Label(window, text= names[2])
    first_name2.place(x=55, y=95)
    first_name3 = Label(window, text= names[3])
    first_name3.place(x=55, y=125)
    first_name4 = Label(window,text= names[4])
    first_name4.place(x=55, y=155)
    second_name1 = Label(window, text= names[5])
    second_name1.place(x=190, y=65 )
    second_name2 = Label(window, text= names[6])
    second_name2.place(x=190, y=95)
    second_name3 = Label(window, text= names[7])
    second_name3.place(x=190, y=125)
    second_name4 = Label(window, text= names[8])
    second_name4.place(x=190, y= 155)
    third_name1 = Label(window, text= names[9])
    third_name1.place(x=310, y=65)
    third_name2 = Label(window, text= names[10])
    third_name2.place(x=310, y=95)
    third_name3 = Label(window, text= names[11])
    third_name3.place(x=310, y=125)
    third_name4 = Label(window, text= names[12])
    third_name4.place(x=310, y=155)

def fam_setters():
    pass

def givers():
    num1 = random.randint(0,11)
    num2 = random.randint(0,11)
    num3 = random.randint(0,11)
    num4 = random.randint(0,11)
    num5 = random.randint(0,11)
    num6 = random.randint(0,11)
    num7 = random.randint(0,11)
    num8 = random.randint(0,11)
    num9 = random.randint(0,11)
    num10 = random.randint(0,11)
    num11 = random.randint(0,11)
    num12 = random.randint(0,11)
    
    while (num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5 or num1 == num6 
           or num1 == num7 or num1 == num8 or num1 == num8 or num1 == num9 or num1 == num10
           or num1 == num11 or num1 == num12 or num2 == num3 or num2 == num4 or num2 == num5 
           or num2 == num6 or num2 == num7 or num2 == num8 or num2 == num9 or num2 == num10 
           or num2 == num11 or num2 == num12 or num3 == num4 or num3 == num5 or num3 == num6 
           or num3 == num7 or num3 == num8 or num3 == num9 or num3 == num10 or num3 == num11 
           or num3 == num12 or num4 == num5 or num4 == num6 or num4 == num7 or num4 == num8 
           or num4 == num9 

           or num5 == num6 or num5 == num7 or num5 == num8
           or num5 == num9 or num6 == num7 or num6 == num8 or num6 == num9 or num7 == num8
           or num7 == num9 or num8 == num9):
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        num3 = random.randint(0,9)
        num4 = random.randint(0,9)
        num5 = random.randint(0,9)
        num6 = random.randint(0,9)
        num7 = random.randint(0,9)
        num8 = random.randint(0,9)
        num9 = random.randint(0,9)

    print(names[num1], names[num2], names[num3], names[num4], names[num5], names[num6], names[num7], names[num8], names[num9])
    giver1 = Label(window, text=names[num1])
    giver1.place(x=615, y=60)
    giver2 = Label(window, text=names[num2])
    giver2.place(x=615, y= 90)
    giver3 = Label(window, text=names[num3])
    giver3.place(x=615, y= 125)
    giver4 = Label(window, text=names[num4])
    giver4.place(x=615, y= 155)
    giver5 = Label(window, text=names[num5])
    giver5.place(x=615, y=190)
    giver6 = Label(window, text=names[num6])
    giver6.place(x=615, y=220)
    giver7 = Label(window, text=names[num7])
    giver7.place(x=615, y=245)
    giver8 = Label(window, text=names[num8])
    giver8.place(x=615, y=270)
    giver9 = Label(window, text=names[num9])
    giver9.place(x=615, y=300)



def getters():
    pass
    
def results():
    pass

def program():
    global window
    window = Tk()    
    window.geometry('1000x500')
    window.title("Secret Santa " + str(version))
    global label
    global entry

    slot4 = 200
    slot5 = 410
    slot6 = 350
    slot7 = 410


    headings()
    entry1()
    quit()

    ttk.Button(window, text= "Add", command= lambda:[entry1, participants(), name_positions(),]).place(x= slot4, y= slot5, anchor= CENTER)
    ttk.Button(window, text= "Randomize", command= lambda:[givers(), getters(), results()]).place(x= slot6, y= slot7, anchor= CENTER)

    window.mainloop()

main(version)
format()
program()

print(names)