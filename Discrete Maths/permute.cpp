#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
unsigned long long test,t,t2,t1,i,ans,arr[100];

int main()
{
	cin >> test;
	//t = 1000000000000000000;
//	cout << t;
	i=1;
	while(i<30)
	{t1 =1;t2=1;ans =0;
	while(t2<=i){t1 = t1*test;ans = ans + t1;t2++;}
	arr[i]=ans;
	cout<<arr[i]<<"  ";
	i++;}
	
	return 0;
}


