fib = [0]*40
fib[0] = 0
fib[1] = 1
fib[2] = 1

def fibonacci(size):
    global table
    for i in range(fib[1:].index(0), size+1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[size]

n = int(input())
print(fibonacci(n))
