import random
import string #string module

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars) #original
key = chars.copy() #copy of chars where it is shuffled

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}") #key is shuffle

#encryption
while True:
    orig_text = input("Enter text: ")
    cypher_t = ""

    for letter in orig_text: #for every letter inputed in orig
        index = chars.index(letter)
        cypher_t += key[index]
    print(f"original text: {orig_text}")
    print(f"encrypted message: {cypher_t}")

    #deryption
    cypher_t = input("Enter encrypt message: ")
    orig_text = ""

    for letter in cypher_t: #for every letter inputed in cyper
        index = key.index(letter)
        orig_text += chars[index]
    print(f"encrypted message: {cypher_t}")
    print(f"original message: {orig_text}")

    ch = input("do you wann run again? (y/n): ").lower()

    if ch != 'y':
        break