#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<iostream>

using namespace std;
int test;
int main()
{
	//for subsequence
	char *a1 = "abcdefghijklmnopqrstuvwxyz";
	char *a2 = "giky";
	int len1 = strlen(a1);
	int len2 = strlen(a2);
	bool result = includes(&a1[0],&a1[len1],&a2[0],&a2[len2]);
	if(result)
	{cout<< "yes a subsequence"<<endl;}
	else
	{cout<< "no, not a subsequence"<<endl;}
	
	//for substring
	char *a11 = "abcdefghijklmnopqrstuvwxyz";
	char *a22 = "xz";
	int len11 = strlen(a11);
	int len22 = strlen(a22);
	char* result1 = search(&a11[0],&a11[len11],&a22[0],&a22[len22]);
	if(result1-a11<len11)
	cout<<"success and matched at " << result1-a11 <<endl;
	else
	{cout<< "no, not a substring"<<endl;}



	return 0;
}


