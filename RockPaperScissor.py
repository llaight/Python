rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [None, rock, paper, scissors]
draw = True
lose = 0
win = 0
again = True
print("Welcome to Rock Paper Scissor Game!")
while again:
    while draw:
        user = 0
        print("Choose your weapon:")

        while user <= 0 or user > 3:
            user = int(input("1. Rock, 2. Paper, 3. Scissor: "))

        print("You chose:")
        print(game_image[user])

        import random
        computer = random.randint(1,3)
        print("Computer chose:")
        print(game_image[computer])

        if computer == 1:
            print("Computer throws Rock")
        elif computer == 2:
            print("Computer throws Paper")
        else:
            print("Computer throws Scissor")

        if computer == user:
            print("DRAW! Play again")
            draw = True
        elif computer == 3 and user == 2:
            print(f"Scissor beats Paper. You LOSE!")
            lose += 1
            break
        elif computer == 1 and user == 3:
            print(f"Rock beats Scissor. You LOSE!")
            lose += 1
            break
        elif computer == 2 and user == 1:
            print(f"Paper beats Rock. You LOSE!")
            lose += 1
            break

            #user win
        elif user == 3 and computer == 2:
            print(f"Scissor beats Paper. You WIN!")
            win += 1
            break
        elif user == 1 and computer == 3:
            print(f"Rock beats Scissor. You WIN!")
            win += 1
            break
        elif user == 2 and computer == 1:
            print(f"Paper beats Rock. You WIN!")
            win += 1
            break
    play_again = input("Do you wanna play again? (y/n): ")
    if not play_again.lower() == 'y':
        again = False

print(f"\nYou won: {win}\n"
      f"You lost: {lose}")
if win <= lose:
    print("Talo ka bading!")
else:
    print("Eyy Panalo is bakla!")
print()
print("THANK YOU FOR USING THE PROGRAM!")




