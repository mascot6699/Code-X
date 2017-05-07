N, M = map(int, input().split())
rows = [input() for _ in range(N)]
K = int(input())

for row in sorted(rows, key=lambda x: int(x.split()[K])):
    print(row)
