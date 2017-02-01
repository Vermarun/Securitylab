import random
import math

def expo(a,k,n):
    b=1
    A=a
    if(k==0):
        return b
    if(k & 1):
        b=a
    for i in range(1,int(math.log(k,2)+1)):
        A = (A*A)%n
        if(k & (2**i)):
            b = (A*b)%n
    return b

def fermat(n,t):
    for i in range(1,t):
        a = random.randint(2,n-2)
        r = expo(a,n-1,n)
        if r !=1:
            return False
    return True

if __name__=="__main__":

    n = int(input('Enter the number to be checked:'))

    t = 3
    if(fermat(n,t)):
        print 'Entered number ',n,' is a prime number.'
    else:
        print 'Entered number ',n,' is a composite number.'
