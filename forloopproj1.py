#import time
#for sec in range (15, 0, -1):
 #   print(sec)
  #  time.sleep(2)
#print("Gumising ka na ba bading")

print("MARIO!!")
height= 0

while height < 1 or height > 8: #if yung height is less 0 or greater than 8 maglooo[
    height= int(input("Height: "))


for i in range(1, height+1): #range from 1 to the given height
        print(" " * (height - i), "#" * i) #print left side- space is the minus of height- i (e.g 1-8=7 space), # counting the i


h = 0
while h < 1 or h > 8:
    h= int(input("Height: "))

for j in range (1, h+1):
    print(" " * (h-j), "#" * j, " ", "#" * j)  #print left side- space is the minus of height- i (e.g 1-8=7 space), # counting the i
