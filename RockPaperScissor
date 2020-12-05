import random
import sys

print("Computer: Rock(r), Paper(p), Scissor(s) ?")
CompChoice = random.randint(1,3)
if CompChoice == 1:
    CompChoice = 'r'
if CompChoice == 2:
    CompChoice = 'p'
if CompChoice == 3:
    CompChoice = 's'

YourChoice = input("You: Rock(r), Paper(p), Scissor(s) ? ")

if YourChoice!='r' and YourChoice!='p' and YourChoice!='s':
    print("\nYou Entered Invalid Character!")
    sys.exit()

print("Your Choice:", YourChoice)
print("Computer's Choice:", CompChoice)

def checkCondition(CompChoice, YourChoice):
    if CompChoice == YourChoice:
        return None

    elif CompChoice == 'r':
        if YourChoice == 'p':
            return True
        elif YourChoice == 's':
            return False
    
    elif CompChoice == 'p':
        if YourChoice == 'r':
            return False
        elif YourChoice == 's':
            return True
    
    elif CompChoice == 's':
        if YourChoice == 'r':
            return True
        elif YourChoice == 'p':
            return False

Result = checkCondition(CompChoice, YourChoice)

if Result == None:
    print("Game Tie!")
elif Result:
    print("You Won!")
else:
    print("You Lose!")
