def right_base(base,number) :
    if base == 2 or base == 16 :
        number = number[2:]
    elif base < 9 :
        number = number[:len(number)-3]
    elif base != 10 :
        number = number[:len(number) - 4]
    allowed = [str(i) for i in range(base)]
    if base > 10 :
        for i in range(base - 10) :
            allowed.append("abcdef"[i])
    for i in number :
        if i not in allowed :
            return False
    return True

#could there be a problem with that magical ")" appearing in the end of each input?
def validate(number):
    while True :
        if number == None:
            number = input("Sorry, try again\n:")
            continue
        if len(number)<3:#edge case for small numbers in decimal print(validate(0))
            number = input("Sorry, try again\n:")
            continue
        number = number.strip()
        number = number.lower()
        if not number.isalnum() :
            number = input("Sorry, try again\n:")# if you type in a lot of shifts it is a problem, i solved it but needs more testing
            continue
        #needs an extra function cause too messy
        if number[0] == "0" or number[0] == "o":
            if number[1] == "b":
                old_base = 2
            elif number[1] == "x":
                old_base = 16
        elif number[len(number) - 2] == "x" and number[len(number) - 1].isnumeric():
            old_base = int(number[len(number) - 1])
        elif number[len(number) - 3] == "x" and number[len(number) - 2:].isnumeric():
            old_base = int(number[len(number) - 2:])
        else:
            old_base = 10
        if right_base(base=old_base, number=number) :
            return number, old_base
        else :
            number = input("Sorry, try again\n:")

#print(validate(input()))








