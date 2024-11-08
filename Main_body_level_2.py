import os
from time import sleep
from Converting import to_other, to_decimal
from Intro_Outro_Ask import ask, outro
from extra_functions_for_level_2 import validate_l2, validate_base_l2


print("Hello!\nThis a converter for numbers of different bases\nAvailable bases are 10, 16, 2")
print("For binary(base 2) enter with prefix '0b',\nfor decimal(base 10) just write the number,\nfor hexadecimal(base 16) enter with prefix '0x'")
print("Some examples:\nBinary - '0b1010'\nHexadecimal - '0x8F'\nDecimal - '142'")
print("So firstly you enter your number and then the new base")


all_requests = []
while True :
    number, old_base = validate_l2(input("Please, enter your number\n: "))
    new_base = validate_base_l2(input("Please, enter your base\n: "))
    os.system('cls')
    new_number = to_other(to_decimal(number,old_base),new_base)
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