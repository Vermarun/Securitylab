#include<iostream>
#include<stdlib.h>
#include<time.h>
#include<math.h>
#include<string.h>
#define Max_bits 8
long  int list[3];
using namespace std;

struct public_key{

	long  int n,E;}pk;

struct users{
	long  int sk;
	public_key pk;};

long  int gcd(long  int a ,long  int b){
	long  int r;
	while(b!=0){
		r=a%b;
		a=b;
		b=r;}
return a;
}

int phi_fun(long int n){
	int count =0;
	for(int i=1;i<n;i++){
		if(gcd(n,i)==1){	
			count++;}
	}
return count;
}
long  int private_key(long  int a,long  int b){
		
		long  int q,r;
		long  int x1=0,x2=1,y1=1,y2=0,x0,y0;
		while(b>0){
			q = floor(a/b);
			r = a - q*b;
			x0 = x2 - q*x1;
			y0 = y2 - q*y1;
			a = b; b = r;
			x2 = x1; x1 = x0;
			y2 = y1; y1 = y0;
			}
//	cout<<"x2="<<x2<<"\n";
	return x2;
}
long  int key_generator(){
	
	long  int p,q,r,e,k,seck,phi_value;
	int flag=0;
	/*while(flag!=1){
	r = rand() % int (pow(2,Max_bits)-1) + int(pow(2,(Max_bits-1)));
	if(phi_fun(r)==r-1){p=r;flag=1;}
	}
	//cout<<"p="<<p<<"\n";
	flag=0;
	while(flag!=1){
	r = rand() % int (pow(2,Max_bits)-1) + int(pow(2,(Max_bits-1)));
	if(phi_fun(r)==r-1 && r!=p){q=r;flag=1;}
	}
	//cout<<"q="<<q<<"\n";*/
	p=2357;
	q=2551;
	k = p*q;
	phi_value=(p-1)*(q-1);
	cout<<"modulo:"<<k<<"\tphi="<<phi_value<<"\n";
	flag=0;
	while(flag!=1){
	   r = rand() % phi_value + 2;
                  if(gcd(r,phi_value)==1)
			{ e = r;flag=1;}
		}
	cout<<"key:"<<e<<"\n";
	flag=0;
	while(flag!=1){
	r = private_key(e,phi_value);
	if(r>0 && r<phi_value){seck=r;flag=1;}
	}
	cout<<"secret="<<seck<<"\n";
	list[0] = k;
	list[1] = e;
	list[2] =seck;
	
return list[3];

}
long  int exponen(long  int a,long  int k,long  int n, long  int array[]){	
	
	long int b,D;
	D=a;
	if(array[0]==1){
		b=a;}
	else {b=1;}
	long int N=log2(k);
	for(int i=1;i<=N;i++){
		D = (D*D)%n;
		if(array[i]==1){
				b = (D*b)%n;}
	}
return b;}
long  int encrypt(long  int key,long  int modulo,long  int m){

	long  int r,C,temp;
	temp=key;
	long  int N= log2(key),key_array[N];

	for(int i=0;i<=N;i++){
		r=temp%2;
		key_array[i]=r;
		temp=temp/2;}
	C=exponen(m,key,modulo,key_array);
return C;
}
long  int decrypt(long  int key,long  int modulo,long  int C){
		
		long  int m,r,temp;
		temp=key;
		long  int N= log2(key),key_array[N];
	
		for(int i=0;i<=N;i++){
		r=temp%2;
		key_array[i]=r;
		temp=temp/2;}
		
		m=exponen(C,key,modulo,key_array);
	
return m;
}
int main()
{	
	users A;
	users B;
	long  int msg =5234673;
	long  int C;
	srand (time(NULL));
	key_generator();
	A.pk.n = list[0];
	A.pk.E = list[1];
	A.sk = list[2];
//	key_generator();
//	B.pk.n = list[0];
//	B.pk.E = list[1];

	C = encrypt(A.pk.E,A.pk.n,msg);
	cout<<"Cypher Text:"<<C<<"\n";
	 cout<<"Message:"<<decrypt(A.sk,A.pk.n,C)<<"\n";

return 0;
}

