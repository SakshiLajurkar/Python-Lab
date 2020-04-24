def f1(y,z):
    #x=(4-7*z-3*y)/5
    #x=(4-y-2*z)/4
    x=(17-y+2*z)/20
    return x

def f2(x,z):
    #y=(9-2*z-3*x)/26
    #y= (7-3*x-z)/5
    y=(-18-3*x+z)/20
    return y

def f3(x,y):
    #z=(5-7*x-2*y)/11
    #z= (3-x-y)/3
    z=(25-2*x+3*y)/20
    return z

x0=0
y0=0
z0=0
count = 0

x1 = f1(y0,z0)
y1 = f2(x1,z0)
z1 = f3(x1,y1)

while abs(x1-x0) > 0.000001:

    x0=x1
    y0=y1
    z0=z1

    x1 = f1(y0,z0)
    y1 = f2(x1,z0)
    z1 = f3(x1,y1)
    count+=1
    print ("{:20} {:20} {:20} : {:3}".format( x1, y1, z1,count))

print (f"\n The roots are: \n x = {x1}  y = {y1}  z = {z1}\n\n No. of iterations = {count}")
