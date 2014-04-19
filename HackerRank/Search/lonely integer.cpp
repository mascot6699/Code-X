// https://www.hackerrank.com/challenges/lonely-integer

#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;

int i;

int lonelyinteger(vector < int > a) {
if(a.size()==1)
{
return a.at(0);
}

if(a.at(0)!=a.at(1))
{
return a.at(0);
}

if(a.at(a.size()-2)!=a.at(a.size()-1))
{
return a.at(a.size()-1);
}

for(i=1; i<a.size()-1; i++)
{
if(a.at(i-1)!=a.at(i) && a.at(i)!=a.at(i+1) )
{
return a.at(i);
}
}

}
int main() {
    int res;
    
    int _a_size;
    cin >> _a_size;
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n'); 
    vector<int> _a;
    int _a_item;
    for(int _a_i=0; _a_i<_a_size; _a_i++) {
        cin >> _a_item;
        _a.push_back(_a_item);
    }
    sort (_a.begin(), _a.begin()+_a_size);
    res = lonelyinteger(_a);
    cout << res;
    
    return 0;
}

