'''
Pattern :   
                 *
               * *
             * * *
           * * * *
'''
n = int(input("Enter No. of Rows: "))
j = 0
for i in range(1,n+1):
    j -= 1
    k = 1
    for j in range(n,i,-1):
        print(" ",end=" ")

    for k in range(1,i+1):
        print("*",end=" ")  
    print()
