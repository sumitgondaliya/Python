# Roll a Dice with having Maximum chances of getting value 6.

import random
count = 0

generateNumber = lambda x,y : random.randint(x,y)

while True:
    a = input("Roll a Dice ?(y/n): ")
    if a == 'y':
        num = generateNumber(1,6)
        temp = generateNumber(3,5)
        if num != 6:
            count += 1
            if count >= temp:
                    num = generateNumber(6,6)
                    count = 0                    
        else:
            count = 0
        print(num)
    else:
        if(a == 'n'):
            break
        else:
            print("Please Give Valid Input!")
            break
