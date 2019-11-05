# Recursion

# Function that calls itself

def foo(n):
    if n == 0: #base case 
        return 
    print(f'before: {n}')

    foo(n - 1)
    foo(n - 1)

    print(f'after {n}')

foo(4)

# foo(4), n=4
# foo(3) n=3
# foo(2)
# foo(1)
# foo(0)