import random

version = 0.25

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

    print(first, first2, first3, first4, second, second2, second3, second4, third, third2, third3, third4)

def getters():
    first_option1, first_option2, first_option3, first_option4, second_option5, second_option6, second_option7, second_option8, third_option9, third_option10, third_option11, third_option12 = random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1) ,random.randint(0,1), random.randint(0,1)
    specific1, specific2, specific3, specific4, specific5, specific6, specific7, specific8, specific9, specific10, specific11, specific12 = random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3), random.randint(0,3),random.randint(0,3)

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
    print(choice1[specific1], choice2[specific2], choice3[specific3], choice4[specific4], choice5[specific5], choice6[specific6], choice7[specific7], choice8[specific8])

main(version)
format()
givers()
getters()