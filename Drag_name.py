import random
print('=========================================')
print('WELCOME TO THE DRAG NAME GENERATOR!')
print('=========================================\n')

ch= input('Type "y" to start: ').lower()
if ch=='y':

    while True:

        df_name=['Trixie', 'Petrovna','Naomi','Gelai','Allysa','Katya','Bob','Pearl', 'Sasha', 'Marina', 'Eva', 'Ms.',
                 'Vaginell', 'Raja', 'Pangina', 'Toni', 'Crystal', 'Gigi', 'Kendall', 'Laganja', 'Manila']
        dl_name=['Zamo', 'Edwards', 'Delano', 'Velour', 'Colby', 'Goode', 'Gaga', 'Methyd', 'Gemini', 'The Drag Queen',
                 'Aja', 'Davenport', 'O\' Hara', 'Avalon', 'Mateo', 'Envy', 'Hall', 'Rose', 'Iman']

        rdf = random.choice(df_name)
        rdl = random.choice(dl_name)

        result= rdf + " " + rdl

        print(f'\nThis is your Drag Name:\n\n{result}')
        ch2=input('\n\nDo you wanna play again? Type "y": ').lower()

        if ch2 != 'y':
            break

print(f'\nThank you for using the Drag Name Generator')
