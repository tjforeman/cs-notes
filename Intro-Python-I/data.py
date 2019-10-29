# Arrays in Python are called Lists 

p = []

q = [10, 60, 20, 5]

print(q[1])

q[1] = 90

print(q[1])

a = 3

print(q[a])

print(q)

for element in q: 
    print("the next element is :")
    print(element)

for i in range(len(q)):
    print("rangey")
    print(q[i])

for i in range(10,30,2):
    print("counting by two")
    print(i)

for i,v in enumerate(q):
    print(f"the value {v} is at index {i}")

for i in "hello":
    print(i)