def right_base(base,number) :
    if base == 2 or base == 16 :
        number = number[2:]
    elif base < 9 :
        number = number[:len(number)-3]
    else :
        number = number[:len(number) - 4]
    allowed = [str(i) for i in range(base)]
    if base > 10 :
        for i in range(base - 10) :
            allowed.append("abcdef"[i])
    for i in number :
        if i not in allowed :
            return False
    return True


def validate(number):
    while True :
        if number == None:
            number = input("Sorry, try again\n:")
            continue
        if len(number)<3:
            number = input("Sorry, try again\n:")
            continue
        number = number.strip()
        number = number.lower()
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










