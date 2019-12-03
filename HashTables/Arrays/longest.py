import random 

def longest_link(keys, buckets, loops=10):
# """"
# Rolls 'keys' number of random keys into buckets and count collisions

# run 'loops' number of times

# """"

    for i in range(loops):
        key_counts = {}

        for i in range(buckets):
            key_counts[i] = 0

        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1
        # count and find the largest linked list chain (index where we had the most collisions)

        largest_number = 0

        for key in key_counts:
            if key_counts[key] > largest_number:
                largest_number = key_counts[key]
        
        print(f'longest linked list chain for {keys} keys in {buckets} buckets (load factor {keys/buckets:2f} : {largest_number} )')

longest_link(4,5,10)