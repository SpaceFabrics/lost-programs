import random

version = 0.20

first_fam = ["bob", "bert", "bill", "ben"]
second_fam = ["alex", "amanda", "angel", "alexandra"]
third_fam = ["luke", "liam", "leonard", "lex"]

first_others = [second_fam, third_fam]
second_others = [first_fam, third_fam]
third_others = [first_fam, second_fam]

choice1 = ""

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

    print(first)
    print(first2)
    print(first3)
    print(first4)
    print(second)
    print(second2)
    print(second3)
    print(second4)
    print(third)
    print(third2)
    print(third3)
    print(third4)

def getters():
    option1, option2, option3, option4, option5, option6, option7, option8 = random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1) ,random.randint(0,1), random.randint(0,1)
    specific1, specific2, specific3, specific4, specific5, specific6, specific7, specific8 = random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3),random.randint(0,3)

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

    choice1 = first_others[option1]
    choice2 = first_others[option2]
    choice3 = first_others[option3]
    choice4 = first_others[option4]

    print("Getters:")
    print(choice1[specific1])
    print(choice2[specific2])
    print(choice3[specific3])
    print(choice4[specific4])

main(version)
format()
givers()
getters()