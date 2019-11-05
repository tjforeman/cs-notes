# Quicksort

# Look for problems that are made up of identical subproblems

# Partitioning
# [5 9 3 7 2 8 1 6]
#  ^
#  p      
# 
# 
# [3 2 1] [5] [9 7 8 6]
#  ^           ^ 
#  p           p
#   p = pivot
#  5 will never move even when the list is completely sorted 


def partition(l):
    left = []
    pivot = l[0]
    right = []

    for v in l[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)
    return left, pivot, right

def quicksort(l):
    if len(l) <= 1:
        return l
    left,pivot,right = partition(l)

    return quicksort(left) + [pivot] + quicksort(right)

data = [5, 9, 3, 7, 2, 8, 1, 6]
print(quicksort(data))

