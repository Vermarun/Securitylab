#include<iostream>

#include<math.h>

using namespace std;

int expo(int a,int k,int n){

	int b=1,A;
	A=a;

	if(k==0){

		return b;}

	if(k & 1){

		b=a;}

	for(int i=1;i<=log2(k);i++){

		A = (A*A)%n;
	
			if(k & (int)pow(2,i)){
					b = (A*b)%n;}

		cout<<"\n"<<A<<"\t"<<b;
		}

return b;
}

		
int main(){

	int a,k,n,r;
			
	cout<<"\n enter the values\n a=";
	cin>>a;
	cout<<"\n k=";cin>>k;
	cout<<"\n n=";cin>>n;

	cout<<"Ans="<<expo(a,k,n)<<"\n";
return 0;
}
