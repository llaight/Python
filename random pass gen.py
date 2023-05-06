import string
import random

def randompass(l, s, n, sp): #pinasa ko dito sa parameter ang var letter, symbol, num, space
    rpass = [] #rpass is a list
    for char in range(1,l + 1):
        rpass.append(random.choice(string.ascii_letters)) #.append ilalagay  sa end ng list
    for char in range(1, s+1):
        rpass.append(random.choice(string.punctuation))
    for char in range(1, n+1):
        rpass.append(random.choice(string.digits))
    for char in range(1, sp + 1):
        rpass.append(" ")

    random.shuffle(rpass) #shinuffle si rpass pero naka list padin to

    password ="" #created a new variable to make it a string instead a list

    for char in rpass: #for every char in rpass; ilalagay niya yon sa vr na pass
        password += char

    return f"The generated password is: {password}" #return the password




while True:
    print("Welcome to pass word generator")

    letters = int(input("enter how many letter: "))
    symbol = int(input("enter how many symbol: "))
    num = int(input("enter how many number: "))
    space = int(input("enter how many space: "))

    print(randompass(letters,symbol,num,space))
    ch = input("Do you wanna try again? (y/n): ")
    if not ch.lower() == 'y':
        break