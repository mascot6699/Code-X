from itertools import combinations

str1, n = input().split(" ")
str1 = sorted(str1)
allcombs = ["".join(combs) for i in range(1, int(n)+1) for combs in combinations(str1, i)]
print(*allcombs, sep='\n')
