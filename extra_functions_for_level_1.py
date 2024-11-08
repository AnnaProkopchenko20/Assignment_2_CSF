def right_base_l1(base,number) :
    if base == 2 :
        number = number[2:]
    allowed = [str(i) for i in range(base)]
    for i in number :
        if i not in allowed :
            return False, number
    return True, number


def validate_l1(number):
    while True :
        number = number.strip()
        number = number.lower()
        if not number.isalnum():
            number = input("Sorry, try again\n: ")
            continue
        base = 10
        if len(number) >= 3:
            if (number[0] == "0" or number[0] == "o") and number[1] == "b":
                base = 2
        is_valid,formatted_number = right_base_l1(base,number)
        if is_valid:
            return formatted_number, base
        number = input("Sorry, try again\n: ")

