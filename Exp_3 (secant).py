from math import *

a = int(input('Enter smaller value: '))
b = int(input('Enter larger value: '))

def f(x):
    return ( 4*x - sin(x) - pow(e,x))
    #return ( x*pow(e,x) - cos(x))
    #return ( pow(x,4) - x -10)
    #return (x*sin(x) - 0.5)

count = 0
c = b - (f(b)*(b-a)) / (f(b)-f(a))

while abs(a-b) > 0.0001:
    a = b
    b = c
    c = b - (f(b)*(b-a)) / (f(b)-f(a))

    count = count + 1
    et = abs( (b-a)/b )

print(f"The root is: {c}")
print(f"Error tolerance: {et}")
print(f"Number of iterations: {count}")
