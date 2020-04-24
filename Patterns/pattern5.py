n = int(input('enter rows:'))

for i in range(1, n):
    print("* "*i +"  "*(2*(n-i) - 1)+ "* "*i)
print("* "*(2*n - 1))
