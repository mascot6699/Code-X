#include<stdio.h>
#include<string.h>
#include<math.h>

double a,n,ans;
double power(double a , double n){
	if(n==0)return 1;
	else if(n==1)return a;
	double t = power(a,n/2);
	
	return t * t* power(a,fmod(n,2));
	
}
int main()
{
	scanf("%lf %lf",&a ,&n);
	ans = power(a,n);
	printf("%lf",ans);
	return 0;
}


