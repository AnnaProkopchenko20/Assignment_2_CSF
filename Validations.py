def right_base(base,number) :
    if base == 2 or base == 16 :
        number = number[2:]
    elif base < 9 :
        number = number[:len(number)-2]
    elif base != 10 :
        number = number[:len(number) - 3]
    allowed = [str(i) for i in range(base)]
    if 16 >= base > 10 :
        for i in range(base - 10) :
            allowed.append("abcdef"[i])
    elif base > 16 :
        return False, number
    for i in number :
        if i not in allowed :
            return False, number
    return True, number


#could there be a problem with that magical ")" appearing in the end of each input?
def validate(number):
    while True :
        number = number.strip()
        number = number.lower()
        if not number.isalnum():
            number = input("Sorry, try again\n: ")
            continue
        base = 10
        if len(number) >= 3:
            if number[0] == "0" or number[0] == "o":
                if number[1] == "b":
                    base = 2
                elif number[1] == "x":
                    base = 16
            elif number[len(number) - 2] == "x" and number[len(number) - 1].isdecimal():
                base = int(number[len(number) - 1])
            elif number[len(number) - 3] == "x" and number[len(number) - 2:].isdecimal():
                base = int(number[len(number) - 2:])
        is_valid,formatted_number = right_base(base=base, number=number)
        if is_valid:
            return formatted_number, base
        number = input("Sorry, try again\n: ")


def validate_base(base:str) :
    while True :
        base = base.strip()
        base = base.lower()
        if base != None :
            if base.isdecimal():
                base = int(base)
                if 1 <= base <= 16 :
                    return base
        base = input("Sorry, try again\n:")




