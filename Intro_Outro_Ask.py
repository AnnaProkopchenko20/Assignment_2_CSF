from time import sleep


def intro():
    print("Hello!\nThis a converter for numbers of different bases\nAvailable bases are from 1 to 16")
    print("For binary(base 2) enter with prefix '0b',\nfor decimal(base 10) just write the number,\nfor hexadecimal(base 16) enter with prefix '0x'")
    print("For any other base enter with a ending 'xn', where n is a base")
    print("Some examples:\nBinary - '0b1010'\nHexadecimal - '0x8F'\nTrinary(base 3) - '211x3'")
    print("So firstly you enter your number and then the new base")


def ask(option):
    while True :
        option = option.strip()
        option = option.lower()
        if option == 'yes' :
            return False
        if option == 'no' :
            return True
        option = input("Sorry, try again\n: ")


def outro():
    print("Thanks for checking out my app!")
    print('''
 /)_/)
(,,>.<)
/ >❤️


https://www.messletters.com/en/text-art/
 ''')

    sleep(20)

