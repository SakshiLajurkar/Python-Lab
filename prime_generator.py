mlist = list()
nlist = list()
num_list = list()
prime_list =list()

t = int(input(""))

for i in range (1,t+1):
    x, y = input("").split()
    m = int(x)
    n = int(y)
    mlist.append(m)
    nlist.append(n)
    num_list.append(list())
    prime_list.append(list())

for k in range (0,t):
    for i in range (mlist[k],nlist[k]+1):
        num_list[k].append(i)

    nl= len(num_list[k])
    p=2
    while p**2 < nlist[k]:
        for i in range (0,nl):
            if num_list[k][i]%p==0 and num_list[k][i]!=p:
                num_list[k][i]=0
        p+=1

    for i in range (0,nl):
        t = num_list[k][i]
        if t!=0:
            prime_list[k].append(t)

    pl = len(prime_list[k])
    for i in range (0, pl):
        print(prime_list[k][i], end=" ")
    print("")
