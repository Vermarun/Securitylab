#include<iostream>
#include<fstream>
using namespace std;


int prime(int list[],int n,int p){


	for(int i=0;i<n;i++){

		if(list[i] > p && list[i]%p == 0){

			list[i] = 0;
		}
	}
	int temp = p;
	for(int i=0;i<n-1;i++){

		if(list[i]!=0 && list[i]>p){

			p=list[i];
			break;
			}
		}
	
	if(temp!=p){
		prime(list,n,p);}



	
}	


int main(){

	int n,p;
	int count=0;
	int list[1000000];
	ofstream myfile;
	myfile.open("prime.txt",ios::app);	
	cout<<"enter the range till where you want to find prime numbers:\n";
	p=2;
	cin>>n;
	for(int i=0;i<n-1;i++){

		list[i]=2+i;}


	prime(list,n,p);

//	cout<<"prime numbers:\n";

	for(int i=0;i<n-1;i++){

		if(list[i]!=0){
			count++;
			cout<<list[i]<<"\t";}
	}
	
	myfile<<n<<"\t\t"<<count<<"\n";
	myfile.close();
	cout<<"\n total number of primes:"<<count<<"\n";
return 0;
}
