import random
#dec= input("What do you wanna do?: ")
#ch=input("Input your choices (seperate it using comma): ")

#ch_split=ch.split(", ")

#print(f"\nYou want to {dec}: {random.choice(ch_split)}")

#number = random.randint(1,6) #whole number

#number = random.random() #floating number

#option = ("rock", "paper", "scissor")

#option = random.choice(option) #choosing

#card = ["1", "2", "3", "4", "5", "A", "J", "K", "Q"] #only use list

#random.shuffle(card)
#print(card)

low = 1
high = 100
number = random.randint(low, high)
guesses = 0

while True:
    while True:
        guess = int(input("Guess a number: "))
        guesses += 1

        if guess < number:
            print(f"{guess} is too Low, bading")
        elif guess > number:
            print(f"{guess} is too High naman, bading")
        else:
            print(f"{guess} is correct!")
            break

    print(f"This round took you {guesses} guesses")

    ch = input("Do you wanna play again? (y for yes): ").lower()

    if ch != "y":
        break

print("Thank you for using the Program!")
