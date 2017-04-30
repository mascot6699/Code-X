table = [0]*40
table[0] = 1
table[1] = 1
table[2] = 2

def count_of_styles_to_jump(size):
    global table
    for i in range(table.index(0), size+1):
        table[i] = table[i - 1] + table[i - 2] + table[i - 3]
    return table[size]

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(count_of_styles_to_jump(n))
