#include<stdio.h>
#include<string.h>
#include<math.h>

double n , sum=0.0;
int i;
int main()
{
	for(i=0;i<12;i++)
	{
		scanf("%lf",&n);
		sum = sum +n;
	}
	sum = sum/12;
	printf("$%.2lf\n",sum);



	return 0;
}


