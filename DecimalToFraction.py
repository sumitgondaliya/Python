def decimalToFraction(n):
    temp = len(n[n.find(".")+1:])
    a = int(float(n) * pow(10,temp))
    b = pow(10,temp)
    for i in range(a,0,-1):
        if a % i == 0 and b % i == 0:
            a = a // i
            b = b // i
            break
    print(f"Fraction is: {a}/{b}")

if __name__ == "__main__":
    n = input("Enter Decimal: ")
    decimalToFraction(n)
