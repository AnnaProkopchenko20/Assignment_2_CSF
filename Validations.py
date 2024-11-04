def basic_validation(input) :
    while True:
        if input != None:
            input = input.strip()
            input = input.lower()
            return input


def right_base(base) :
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


def validate_number(number:str):
    number = basic_validation(input=number)
    if len(number) < 3 :
        return False
    #а десяткова система????????????????????
    if number[0] == "0" or number[0] == "o" :
        if number[1] == "b" :
            old_base = 2
        elif number[1] == "x" :
            old_base = 16
    elif number[len(number)-2] == "x" and number[len(number)-1].isnumeric() :
        old_base = int(number[len(number)-1])
    elif number[len(number)-3] == "x" and number[len(number)-2:].isnumeric() :
        old_base = int(number[len(number)-2:])
    if old_base != None :
        right_base(base=old_base)






