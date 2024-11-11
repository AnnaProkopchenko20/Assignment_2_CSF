import os
from os import system
from Converting import to_other, to_decimal
from Intro_Outro_Ask import intro, ask, outro
from Validations import validate_base, validate
from time import sleep


intro()


all_requests = []
while True :
    number, old_base = validate(input("Please, enter your number\n: "))
    if old_base == "r":
        number_in_decimal = number[1]
        number = number[0].upper()
    else :
        number_in_decimal = to_decimal(number,old_base)
    new_base = validate_base(input("Please, enter new base\n: "),number_in_decimal,old_base)
    os.system('cls')
    new_number = to_other(number_in_decimal,new_base)
    result = f"{number} in base {old_base} system is {new_number} in base {new_base} system"
    #if user enters the same base
    all_requests.append(result)
    print(result)
    sleep(3)
    end = ask(input("Do you want to convert again?\nEnter 'Yes' or 'No'\n: "))
    os.system('cls')
    if end :
        break


#записування всіх requests у файл????
if len(all_requests) == 1 :
    print(f"You have converted 1 time : ")
else :
    print(f"You have converted {len(all_requests)} times : ")
for i in all_requests :
    print(i)
outro()


#maybe add a readme and proper gitignore







