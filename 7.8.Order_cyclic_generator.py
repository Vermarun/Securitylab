import math

def gcd(a,b):
        while(b!=0):
                r=a%b
                a=b
                b=r
        return a

def phi_fun(n):
        count=0
        for i in range(1,n):
                if(gcd(n,i)==1):
                        count+=1
        return count

if __name__=='__main__':
        n = int(raw_input("Enter the modulus number:"))
        a = int(raw_input("Enter the integer:"))
        phi_value = phi_fun(n)
#       print phi_value
        if(gcd(n,a)==1):
                for i in range(1,phi_value+1):
                        if(((a**i) - 1)%n==0):
                                print "order =", i 
                                break
                        
                if(i==phi_value):
                        print a,"is a primitive root(generator)"
                        pri_roots = phi_fun(phi_value)
                        print "Total primitive roots of ",n,"=",pri_roots
#                       print j
                        print "Other primitive roots(generators) are:"
                        for j in range(1,phi_value+1):
                                if(gcd(n,j)==1):
                                        for k in range(1,phi_value+1):
                                              if(((j**k) - 1)%n==0):
                                                     break
                                        if(k==phi_value):
                                                print j,  
        else: print "Warning: select a such that gcd(n,a) should be 1"
        
                
                        
                                
                                        
                                                
                                
                                                
