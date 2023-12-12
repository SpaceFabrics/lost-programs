import random
from tkinter import *
from tkinter import ttk

version = 0.43

first_fam = ["bob", "bert", "bill", "ben"]
second_fam = ["alex", "amanda", "angel", "alexandra"]
third_fam = ["luke", "liam", "leonard", "lex"]

first_others = [second_fam, third_fam]
second_others = [first_fam, third_fam]
third_others = [first_fam, second_fam]

def main(number):
    print("Secret Santa " + str(number))

def format():
    print("Givers:")

def givers():
    first, first2, first3, first4, second, second2, second3, second4, third, third2, third3, third4 = "","","","","","","","","","","","",

    while first == first2 or first == first3 or first == first4 or first2 == first3 or first2 == first4 or first3 == first4:
        first = random.sample(first_fam, 1)
        first2 = random.sample(first_fam, 1)
        first3 = random.sample(first_fam, 1)
        first4 = random.sample(first_fam, 1)

    while second == second2 or second == second3 or second == second4 or second2 == second3 or second2 == second4 or second3 == second4:
        second = random.sample(second_fam,1)
        second2 = random.sample(second_fam,1)
        second3 = random.sample(second_fam,1)
        second4 = random.sample(second_fam,1)

    while third == third2 or third == third3 or third == third4 or third2 == third3 or third2 == third4 or third3 ==third4:
        third = random.sample(third_fam,1)
        third2 = random.sample(third_fam,1)
        third3 = random.sample(third_fam,1)
        third4 = random.sample(third_fam,1)

    print(first, first2, first3, first4, 
          second, second2, second3, second4, 
          third, third2, third3, third4)

def getters():
    first_option1, first_option2, first_option3, first_option4 = random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)
    second_option5, second_option6, second_option7, second_option8 = random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)
    third_option9, third_option10, third_option11, third_option12 = random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)

    specific1, specific2, specific3, specific4 = random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3)
    specific5, specific6, specific7, specific8 = random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3)
    specific9, specific10, specific11, specific12 = random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3)

    while specific1 == specific2 or specific1 == specific3 or specific1 == specific4 or specific2 == specific3 or specific2 == specific4 or specific3 == specific4:
        specific1 = random.randint(0,3)
        specific2 = random.randint(0,3)
        specific3 = random.randint(0,3)
        specific4 = random.randint(0,3)

    while specific5 == specific6 or specific5 == specific7 or specific5 == specific8 or specific6 == specific7 or specific6 == specific8 or specific7 == specific8:
        specific5 = random.randint(0,3)
        specific6 = random.randint(0,3)
        specific7 = random.randint(0,3)
        specific8 = random.randint(0,3)

    while specific9 == specific10 or specific9 == specific11 or specific9 == specific12 or specific10 == specific11 or specific10 == specific12 or specific11 == specific12:
        specific9 = random.randint(0,3)
        specific10 = random.randint(0,3)
        specific11 = random.randint(0,3)
        specific12 = random.randint(0,3)

    choice1 = first_others[first_option1]
    choice2 = first_others[first_option2]
    choice3 = first_others[first_option3]
    choice4 = first_others[first_option4]
    choice5 = second_others[second_option5]
    choice6 = second_others[second_option6]
    choice7 = second_others[second_option7]
    choice8 = second_others[second_option8]
    choice9 = third_others[third_option9]
    choice10 = third_others[third_option10]
    choice11 = third_others[third_option11]
    choice12 = third_others[third_option12]

    print("Getters:")
    print(choice1[specific1], choice2[specific2], choice3[specific3], choice4[specific4], 
          choice5[specific5], choice6[specific6], choice7[specific7], choice8[specific8],
          choice9[specific9], choice10[specific10], choice11[specific11], choice12[specific12])
    
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

def name_position_1():
    name1 = Label(window, text= entry.get())
    name1.place(x=35,y=65)

def participants():
    new_name = entry.get()
    names.append(new_name)
    print(names)

def name_position_2():
    name2 = Label(window, text= entry.get())

def program():
    global window
    window = Tk()    
    window.geometry('1000x500')
    window.title("Secret Santa " + str(version))
    global label
    global entry

    slot4 = 200
    slot5 = 410

    headings()

    entry1()

    quit()

    ttk.Button(window, text= "Add", command= lambda:[name_position_1(), show_msg(), entry1, participants()]).place(x= slot4, y= slot5, anchor= CENTER)

    window.mainloop()

main(version)
format()
givers()
getters()
program()

print(names)