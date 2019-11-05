# Recursion

# Definitions that refer to themselves
# 0 1 2 3 4 5 6 7  8  9  10  
#  
                          
# 0 1 1 2 3 5 8 13 21 34 55

# fib(n):
#     if n == 0: 0
#     if n == 1: 1
#     else fib(n-1) + fib(n-2)

def fib(n):
    if n == 0: return 0
    if n == 1: return 1

    return fib(n-1) + fib(n-2)

for i in range(10):
    print(f'{i}: {fib(i)}')