#include<iostream>
using namespace std;


// compute gcd of given numbers a & b
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
	// give the values for which gcd needs to be computed 
	cout<<"\n enter the values of a & b (a>=b)";
	cin>>a>>b;
	 cout<<"\n gcd ="<<gcd(a,b);
return 0;
}
