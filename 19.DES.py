hex_array={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    
bin_to_hex={'0000':0,'0001':1,'0010':2,'0011':3,'0100':4,'0101':5,'0110':6,'0111':7,'1000':8,'1001':9,'1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}

PC_1=[57,49,41,33,25,17,9,
      1,58,50,42,34,26,18,
      10,2,59,51,43,35,27,
      19,11 ,3,60,52,44,36,
      63,55,47,39,31,23,15,
      7,62,54,46,38,30,22,
      14,6,61,53,45,37,29,
      21,13,5,28,20,12,4
    ]
S1=[
    [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
    [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
    [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
    [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ]
S2=[
    [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
    [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
    [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
    [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ]
S3=[
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], 
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], 
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ]
S4=[
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], 
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], 
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ]
S5=[
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], 
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], 
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], 
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ]
S6=[
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], 
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ]
S7=[
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], 
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], 
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], 
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ]
S8=[
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], 
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], 
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]

left_shifts=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    
PC_2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,
      47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

IP=[58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48,
    40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13,
    5, 63, 55, 47, 39, 31, 23, 15, 7]

E_bit=[32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22,
       23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

IP_1=[40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

P=[16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]


LL_arr=[]
RR_arr=[]

LD_arr=[]
RD_arr=[]

def left_shift(a,n):
    if n==1:
        b=a[n:]+a[:1]
    elif n==2:
        b=a[2:]+a[:2]
    return b

def convert_to_bits(n,padding):
    result=[]
    while n>0:
        if n%2==0:
            result=[0]+result
        else:
            result=[1]+result
        n=int(n/2)
    while len(result)<padding:
        result=[0]+result
    return result

def xOr(a,b):
    arrr=[]
    for i in range(len(a)):
        arrr+=[int(a[i])^int(b[i])]
    return arrr   

def calculate_binary(arra,n):
    if n==2:
        return 2*arra[0]+1*arra[1]
    elif n==4:
        return 2**3*arra[0]+2**2*arra[1]+2*arra[2]+arra[3]
    
def f_function(R,K):
    temp=[]
    for i in range(len(E_bit)):
        temp.append(R[E_bit[i]-1])
    
    abc=xOr(K,temp)
    bc=[abc[i:i + 6] for i in range(0, len(abc), 6)]
    
    SS=[S1,S2,S3,S4,S5,S6,S7,S8]
    SSS=[]
    for i in range(8):
        SSS+=S_B(bc[i],SS[i])
    f_R_K=[]
    for i in range(len(P)):
        f_R_K.append(SSS[P[i]-1])
        
    return f_R_K

def key_generator(j,CD):
    K1=[]
    for i in range(len(PC_2)):
        K1.append(CD[j][PC_2[i]-1])
    return K1  

def S_B(a,S_arr):
    row=calculate_binary([a[0],a[5]],2)
    column=calculate_binary(a[1:5],4)
    result=convert_to_bits(S_arr[row][column],4)
    return result


def encrypt(message,key):
    if len(message)<16 or len(key)<16:
        print "\nMessage or Key size is less than 16 characters(All Hexadecimal only)\nTry Again!"
        return
    elif len(message)>16 or len(key)>16:
         print "\nMessage or Key size is more than 16 characters(All Hexadecimal only)\nTry Again!"
         return
    #K='1334577991234561'
    M=message
    K=key
    size_M=len(M)
    M_bin=[]
    for i in range(size_M):
        M_bin.append(convert_to_bits(hex_array[M[i]],4))    
    message=[]
    for i in range(len(M_bin)):
        message+=M_bin[i]
    #print "Mesage in binary is",message

    L=message[:32]
    #print "L=",L
    R=message[32:]
    #print "R=",R
    #K='0E329232EA6D0D73'
    size_K=len(K)
    K_bin=[]
    for i in range(size_K):
        K_bin.append(convert_to_bits(hex_array[K[i]],4))
    key=[]
    message+=M_bin[i]
    for i in range(len(K_bin)):
        key+=K_bin[i]
    #print "Key in binary is:",key,"\nKey length is",len(key)

    #Calculating K+
    K_plus=[]
    for i in range(len(PC_1)):
        K_plus.append(int(key[PC_1[i]-1]))

    #print "K+ is\n",K_plus

    C0=K_plus[:28]
    D0=K_plus[28:]

    #For generating 16 keys

    left_shifts=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

    C=[]
    C.append(C0)
    for i in range(1,17):
        temp=left_shift(C[i-1],left_shifts[i-1])
        C.append(temp)

    D=[]
    D.append(D0)
    for i in range(1,17):
        temp=left_shift(D[i-1],left_shifts[i-1])
        D.append(temp)

    #Key Generation
    C0D0=[]
    for i in range(len(C)):
        C0D0.append(C[i]+D[i])

    #Converting 56 bits C0D0 to 48 by using PC_2
    Kn=[]
    for j in range(1,17):
        Kn.append(key_generator(j,C0D0))
        
    #Initial permutaiton on Message using IP_array
    IP_array=[]
    for i in range(len(IP)):
        IP_array.append(message[IP[i]-1])
    
    #print "Initial permutaiton on Message using IP \n",IP_array
    
    L0=IP_array[:32]
    R0=IP_array[32:]

    LL_arr.append(L0)
    RR_arr.append(R0)
    # final_computing(encrypt_flag)
    for i in range(1,17):
        LL_arr.append(RR_arr[i-1])
        RR_arr.append(xOr(LL_arr[i-1],f_function(RR_arr[i-1],Kn[i-1])))

    R16L16=RR_arr[16]+LL_arr[16]
    
    IP_ea=[]
    for i in range(len(IP_1)):
        IP_ea.append(R16L16[IP_1[i]-1])
    Cipher_text=''
    for i in range(len(IP_ea)):
        Cipher_text+=str(IP_ea[i])
        
    Cipher_text=[Cipher_text[i:i+4] for i in range(0,len(IP_ea),4)]

    #Decrypted Text
    answer=''
    for i in range(len(bin_to_hex)):
        answer+=str(bin_to_hex[Cipher_text[i]])
    return answer

def decrypt(cipher,key):
    if len(cipher)<16 or len(key)<16:
        print "\nKey size have less than 16 characters(All Hexadecimal only)\nTry Again!"
        return
    elif len(cipher)>16 or len(key)>16:
        print "\nKey size have more than 16 characters(All Hexadecimal only)\nTry Again!"
        return
        
    #K='1334577991234561'
    M=cipher
    K=key
    size_M=len(M)
    M_bin=[]
    for i in range(size_M):
        M_bin.append(convert_to_bits(hex_array[M[i]],4))    
    message=[]
    for i in range(len(M_bin)):
        message+=M_bin[i]
    #print "Mesage in binary is",message

    L=message[:32]
    #print "L=",L
    R=message[32:]
    #print "R=",R
    #K='0E329232EA6D0D73'
    size_K=len(K)
    K_bin=[]
    for i in range(size_K):
        K_bin.append(convert_to_bits(hex_array[K[i]],4))
    key=[]
    message+=M_bin[i]
    for i in range(len(K_bin)):
        key+=K_bin[i]
    #print "Key in binary is:",key,"\nKey length is",len(key)

    #Calculating K+
    K_plus=[]
    for i in range(len(PC_1)):
        K_plus.append(int(key[PC_1[i]-1]))

    C0=K_plus[:28]
    D0=K_plus[28:]

    #For generating 16 keys

    left_shifts=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

    C=[]
    C.append(C0)
    for i in range(1,17):
        temp=left_shift(C[i-1],left_shifts[i-1])
        C.append(temp)

    D=[]
    D.append(D0)
    for i in range(1,17):
        temp=left_shift(D[i-1],left_shifts[i-1])
        D.append(temp)

    #Key Generation
    C0D0=[]
    for i in range(len(C)):
        C0D0.append(C[i]+D[i])
    
    #Converting 56 bits C0D0 to 48 by using PC_2
    Kn=[]
    for j in range(1,17):
        Kn.append(key_generator(j,C0D0))
    
    #Initial permutaiton on Message using IP_array
    IP_array=[]
    for i in range(len(IP)):
        IP_array.append(message[IP[i]-1])
    
    L0=IP_array[:32]
    R0=IP_array[32:]

    LD_arr.append(LL_arr[16])
    RD_arr.append(RR_arr[16])

    for i in range(1,17):
            RD_arr.append(LD_arr[i-1])
            LD_arr.append(xOr(RD_arr[i-1],f_function(LD_arr[i-1],Kn[16-i])))
   
    IP_da=[]

    temp1=LD_arr[16]+RD_arr[16]
    
    for i in range(len(IP_1)):
        IP_da.append(temp1[IP_1[i]-1])

    for i in range(len(IP_da)):
        IP_da[i]=str(IP_da[i])
    Plain_Text=''
    for i in range(len(IP_da)):
        Plain_Text+=str(IP_da[i])
        
    Plain_Text=[Plain_Text[i:i+4] for i in range(0,len(IP_da),4)]

    #Decrypted Text
    answer=''
    for i in range(len(bin_to_hex)):
        answer+=str(bin_to_hex[Plain_Text[i]])
    return answer    
    

if __name__=="__main__":
    msg = raw_input("Enter your message(Hexadecimal Only) of lenth 16\n")
   # Key = input("Enter your key(Hexadecimal Only) of lenth 16")
    Key = '1234567890123498'
    print '\nMessage:',msg
    print '\nKey:',Key
    print '\nMessage after encryption:'
    print '\n**********************Encryption**********************************'
    cipher = encrypt(msg,Key)

    print "\nEncryption: ",cipher

    print '\nMessage after decryption:'
    print '\n**********************Decryption**********************************'
    print "\nDecryption: ",decrypt(cipher,Key)
