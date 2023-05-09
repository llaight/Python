#FUCK TUTORIAL HELL FYI THIS NOT FROM TUTORIAL HAHAHA
import time
ch3=input("Use the CALCULATOR 101 (Type 'y' - yes) : ")
if ch3.lower() == 'y':
    for i in range(3,0,-1):
        print(f"The program will start in {i}...")
        time.sleep(1)

    print()
    print("========================================")
    print("WELCOME TO CALCULATOR 101 ")
    print("========================================")
    while True:
        total = 0
        num1 = int(input("Enter 1 number: "))
        while True:
            print("\nOPERATORS:")
            print("(+)---ADDITION")
            print("(-)---SUBTRACTION")
            print("(*)---MULTIPLICATION")
            print("(/)---DIVISION")

            while True:
                op = input("Enter an operator (+, -, *, /): ")
                if op == '+' or op == '-' or op == '/' or op == '*':
                    break
            match op:
                case "+":
                    num2 = int(input("\nEnter 2 number: "))
                    if num1 > 0:
                        total = num1 + num2
                    else:
                        total += num2
                case "-":
                    num2 = int(input("\nEnter 2 number: "))
                    if num1 > 0:
                        total = num1 - num2
                    else:
                        total -= num2
                case "*":
                    num2 = int(input("\nEnter 2 number: "))
                    if num1 > 0:
                        total = num1 * num2
                    else:
                        total *= num2
                case "/":
                    num2 = int(input("\nEnter 2 number: "))
                    if num1 > 0:
                        total = num1 // num2
                    else:
                        total //= num2

            print(f"\nThe total is: {total}")
            num1 = 0
            ch= input("Do you want to add the total? (y/n): ")
            if ch.lower() != 'y':
                break
        ch2 = input("Do you want to use the program again? (y/n): ")
        if ch2.lower() != 'y':
            break
    print()
    for i in range(5, 0, -1):
        print(f"The program will sleep in {i}...")
        time.sleep(1)

print()
print("Program is shut down...")






