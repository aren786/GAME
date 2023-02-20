import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("guess it bro: "))
    guesses += 1
    if(userGuess==randNumber):
        print("Sahi hai!")
    else:
        if(userGuess>randNumber):
            print("galat bro!! Niche Thoda")
        else:
            print("galat bro!! Thoda upar")

print(f"bro tried this much {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("Muh mitha karao be!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
