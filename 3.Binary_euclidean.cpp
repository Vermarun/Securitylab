#include<iostream>

using namespace std;

int gcd(int a ,int b){

	if(a==0 && b==0 || b==0){

			return 0;}

	else if(a==0){
		
		return b;}

	else if(a%2 == 0 && b%2!=0){

		gcd(a/2,b);}

	else if ( a%2!=0 && b%2==0){

		gcd(a,b/2);}
		
	else if ( a%2==0 && b%2==0){

		return(2*gcd(a/2,b/2));}

	else{

		if(a>=b)	
			{
				
				gcd((a-b)/2,b);}
		else{
			
			gcd((b-a)/2,a);}
	}
}
int main(){
		int a,b;

	cout<<"enter the values of a & b:\n";

	cin>>a>>b;

	cout<<"GCD= "<<gcd(a,b)<<"\n";

	return 0;

}

