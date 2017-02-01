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
	int a,b,c,x,y,val,t,q,r;//a*x=c (mod b)
	int x1=0,x2=1,y1=1,y2=0,x0,y0;
	cout<<"\n enter the values:\n";
	cout<<"a=";cin>>a;cout<<"\n";
	cout<<"b=";cin>>b;cout<<"\n";
	cout<<"c=";cin>>c;cout<<"\n";
	val = gcd(a,b);
	int A = a;
	int B = b;
	cout<<"\n gcd ="<<val<<"\n";
	t=c/val;
	if(c%val==0)
	{
		cout<<"\n solution exist\n";
		
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
		x=t*x0;
		cout<<"\n x="<<x;}
		
	 }
	else
		{cout<<"\n solution does not exist\n"; }
	cout<<"\n other solutions:\n";
	for(int i=0;i<val;i++){
			int sal;
			sal =x+(B/val)*i;
			cout<<"x"<<":"<<sal<<"\n";
			
		}
	
return 0;
}
	

