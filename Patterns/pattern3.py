n = int(input('enter odd no. of rows:'))

for i in range(0, n):
    for j in range(0, n):
        if (i+j)==(n//2) or (i+j)==(n-1 + n//2) or abs(i-j)==(n//2) :
            print("* ", end="")
        else:
            print(end="  ")
    print()
