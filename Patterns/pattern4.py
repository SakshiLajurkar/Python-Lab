n = int(input('enter odd no. of rows:'))

list1 = []
entry = 'A'

for i in range(0,n):
    list1.append(entry)
    entry = chr(ord(entry)+1)

for i in range(0,n):
    for j in range(0,n):
        if j==i or j==n-1-i:
            print( min(list1[n-1-j], list1[j]) + " ", end="")
        else:
            print(end="  ")
    print()
