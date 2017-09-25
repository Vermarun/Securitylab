#include<iostream>
using namespace std;


<<<<<<< HEAD
// compute gcd of given numbers a & b
=======
// computr gcd of given numbers 
>>>>>>> 41a92ed0cd181ee3c562aa956e24ba2ecaf22ab8
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
