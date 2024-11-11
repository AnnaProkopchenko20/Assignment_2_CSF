import pickle

ALL_NUMBERS = ("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F")

def to_decimal(number:str,old_base):
    return sum([ALL_NUMBERS.index(num.upper()) * old_base ** ind for ind,num in enumerate(number[::-1])])


def to_other(old_num_dec:int, new_base:int) :
    new_number = ""
    if old_num_dec == 0 and new_base != 1 :
        return 0
    if new_base == 1 :
        return "1"*old_num_dec
    if new_base == 10 :
        return old_num_dec
    if new_base == "r":
        with open("all_roman_numerals_dictionary","rb") as file:
            dict = pickle.load(file)
            return dict[old_num_dec]
    while old_num_dec != 0 :
        new_number += ALL_NUMBERS[old_num_dec%new_base]
        old_num_dec //= new_base
    new_number = new_number[::-1]
    return new_number




