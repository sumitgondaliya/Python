""" 
pattern: 
        *
        * *
        * * *
        * *
        * 
Make Sure: No. of rows should be an odd number to see proper pattern.
"""
n = int(input("Enter No. of Rows:"))
m = (n//2)+1        
for i in range(1,n+1):
    if i <= m:
        j = 1
        while j <= i:
            print("*", end=" ")
            j += 1
    else:
        for k in range(m+1,(n+m-(i-1))+1):
            print("*",end=" ")
    print()
