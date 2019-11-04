# takes the same amount of time regardless of the length of the list
# "constant time "
# 0(1) "order 1" Big-O notation 
def process(l):
    first_val = l[0]

    return first_val

# len(l) | num of operations
# ---------------------------------
#   1    |    2
#   2    |    2
#   3    |    4

# Double the length of l, alg takes 2x as long to process 
# "Linear time"
# O(n) "Order n"
def processs(l):
    t=0 

    for v in l:
        t+=v
        
    return t

def proc(n): # n is an int
    for _ in range(n): # O(n)
        pass

# n   |  n^2  | number of ops
# ---------------------------
# 1   |   1   |       1 
# 2   |   4   |       4
# 3   |   9   |       9
# 4   |   16  |       16

def procs(n): # n is an int
    for _ in range(n**2): # O(n)
        pass