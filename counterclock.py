import time
while True:
    for i in range(int(input("Enter a sec: ")), 0, -1):
        sec= i%60
        min= int(i/60)%60
        hr = int(i/3600)%3600
        print(f"{hr:02}:{min:02}:{sec:02}")
        time.sleep(1)
    print("\nGising na bading!\n")

    ch=input("Do you wanna try again? Type 'y': ")

    if ch.lower() != 'y':
        break

print("Thank you for using the ClockCounter!")
