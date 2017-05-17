from itertools import permutations

str1, n = input().split(" ")
for perms in permutations(sorted(str1), int(n)):
    print("".join(perms))
