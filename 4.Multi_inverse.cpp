#include<iostream>
#include<math.h>
using namespace std;

//input a number a and mod b

// Output a^(-1)mod b

int main(){
	int a,b,d,x,y,q,r;//d=ax+by
	int x1=0,x2=1,y1=1,y2=0;
	cout<<"\n enter the values of a & b(a>=b)\n";
	cin>>a>>b;

	if (b==0){
		d = a;
		x=1;
		y=0;
		cout<<"\n d="<<d<<"\t x="<<x<<"\t y="<<y;
	}
	else
		{
		while(b>0){
			q = floor(a/b);
			r = a - q*b;
			x = x2 - q*x1;
			y = y2 - q*y1;
			a = b;
			b = r;
			x2 = x1;
			x1 = x;
			y2 = y1;
			y1 = y;

			}
		d = a;
		x = x2;
		y = y2;
		
		if(d>1){
			cout<<"Multiplicative inverse of a mod b doesn't exist.";
			}
		else{
			if(x<0){x = x+b;}
			cout<<"Multiplicative inverse of a mod b is:"<<x<<"\n";}
		}
	
	return 0;
}
