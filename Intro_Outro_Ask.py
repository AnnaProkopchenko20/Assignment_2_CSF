def intro() :
    print("Hello!\nThis a converter for numbers of different bases\nBases available are from 1 to 16")
    print("For binary(base 2) enter with prefics '0b',\n for decimal(base 10) just write the number,\n for hexadecimal(base 16) enter with prefics '0x'")
    print("For any other enter with a ending 'xn', where n is a base")
    print("Some examples:\nBinary - '0b1010'\nHexadecimal - '0x8F'\nTrinary(base 3) - '211x3'")
    number = input("Please, enter your number\n: ")
    print("And you also need to pick a new base of the number.\nFor this you should just enter the number of the base")
    new_base = input("Please, enter your base\n: ")
