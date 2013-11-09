//use of find algorithm on various stl containers
//format iterator = find(first , last , value)
//find function returns an iterator that refers to the first occurence of value (zero-based indexing)
//it returns "off-the-end" iterator which is same iterator returned by end member functions

#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<vector>
#include<list>
#include<deque>

using namespace std;

int main()
{
// with simple array
char* s = "C++ is better than C";
int len = strlen(s);
char* where = find(&s[0],&s[len],'e');
if(where !=&s[len])cout<<"Successfully found"<<endl;
if(where == &s[8])cout << "that too at correct position";
cout <<" which is " << (where-s)+1 <<endl<<endl;

//with vectors
int arr[10] = {1,2,3,4,5,6,7,8,9,10};
vector<int>v1(arr, arr+9);
vector<int>::iterator where1 = find(v1.begin(),v1.end(),4);
if(where1 != v1.end())cout << "Successfull"<<endl<<endl;

//with list
list<char>list1(&s[0],&s[len]);
list<char>::iterator where3 = find(list1.begin(),list1.end(),'d');
if(where3 == list1.end()) cout<< "failed"<<endl<<endl;

//with deque
deque<char>deque1(&s[0],&s[len]);
deque<char>::iterator where4 = find(deque1.begin(),deque1.end(),'t');
if(where4 != deque1.end())cout << "Successfull"<<endl<<endl;

return 0;
}
