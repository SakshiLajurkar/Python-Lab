a=int(input('Enter x1: '))
b=int(input('Enter x2: '))

def f(x):
    return x*x-x-11

m = (a+b)/2
count = 0

if f(a)*f(b)<0:

    while abs(a-b)>0.0001:

        count= count+1
        m = (a+b)/2

        if f(a)*f(m) > 0:
            a = m
        else:
            b = m

else:
    print('Invalid entries')

print(f"The root is: {m}")
print(f"Number of iterations: {count}")
