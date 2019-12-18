# Stack, grows downward

# When you make a function call, a stack frame is allocated (pushed)
# when you return from a function, the stack frame is deallocated (popped)

# stack frame is space for all locals, and for the return address

# R0 14(return value)

# 701: 0 <--- sp
# 
# 700 : [return point 1] |
# 699: a ??              | --- mains stack frame 
# 698: b ??              | 

# 697: [return point 2]
# 696: x 2
# 695: y 7
# 694: z 14


def mult2(x,y):
    z = x * y

    return z

def main():
    a = 2

    b = mult2(a ,7) 

    print(b)

    return

main() 
# return point 1