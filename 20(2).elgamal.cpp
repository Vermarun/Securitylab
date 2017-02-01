#include<iostream>
#include<stdlib.h>
#include<time.h>
#include<math.h>
using namespace std;
long int order;
long int c[2];
long int gcd(long int a ,long int b){
	long int r;
	while(b!=0){
		r=a%b;
		a=b;
		b=r;}
return a;
}

long int phi_fun(long int n){
	long int count =0;
	for(int i=1;i<n;i++){
		if(gcd(n,i)==1){	
			count++;}
	}
return count;
}
long int expo(long int a,long int k,long int n){

	long int b=1,A;
	A=a;

	if(k==0){

		return b;}

	if(k & 1){

		b=a;}

	for(long int i=1;i<=log2(k);i++){

		A = (A*A)%n;
	
			if(k & (long int)pow(2,i)){
					b = (A*b)%n;}

//		cout<<"\n"<<A<<"\t"<<b;
		}

return b;
}
long int check_cyclic(long int n,long int a){
	
	long int phi_value;
	phi_value = phi_fun(n);
	if(gcd(n,a)==1){
			for(long int i=1;i<=phi_value;i++){
				if(phi_value %i==0){
					if(expo(a,i,n)==1){
						order=i;
					//	cout<<"\n Order ="<<order<<"\n";
					
					break;}
				}
			}
	}
	if(order==phi_value){return a;}
}
long int encryption(long int n,long int m,long int h,long int g){

	long int r , s;
	m=m%n;
	r = rand() % (order-1) +1;
	s=expo(h,r,n);
	c[0]=expo(g,r,n);
	c[1]=m*s;

return c[2];
	
}
long int decryption(long int a,long int n){

	long int s,m;
	s = expo(c[0],a,n);
	m = c[1]/s;
return m;

}
int main(){

	long int n,g,h,a;

	n=2357;
	a=1751;
	long int m ;
	cout<<"\n Enter the msg:";
	cin>>m;
	long int C[2];
//	int phi_value;
//	int temp;	
//	cout<<"enter the modulo:";cin>>n;cout<<"\n";
//	cout<<"enter the integer:";cin>>g;cout<<"\n";
//	phi_value= phi_fun(n);
//	cout<<phi_value<<"\n";
	cout<<"\nphi_value="<<phi_fun(n);
	for(g=2;g<=n-1;g++){
		
			if(check_cyclic(n,g)==g){
			cout<<"\n Generator="<<g<<"\n";
			h=expo(g,a,n);
			cout<<"\npublic key="<<h;
			break;	}

	}
	encryption(n,m,h,g);
	cout<<"\n encrypted msg:";
	for(int i=0;i<2;i++){cout<<"\n"<<c[i]<<"\t";}
	cout<<"\ndecrypt:"<<decryption(a,n);
return 0;

}
