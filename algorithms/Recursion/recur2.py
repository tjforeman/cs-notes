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


def fib_bottom_up(n): # 0(n) time complexity 0(1) space complexity 
    if n == 0: return 0
    if n == 1: return 1

    p2 = 0
    p = 1

    count = 0


    while count < n-1:
        c= p + p2
        p2 = p
        p = c 
        

        count += 1

    return c  

    
for i in range(100):
    print(f'{i}: {fib_bottom_up(i)}')


def fib_top_down_dynamic(n):


    cache = {}
    
    def fib2(n):

        nonlocal cache


        if n == 0: return 0
        if n == 1: return 1
     
        if n not in cache:
            cache[n] = fib2(n-1) + fib2(n-2)

        return cache[n]

    return fib2(n)

for i in range(100):
    print(f'{i}: {fib_top_down_dynamic(i)}')