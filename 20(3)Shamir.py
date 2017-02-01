
n=int(input("Enter the number of shares "))
k=int(input("Enter the minimum number of shares required "))

poly_fun=[]

msg=int(input("Enter the message to be protected "))

poly_fun.append(msg) #constant part of the polynomial

#choose other coefficients

for i in range(k-1):
    poly_fun.append(int(input("Enter the "+str(i+1)+" coefficient ")))
    
print "\n Function coefficients are(First element is the secret) ",poly_fun

  
def eval_poly(x,a):
    result=0
    for i in range(len(a)):
        result+=a[i]*x**i
    return result  

D_arr=[]
def D_array():
    #D_arr=[]
    for i in range(1,n+1):
        temp=[]
        for j in range(1):
            temp.append(i)
            temp.append(eval_poly(i,poly_fun))
        D_arr.append(temp)
    return D_arr

print "\n shares with index ",D_array() #first entry in every row is index and second is corresponding polynomial value



#Randomly choose any of minimum number of shares 
    
x_arr=[]

print "select any combination of (minimum number=",k,")shares to reconstruct the message."
for i in range(k):
	x_arr.append(int(input("select "+str(i)+" shares's index ")))

print "\n selected shares(index) are:",x_arr

#Finding l(x)
l_array=[]

def l_x(t):
    
    for i in range(t):
        temp=[]
        result_numerator=[1]
        result_denominator=1
        for j in range(1,t):
            result_numerator = poly_mult(result_numerator,[-1,x_arr[(i+j)%t]])
            #print result_numerator
            result_denominator = result_denominator*(x_arr[i%t]-x_arr[(i+j)%t])
                        
        temp.append(result_numerator)
        temp.append(result_denominator)
        l_array.append(temp)
    return l_array
        
def poly_mult(p,q):
    result_prod=[0]*(len(p)+len(q)-1)
    for i in range(len(p)):
        for j in range(len(q)):
            result_prod[i+j]+=p[i]*q[j]
    return result_prod

print "\n First entry in the array  is for numerator and second is for denominator ",l_x(k)

def poly_add(p,q):
    result_sum=p
    for i in range(len(q)):
        result_sum[i]+=q[i]
    return result_sum

def Lagranges_Interpolation():
    L_array=[1]*len(x_arr)
    L=[]
    #L_arrays store y divided by l(x) denominator
    for i in range(len(x_arr)):
        L_array[i]=float(D_arr[x_arr[i]-1][1])/l_array[i][1]
    print "L_array:" ,L_array
    for i in range(len(L_array)):
        t=[]
        temp=l_array[i][0]
        for j in range(len(temp)):
            t.append(temp[j]*L_array[i])
        L.append(t)
    print L
    return reduce((lambda x,y:poly_add(x,y)),L)

coefficients=Lagranges_Interpolation()

#the decrypted message will be the last entry in the array
print "constructed polynomial:\n"
print "\nCoefficients are ",coefficients,"(decreasing power of x) "
if k%2==0:
    msg = int(coefficients[-1]*(-1))
else :
    msg = int(coefficients[-1])
print "\n Message :",msg
    
