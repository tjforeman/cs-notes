# pass is a function body that does nothing, however it's a syntax error for a function to not have a body 
#def foo():
    # pass

def foo(a, b=99, *args, **kwargs):
    print(f"{a} {b}")
    print(args)
    print(kwargs)

#foo(1,2)
foo(1,2, 4, 9, 30, c=12,d=89,e=1)

# x={
#     "c":12,
#     "d":89,
#     "e":-1,
# }

# foo(1, 3, **x)

x = [1,2,3,4]
y = [6,7,*x]
print(y)