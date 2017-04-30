import math

def is_prime(n):
    if (n in [2,3]):
        return "Prime"
    if (n%2==0 or n%3==0 or n<=1):
        return "Not prime"
    sqrt = int(math.sqrt(n))+1
    for i in range(5, sqrt, 2):
        if n % i == 0:
            return "Not prime"
    return "Prime"
p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    print(is_prime(n))

