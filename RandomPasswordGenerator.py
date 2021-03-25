import string
import random

def randompassword():
    chars = string.ascii_letters + string.digits
    size = 3
    return ''.join(random.choice(chars) for x in range(size,25))

n = 0 
while n < 10:
    print(randompassword())
    n += 1

#If you want symbols in password then concate string.punctuation in chars variable
#Also you can set any length of password to be generate 
