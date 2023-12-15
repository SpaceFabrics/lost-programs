import random
from tkinter import *
from tkinter import ttk

version = 0.61

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
    names = []

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
    first_name1 = Label(window, text= names[0])
    first_name1.place(x=55,y=65)
    first_name2 = Label(window, text= names[1])
    first_name2.place(x=55, y=95)
    first_name3 = Label(window, text= names[2])
    first_name3.place(x=55, y=125)
    first_name4 = Label(window,text= names[3])
    first_name4.place(x=55, y=155)
    second_name1 = Label(window, text= names[4])
    second_name1.place(x=190, y=65 )
    second_name2 = Label(window, text= names[5])
    second_name2.place(x=190, y=95)
    second_name3 = Label(window, text= names[6])
    second_name3.place(x=190, y=125)
    second_name4 = Label(window, text= names[7])
    second_name4.place(x=190, y= 155)
    third_name1 = Label(window, text= names[8])
    third_name1.place(x=310, y=65)
    third_name2 = Label(window, text= names[9])
    third_name2.place(x=310, y=95)
    third_name3 = Label(window, text= names[10])
    third_name3.place(x=310, y=125)
    third_name4 = Label(window, text= names[11])
    third_name4.place(x=310, y=155)

def fam_setters():
    global first_fam
    global second_fam
    global third_fam
    global first_others
    global second_others
    global third_others

    first_fam = [names[0], names[1], names[2], names[3]]
    second_fam = [names[4], names[5], names[6], names[7]]
    third_fam = [names[8], names[9], names[10], names[11]]

    first_others = [names[4], names[5], names[6], names[7], names[8], names[9], names[10], names[11]]
    second_others = [names[0], names[1], names[2], names[3], names[8], names[9], names[10], names[11]]
    third_others = [names[0], names[1], names[2], names[3], names[4], names[5], names[6], names[7]]

def givers():
    print(names[0], names[1], names[2], names[3], names[4], names[5], names[6], names[7], names[8], names[9], names[10], names[11])
    giver1 = Label(window, text=names[0])
    giver1.place(x=615, y=60)
    giver2 = Label(window, text=names[1])
    giver2.place(x=615, y= 90)
    giver3 = Label(window, text=names[2])
    giver3.place(x=615, y= 125)
    giver4 = Label(window, text=names[3])
    giver4.place(x=615, y= 155)
    giver5 = Label(window, text=names[4])
    giver5.place(x=615, y=190)
    giver6 = Label(window, text=names[5])
    giver6.place(x=615, y=220)
    giver7 = Label(window, text=names[6])
    giver7.place(x=615, y=245)
    giver8 = Label(window, text=names[7])
    giver8.place(x=615, y=270)
    giver9 = Label(window, text=names[8])
    giver9.place(x=615, y=300)
    giver10 = Label(window, text=names[9])
    giver10.place(x=615,y= 330)
    giver11 = Label(window, text=names[10])
    giver11.place(x=615,y=360)
    giver12 = Label(window, text=names[11])
    giver12.place(x=615,y=390)

def getters():
    first_fam = [names[0], names[1], names[2], names[3]]
    second_fam = [names[4], names[5], names[6], names[7]]
    third_fam = [names[8], names[9], names[10], names[11]]

    first_others = []
    second_others = []
    third_others = []

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
    
    while(num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5 or num1 == num6 
           or num1 == num7 or num1 == num8 or num1 == num9 or num1 == num10
           or num1 == num11 or num1 == num12 or num2 == num3 or num2 == num4 or num2 == num5 
           or num2 == num6 or num2 == num7 or num2 == num8 or num2 == num9 or num2 == num10 
           or num2 == num11 or num2 == num12 or num3 == num4 or num3 == num5 or num3 == num6 
           or num3 == num7 or num3 == num8 or num3 == num9 or num3 == num10 or num3 == num11 
           or num3 == num12 or num4 == num5 or num4 == num6 or num4 == num7 or num4 == num8 
           or num4 == num9 or num4 == num10 or num4 == num11 or num4 == num12 or num5 == num6 
           or num5 == num7 or num5 == num8 or num5 == num9 or num5 == num10 or num5 == num11 or num5 == num12
           or num6 == num7 or num6 == num8 or num6 == num9 or num6 == num10 or num6 == num11 or num6 == num12 
           or num7 == num8 or num7 == num9 or num7 == num10 or num7 == num11 or num7 == num12
           or num8 == num9 or num8 == num10 or num8 == num11 or num8 == num12 or num9 == num10 
           or num9 == num11 or num9 == num12 or num10 == num11 or num10 == num12 or num11 == num12):
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
    
    if names[num1] in first_fam:
        second_others.append(names[num1])
        third_others.append(names[num1])
    elif names[num1] in second_fam:
        first_others.append(names[num1])
        third_others.append(names[num1])
    elif names[num1] in third_fam:
        first_others.append(names[num1])
        second_others.append(names[num1])

        
    if names[num2] in first_fam:
        second_others.append(names[num2])
        third_others.append(names[num2])
    elif names[num2] in second_fam:
        first_others.append(names[num2])
        third_others.append(names[num2])
    elif names[num2] in third_fam:
        first_others.append(names[num2])
        second_others.append(names[num2])

        
    if names[num3] in first_fam:
        second_others.append(names[num3])
        third_others.append(names[num3])
    elif names[num3] in second_fam:
        first_others.append(names[num3])
        third_others.append(names[num3])
    elif names[num3] in third_fam:
        first_others.append(names[num3])
        second_others.append(names[num3])


    if names[num4] in first_fam:
        second_others.append(names[num4])
        third_others.append(names[num4])
    elif names[num4] in second_fam:
        first_others.append(names[num4])
        third_others.append(names[num4])
    elif names[num4] in third_fam:
        first_others.append(names[num4])
        second_others.append(names[num4])


    if names[num5] in first_fam:
        second_others.append(names[num5])
        third_others.append(names[num5])
    elif names[num5] in second_fam:
        first_others.append(names[num5])
        third_others.append(names[num5])
    elif names[num5] in third_fam:
        first_others.append(names[num5])
        second_others.append(names[num5])

    if names[num6] in first_fam:
        second_others.append(names[num6])
        third_others.append(names[num6])
    elif names[num6] in second_fam:
        first_others.append(names[num6])
        third_others.append(names[num6])
    elif names[num6] in third_fam:
        first_others.append(names[num6])
        second_others.append(names[num6])

    if names[num7] in first_fam:
        second_others.append(names[num7])
        third_others.append(names[num7])
    elif names[num7] in second_fam:
        first_others.append(names[num7])
        third_others.append(names[num7])
    elif names[num7] in third_fam:
        first_others.append(names[num7])
        second_others.append(names[num7])

    if names[num8] in first_fam:
        second_others.append(names[num8])
        third_others.append(names[num8])
    elif names[num8] in second_fam:
        first_others.append(names[num8])
        third_others.append(names[num8])
    elif names[num8] in third_fam:
        first_others.append(names[num8])
        second_others.append(names[num8])
    
    if names[num9] in first_fam:
        second_others.append(names[num9])
        third_others.append(names[num9])
    elif names[num9] in second_fam:
        first_others.append(names[num9])
        third_others.append(names[num9])
    elif names[num9] in third_fam:
        first_others.append(names[num9])
        second_others.append(names[num9])

    if names[num10] in first_fam:
        second_others.append(names[num10])
        third_others.append(names[num10])
    elif names[num10] in second_fam:
        first_others.append(names[num10])
        third_others.append(names[num10])
    elif names[num10] in third_fam:
        first_others.append(names[num10])
        second_others.append(names[num10])

    if names[num11] in first_fam:
        second_others.append(names[num11])
        third_others.append(names[num11])
    elif names[num11] in second_fam:
        first_others.append(names[num11])
        third_others.append(names[num11])
    elif names[num11] in third_fam:
        first_others.append(names[num11])
        second_others.append(names[num11])

    if names[num12] in first_fam:
        second_others.append(names[num12])
        third_others.append(names[num12])
    elif names[num12] in second_fam:
        first_others.append(names[num12])
        third_others.append(names[num12])
    elif names[num12] in third_fam:
        first_others.append(names[num12])
        second_others.append(names[num12])

    getter = Label(window, text=first_others[0])
    getter.place(x=800, y=60)
    getter2 = Label(window, text=first_others[1])
    getter2.place(x=800, y=90)
    getter3 = Label(window,text=first_others[2])
    getter3.place(x=800, y=125)
    getter4 = Label(window, text=first_others[3])
    getter4.place(x=800,y=155)
    getter5 = Label(window, text=second_others[0])
    getter5.place(x=800,y=190)
    getter6 = Label(window, text=second_others[1])
    getter6.place(x=800,y=220)
    getter7 = Label(window, text=second_others[2])
    getter7.place(x=800, y=245)
    getter8 = Label(window,text=second_others[3])
    getter8.place(x=800, y=270)
    getter9 = Label(window, text=third_others[0])
    getter9.place(x=800, y=300)
    getter10 = Label(window, text=third_others[1])
    getter10.place(x=800, y=330)
    getter11 = Label(window, text=third_others[2])
    getter11.place(x=800, y=360)
    getter12 = Label(window, text=third_others[3])
    getter12.place(x=800, y=390)

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