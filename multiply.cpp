#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>

using namespace std;
long long a , b, result;
long long mul(long long a,long long b){
	result =0;
	while(a>=1){
    if(a%2==1)
	result = result + b;
	a = a>>1;
	b = b<<1;	
	}
	
	return result;
}
int main()
{   while(1){
	cin >>a >> b;
	cout << mul(a,b)<<endl;
}
	return 0;
}


