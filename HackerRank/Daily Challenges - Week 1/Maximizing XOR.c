/*
Given two integers: L and R,
Find the maximal values of A xor B ? L = A = B = R

Input Format
The input contains two lines, L is present in the first line. 
R in the second line.

Constraints
1 = L = R = 103

Output Format
The maximal value as mentioned in the problem statement.

Sample Input
1
10
Sample Output
15
Explanation
The maximum value can be obtained for A = 5 and B = 10,
1010 xor 0101 = 1111 hence 15.
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>

int maxXor(int l, int r) {
int max = 0,i,j,c;
for (i=l;i<=r;i++)
for (j=l;j<=r;j++)
{
c = i ^j;
if(max < c) {
max = c;
}
}
return max;
}
int main() {
    int res;
    int _l;
    scanf("%d", &_l);
    
    int _r;
    scanf("%d", &_r);
    
    res = maxXor(_l, _r);
    printf("%d", res);
    
    return 0;
}

