print('+++++++++++++++++++++++++++++++++++++')
print('WELCOME TO LOVE LINE!')
print('+++++++++++++++++++++++++++++++++++++')
print('Your mission is to get your S/O.')
ans= 'y'

while ans == 'y':
    name=input('\nEnter your S/O name (note:Male): ')

    ch1=input('\nYou are currently in a party, hanging out with your friends.\n'
              'You are having fun, but then someone tap into your shoulder, wanting to get your attention.\n'
              '\nWould you entertain him? Type "Yes" or "No": ').lower()
    if ch1 == 'yes':
        ch2=input('\nHe introduce himself, he said his name is ' + name + '.\n'
                  'and you did the same. You to start to click as you get to know each other '
                  'until he asked a personal question. \n\nAre you in a relationship? Type "Single" or "Lie": ').lower()
        if ch2 == 'single':
            ch3=input('\nYou saw him widen his smile, and then grab you to dance. You enjoy spending your time with him.\n'
                      'As the time clocks to midnight, you realize you have to go, since you have school later morning.\n'
                      'You told '+ name + ' you have to leave, and without hesitation he asked for your number,\nconfessing'
                      ' that he likes you so much and want to stay connected with you.\n'
                      'But, you\'re still a student, and you have a rule that you don\'t date, till you graduate.\n'
                      '\nWould you give your number? Type "Yes" or "No": ').lower()
            if ch3 == 'yes':
                print('\n' + name + ' Let out a big WOOH! making you smile, and before you left you,\nhe give you the sweetest'
                      ' kiss in the cheeks, promising he will call. \nAnd he did!')
                print('\n\n#Love Wins!\nThe end!')
            elif ch3 == 'no':
                ch4=input('\n' + name + ' beg you, because he likes you so much, he offer to give his number instead.\n\nWould you take it?'
                                 ' Type "Okay" or "dont": ').lower()
                if ch4 == 'okay':
                    print('\n' + name + ' let out a sigh of relief, then escort you out the party.\nAnd the moment you went home'
                                 ' you texted.\nWithout a second he replied!')
                    print('\n\n#Love Wins!\nThe end!')
                elif ch4 == 'dont':
                    print('\n' +name + ' sigh in defeat, he just give you a weak smile, and said he have fun meeting you,'
                                 ' then he left.\nAnd this is the last time you meet him.')
                    print('\nGame over!')
                else:
                    print('\nThere is no such thing in the choices.\n\nGame over!')
            else:
                print('\nThere is no such thing in the choices.\n\nGame over!')
        elif ch2 == 'lie':
            print('\n' +name + ' gives you a weak smile, then left.\nAnd this is the last time you meet him.')
            print('\nGame over!')
        else:
            print('\nThere is no such thing in the choices.\n\nGame over!')
    elif ch1 == 'no':
        print('\nThe person left.\n\nGame over!')
    else:
        print('\nThere is no such thing in the choices.\n\nGame over!')
    ans=input('\nDo you wanna play again? Type "y" or "n" : ').lower()

print('\n\n+++++++++++++++++++++++++++++++++++++')
print('THANK YOU FOR PLAYING LOVE LINE!')
print('+++++++++++++++++++++++++++++++++++++')


