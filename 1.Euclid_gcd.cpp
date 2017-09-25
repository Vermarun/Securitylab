#include<iostream>
using namespace std;


// computr gcd of given numbers 
int gcd(int a ,int b){

	int r;
	if (b==0){
		return a;	
	}
	else 
		{r = a % b;
		
	gcd(b,r);}
}

int main(){
	
	int a ,b;
	cout<<"\n enter the values of a & b (a>=b)";
	cin>>a>>b;
	 cout<<"\n gcd ="<<gcd(a,b);
return 0;
}
