import random

def sumofsquares(integ):
    geymari = 0
    teljari = integ -1
    while(teljari != 0):
        geymari += (integ - teljari)**2
        teljari -= 1
    return geymari


print(sumofsquares(5),"sumofsq fall")

def sumofsquarestwo(n):
    print(sum([i*i for i in range (0,n)]), "FALL2")

sumofsquarestwo(5)
'''
a = range(10)
for k in range(-10, 0):
    print ('k er ', k)
    print(a[k])
b = "abcdefg"

print(b[-2])
'''
##R-1.9
y = range(50,90,10)
for k in range (len(y)):
    print(y[k])

##R-1.10
t = range(8,-9,-2)
for k in range(len(t)):
    print(t[k],end=", ")
print("")

#R-1.11
n = [2**n for n in range(100) if 2**n <= 256] 
print(n)

#R-1.12

fasdds = range(100)

def mychoice(q):
    randelement = random.randrange(len(q)-1)
    print(q[randelement])
    return q[randelement]

mychoice(fasdds)

for i in range(10):
    print(i)