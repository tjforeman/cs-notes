# List Comprehensions 

a = [2, 3, 6, 7, 9, 12, 4]

# evens = []
# for i in a:
#     if i % 2 == 0:
#         evens.append(i) 

evens = [i for i in a if i % 2 == 0 ]

print(evens)