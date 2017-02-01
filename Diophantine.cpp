#include<iostream>
#include<math.h>
using namespace std;

int gcd(int a ,int b){

	if(a<b){
	int temp;
	temp=a;
	a=b;
	b=temp;}
	int r;
	if (b==0){
		return a;	
	}
	else 
		{r = a % b;
		
	gcd(b,r);}
}
int main ()
{
	int a,b,c,x,y,val,t,q,r;//ax+by=c
	int x1=0,x2=1,y1=1,y2=0,x0,y0;
	cout<<"\n enter the values:\n";
	cout<<"a=";cin>>a;cout<<"\n";
	cout<<"b=";cin>>b;cout<<"\n";
	cout<<"c=";cin>>c;cout<<"\n";
	cout<<"\nequation:"<<c <<"="<< a<<"*x+"<<b<<"*y\n";
	
	val = gcd(a,b);
	
	cout<<"\n gcd ="<<val<<"\n";
	if(c%val==0)
	{
		cout<<"\n solution exist\n";
		t=c/val;

	    if (b==0){

		x0=1;
		y0=0;

		}
	    else
		{
		while(b>0){
			q = floor(a/b);
			r = a - q*b;
			x0 = x2 - q*x1;
			y0 = y2 - q*y1;
			a = b;
			b = r;
			x2 = x1;
			x1 = x0;
			y2 = y1;
			y1 = y0;

			}
	
		x0 = x2;
		y0 = y2;
		x=t*x0;
		y=t*y0;
		cout<<"\n x="<<x<<"\t y="<<y;
		}
	}
	else
		{cout<<"\n solution does not exist\n"; }
		
	
return 0;
}
	
