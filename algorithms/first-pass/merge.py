
# Merge sort basics
# Step 1: split into smaller lists
# [5 9 3 7 2 8 1 6]
# [5 9 3 7] [2 8 1 6]
# [5 9] [3 7] [2 8] [1 6]
# [5] [9] [3] [7] [2] [8] [1] [6]
# ​
# Step 2: merge
# [5] [9] [3] [7] [2] [8] [1] [6]
# [5 9] [3 7] [2 8] [1 6]
# [3 5 7 9] [1 2 6 8]
# [1 2 3 5 6 7 8 9]
# ​
# To merge, walk along the two lists with two different indexes, and move the
# smaller number into the destination list and advance that list's index. Repeat
# until both lists are empty.



def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[len(arr) // 2:])
        right = merge_sort(arr[:len(arr) // 2])

        merge(left,right)

        return arr