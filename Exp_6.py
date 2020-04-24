s = []
n  = int(input("enter size of the array: "))

print("enter the elements of array: ")
for i in range (int(n)):
    k = int(input(""))
    s.append(k)

m  = s.index(min(s))

a = s[0:m];
a.sort();
a.reverse();

b = s[m:n];
b.sort();

c = a+b;

if c==s:
    print("true")
else:
    print("false")
