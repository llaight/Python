import math
print("Welcome to the PWD and Senior Discount!")
print("Enter the total value of the amount")
amount=float(input("P:"))
ans=(input("Are you a PWD or Senior: "))

if ans == "yes" or ans== "YES":
    discount=amount*.80
    print("Your discounted price is: " + "\n" + "P:" + str(discount))
else:
    print("Your total amount is" + "\n" + "P" + str(amount))

