#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<iostream>

using namespace std;
int i;

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
	cout<<endl <<"union example \t\t\t";
	
	//union
	char a11[8] = {'a','b','c','d','e','f','g','h'};
	char a22[5] = {'a','e','i','o','u'};
	vector<char> a3(100);
	int len11 = strlen(a11);
	int len22 = strlen(a22);
	set_union(&a11[0],&a11[len11],&a22[0],&a22[len22],a3.begin());
	for(i=0;i<a3.size();i++)
	cout<<a3[i];
	
	cout<<endl <<"intersection example \t\t";	
	//intersection
	vector<char> a4(100);
	set_intersection(&a11[0],&a11[len11],&a22[0],&a22[len22],a4.begin());
	for(i=0;i<a4.size();i++)
	{cout<<a4[i];}
	
	cout<<endl <<"difference example \t\t";
	//difference (ie in first but not in second)
	vector<char> a5(100);
	set_difference(&a11[0],&a11[len11],&a22[0],&a22[len22],a5.begin());
	for(i=0;i<a5.size();i++)
	{cout<<a5[i];}
	
	//symmmetrric difference (ie that are in one but not both)
	cout<<endl <<"symmetric difference example \t";
	vector<char> a6(100);
	set_symmetric_difference(&a11[0],&a11[len11],&a22[0],&a22[len22],a6.begin());
	for(i=0;i<a6.size();i++)
	{cout<<a6[i];}
	
	return 0;
}


