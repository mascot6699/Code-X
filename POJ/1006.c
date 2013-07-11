#include<stdio.h>
#include<string.h>
#include<math.h>

int a,b,c,d,i,ans;
int main()
{
	while(scanf("%d %d %d %d",&a,&b,&c,&d)==4){
		
		if(a==-1 && b==-1 && c==-1 && d==-1)break;
		ans =(5544*(a%23)+14421*(b%28)+1288*(c%33))%21252-d;
		if(ans<=0)ans = ans + 21252;
		printf("Case %d: the next triple peak occurs in %d days.\n",i,ans);
		i++;
	}
	
	return 0;
}


