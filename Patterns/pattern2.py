n = int(input('enter rows:'))

for i in range(n+1, 1, -1):
    for j in range(1, i):
        print(f'{j}', end=" ")
    print("* "*(n+1-i) + "* "*(n-i))
