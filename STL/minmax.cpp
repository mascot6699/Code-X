#include <iostream>
#include <algorithm>
using namespace std;
int main () {
  pair<int,int> result = std::minmax({1,2,3,4,5});

  std::cout << "minmax({1,2,3,4,5}): ";
  std::cout << result.first << ' ' << result.second << '\n';
  return 0;
}
