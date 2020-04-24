x = int(input("Enter a non-negative integer 'A' : "))
alist = list()
blist = list()

for b in range (1,x):
    for a in range (1,b):
        if (a*a + b*b == x):
            alist.append(a)
            blist.append(b)

length = len(alist)

for i in range (0,length):
    print(f" [{alist[i]},{blist[i]}]")

if length == 0:
    print(f"\n No such pair of (a,b) satisfy pythagoras thm for {x}")
