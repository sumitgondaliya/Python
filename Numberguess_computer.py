import random

def guessTheNumber(x):
    minimum = 1
    maxmimum = x
    ack = ''
    while ack != 'c':
        if minimum != maxmimum:
            ran = random.randint(minimum,maxmimum)
        else: 
            ran = maxmimum
        ack = input(f"Is {ran} is high(h), Low(l), Correct(c)? ").lower()
        if ack == 'h':
            maxmimum = ran - 1
        elif ack == 'l':
            minimum = ran + 1

    print(f"Wow! Computer Guessed Your Number {ran}.")

if __name__ == "__main__":
    guessTheNumber(1000)   # Consider Computer has passed the range in argument 
