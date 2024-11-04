from Main_Body import ALL_NUMBERS

def to_decimal(number:str,old_base):
    return sum([num * old_base ** ind for num,ind in enumerate(number[::-1])])

def to_other(old_num_dec:int, new_base) :
    new_number = ""
    #unary makes an edge case
    while old_num_dec != 0 :
        new_number += ALL_NUMBERS[old_num_dec%new_base]
        old_num_dec //= new_base
    new_number = new_number[::-1]
    return new_number





