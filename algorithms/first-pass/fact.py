# Factorial 

# n is a non-negative interger

# 0! = 0
# 1! = 1
# n! = n* (n - 1) * (n - 2) * ... * 1

# 3! = 3 * 2 *1
# 5! = 5 * 4 * 3 * 2 * 1 
# 8! = 8 * 7 * 6 * 5 * 5 * 3 * 2 * 1 

def fac(n): # 0(n) time complexity, 0(n) space complexity
    if n == 0: 
        return 1
    return n * fac(n - 1)
    
for i in range (22):
    print(f'{i}: {fac(i)}')

    def fac_iterative(n): # 0(n) time complexity, 0(1) space complexity
        if n == 0: 
            return 1

        r = 1 
        for i in range(1, n + 1 ):
            r*i 
            return r
    # return n * fac(n - 1)
    
for i in range (22):
    print(f'{i}: {fac(i)}')