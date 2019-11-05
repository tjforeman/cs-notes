# If default params are reference types, don't do this

def foo(a=[]):
    a.append(5)
    return a

def foo2(a=None):
    if a is None:
        a= []
        a.append(5)
        return a
