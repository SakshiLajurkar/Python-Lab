a = int(input('Enter 1st number :'))
b = int(input('Enter 2nd number :'))

if a==0 or b==0:
        print(f'The GCD is {a+b}')

else:

    if max(a,b) % min(a,b)==0:
        print(f'The GCD is {min(a,b)}')

    else:
        for i in range(1, min(a,b)+1):
            if a%i==0 and b%i==0:
                g=i
        print(f'The GCD is: {g}')
