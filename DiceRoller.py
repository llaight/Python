card_1 = '''
|-----|
|     |
|  0  |
|     |
|_____|
'''

card_2 = '''
|-----|
| 0   |
|     |
|   0 |
|_____|
'''

card_3 ='''
|-----|
|     |
|0 0 0|
|     |
|_____|
'''

card_4 = '''
|-----|
|0   0|
|     |
|0   0|
|_____|
'''

card_5 ='''
|-----|
|0   0|
|  0  |
|0   0|
|_____|
'''

card_6 = '''
|-----|
|0 0 0|
|     |
|0 0 0|
|_____|
'''

game_art = [None, card_1, card_2, card_3, card_4, card_5, card_6]
import time
import random
import math
user_score= 0
comp_score= 0
again= True
draw= True
print("=============================")
print("Welcome to Dice Roll!")
print("=============================\n")
while again:
    while draw:
        cho= input("Enter 'r' to roll the dice: " )

        if cho.lower() == 'r':
            print(f"You rolls dice in")
            for i in range(3,0,-1):
                print(f"{i}...", end=" ")
                time.sleep(1)

            user_dice1 = random.randint(1,6)
            user_dice2 = random.randint(1,6)

            print(f"\nYour dice 1= {user_dice1} {game_art[user_dice1]}")
            #print(game_art[user_dice1])
            print(f"Your dice 2= {user_dice2} {game_art[user_dice2]}")
            user_total = user_dice1 + user_dice2
            print(f"Your Total ={user_total}\n")


            #computer
            print(f"Computer rolls dice in ")
            for i in range(5,0,-1):
                print(f"{i}...", end=" ")
                time.sleep(1)

            print()
            comp_dice1 = random.randint(1,6)
            comp_dice2 = random.randint(1,6)
            print(f"The computer dice 1= {comp_dice1} {game_art[comp_dice1]}")
            print(f"The computer dice 2= {comp_dice2} {game_art[comp_dice2]}")
            comp_total = comp_dice1 + comp_dice2
            print(f"Computer Total ={comp_total}")

            if not comp_total == user_total:
                print(f"\nThe Highest number is: {max(comp_total, user_total)}")

            print()
            if user_total == comp_total:
                print(f"Your Total ={user_total} == Computer Total ={comp_total}")
                print("\033[1mIt's a DRAW!\033[0m")
                draw = True
                print()

            elif user_total > comp_total:
                print(f"Your Total ={user_total} > Computer Total ={comp_total}")
                print("\033[1mYOU WON!\033[0m")
                user_score +=1
                break
            else:
                print(f"Your Total ={user_total} < Computer Total ={comp_total}")
                print("\033[1mYOU LOSE!\033[0m")
                comp_score += 1
                break

    cho2= input("\nDo you wanna play again? (Type 'y'): ")
    print()
    if not cho2.lower() == 'y':
        again = False
print(f"Your total score is: {user_score}\nComputer total score is: {comp_score}")
if user_score <= comp_score:
    print("\nBOOOOH! YOU \033[1mLOSE\033[0m BITCH!!!")
else:
    print("\nYOU ARE \033[1mWINNER\033[0m OF THIS CHALLENGE!!!")