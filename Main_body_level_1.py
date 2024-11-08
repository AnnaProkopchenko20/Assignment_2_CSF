import os
from time import sleep
from Intro_Outro_Ask import ask, outro
from extra_functions_for_level_1 import validate_l1


print("Hello!\nThis a converter from binary to decimal and vice versa")
print("For binary(base 2) enter with prefix '0b',\nfor decimal(base 10) just write the number")
print("Some examples:\nBinary - '0b1010'\nDecimal - '142'")


all_requests = []
while True :
    number, old_base = validate_l1(input("Please, enter your number\n: "))
    os.system('cls')
    if old_base == 10 :
        new_base = 2
        new_number = bin(int(number))[2:]
    else:
        new_base = 10
        new_number = int(number, 2)
    result = f"{number} in base {old_base} system is {new_number} in base {new_base} system"
    all_requests.append(result)
    print(result)
    sleep(3)
    end = ask(input("Do you want to convert again?\nEnter 'Yes' or 'No'\n: "))
    os.system('cls')
    if end :
        break


os.system('cls')
print(f"You have converted {len(all_requests)} times : ")
for i in all_requests :
    print(i)
outro()