from colorama import Fore
import random 

chars = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1', '2', '3', '4', '5', 
'6', '7', '8', '9','@', '!', '#', '$', 
'%', '^', '&', '*', '(', ')', '-', '_', '+']
]

password = []

pWord = ""

def genPW():
    x = 1 
    password.append(chars[0][random.randint(0,51)])
    while x < 10:
        password.append(chars[1][random.randint(0,73)])
        x += 1

def dispPW(lList, str):
    for l in lList:
        str = str + l

    print(Fore.YELLOW, str)


if __name__ == '__main__':
    genPW()
    dispPW(password, pWord)



