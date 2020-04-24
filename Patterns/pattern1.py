n = int(input('enter rows:'))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(max(i, j, n+1-i, n+1-j), end=" ")
    print()
