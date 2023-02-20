import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'p':
        if you=='r':
            return False
        elif you=='s':
            return True
    
    elif comp == 'r':
        if you=='s':
            return False
        elif you=='p':
            return True
    elif comp == 's':
        if you=='p':
            return False
        elif you=='r':
            return True

print("Comp Turn: Paper(p) Rock(r) or Scissors(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'p'
elif randNo == 2:
    comp = 'r'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: Paper(p) Rock(r) or Scissors(s)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("EQUAL IDIOTS!")
elif a:
    print("WINNER!")
else:
    print("NOT AGAIN!")