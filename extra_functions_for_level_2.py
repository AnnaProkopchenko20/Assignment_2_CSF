def right_base_l2(base,number) :
    if base == 2 or base == 16 :
        number = number[2:]
    allowed = [str(i) for i in range(base)]
    if base == 16 :
        for i in range(6) :
            allowed.append("abcdef"[i])
    for i in number :
        if i not in allowed :
            return False, number
    return True, number


def validate_l2(number):
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
        is_valid,formatted_number = right_base_l2(base=base, number=number)
        if is_valid:
            return formatted_number, base

        number = input("Sorry, try again\n: ")


def validate_base_l2(base:str) :
    while True :
        base = base.strip()
        base = base.lower()
        if base != None :
            if base.isdecimal():
                base = int(base)
                if base == 2 or base == 10 or base == 16 :
                    return base
        base = input("Sorry, try again\n:")