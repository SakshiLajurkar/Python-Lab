a=int(input('Enter trial x: '))

def f(x):
    return x*x - 5*x + 4
    #return
    #return

def g(x):
    return 2*x - 5
    #return
    #return

def newr(x):

    count=0

    while abs(f(x)/g(x)) > 0.0001:

        x = x - (f(x)/g(x))
        count = count + 1

    print(f"The root is: {x}")
    print(f"Number of iterations: {count}")

newr(a)
