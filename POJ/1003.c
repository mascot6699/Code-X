#include<stdio.h>
#include<string.h>
#include<math.h>

int test;
double sum;
int main()
{
	while(scanf("%lf",&sum)!=0.00){
	int i=2;
	if(sum==0.00) break;
	while(sum>=0){
		sum = sum - (1.0/i);
		i++;
	}
	printf("%d card(s)\n",i-2);
    }

	return 0;
}


