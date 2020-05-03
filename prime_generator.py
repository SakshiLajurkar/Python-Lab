mlist, nlist, num_list, prime_list = (list() for i in range (4))
t = int(input(""))
for k in range (0,t):
    m, n = input("").split()
    mlist.append(int(m))
    nlist.append(int(n))
    num_list.append(list())
    prime_list.append(list())
for k in range (0,t):
    for i in range (mlist[k],nlist[k]+1):
        num_list[k].append(i)  # list of integers from m to n
    nl= len(num_list[k])
    p=2  # p set to 2
    while p**2<nlist[k]:
        for i in range (0,nl):
            if num_list[k][i]%p==0 and num_list[k][i]!=p:
                num_list[k][i]=0  # all the multiples of p (2p, 3p etc) in the list are marked by equating to 0
        p+=1  # p is set to next prime number
    for i in range (0,nl):
        t = num_list[k][i]
        if t!=0:
            prime_list[k].append(t)  # non marked (non-zero) elements in the list are prime numbers
    for i in range (0, len(prime_list[k])):
        print(prime_list[k][i], end=" ")
    print("")
