#include <stdio.h>

void sieveErat(int *a, int d)
{
     int i, j;
     for(j = 4; j <= d; j += 2) 
           a[j] = 1;
     
     for(i = 3; i <= sqrt(d); i+=2) {
           if(a[i] == 0) {
                   for(j = i*i; j <= d; j += i) 
                         a[j] = 1;
           }
     }
}

void segment(long long m, long long n)
{
     int i, j, *b, *c, d;
     if (m < 2)
        m = 2;
     d = n-m+1;
     b = malloc(sizeof(int) * ((int)sqrt(n) + 1));
     c = malloc(sizeof(int) * d);
     b[0] = b[1] = 1;
     for(i = 2; i <= sqrt(n); i++)
           b[i] = 0;
     for(i = 0; i < d; i++)
           c[i] = 0;
           
     sieveErat(b, (int)sqrt(n));

     for(i = 2; i <= sqrt(n); i++) {
           if(b[i] == 0) {
                   j = m%i;
                   if(j != 0)
                        j = i-j;
                   for(; j < d; j += i)
                         if(m + j != 2 && m+j != 3 && m+j != 5 && m+j != 7)
                         c[j] = 1;
           }
     }

     for(i = 0; i < d; i++) {
           if(c[i] == 0 )
                   printf("%lld\n", m+i);
     }
     printf("\n");
}

int main()
{
    int t, i=0;
    long long *a;
    scanf("%d", &t);
    a = malloc(sizeof(long long) * 2 * t);
    while(i < 2*t) {
               scanf("%lld %lld", &a[i], &a[i+1]);
               i += 2;          
    }
    
    for(i = 0; i < 2*t; i += 2) {
          segment(a[i], a[i+1]);
    }
    return 0;
}
