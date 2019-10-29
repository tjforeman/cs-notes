# References Vs Values 

# value types (ints, floats, strings)
# A copy of te arg goes in the paramater
def foo(x):
    print(f'x is {x}')
    x= x+30
    print(f'x is now {x}')

a=20
foo(a)
print(a)

print(f'a is {a}')

#reference types (lists, dicts, objects)

l = [1,2,3]

def bar(x):
    x.append(4)

bar(l)

print(l)