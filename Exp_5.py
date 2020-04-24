print("Enter integer numbers between -1000 & 1000: ")

i = True
sum = 0
numbers = list()

while i is True:
    n = int(input())

    if (n>=-1000 & n<=1000) :
        sum = sum + n

        if sum >= 0:
            numbers.append(n)
        else:
            i = False
    else:
        print("Invalid entry")

print("\n List of numbers before sum becomes negative: ")
for j in numbers:
    print(j)
