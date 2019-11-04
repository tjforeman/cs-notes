def process(l):
    t= 0

    t += l[0]


    t += l[1]

    return t

    #0(1 + 1 + 1 + 1) == 0(4) == 0(4*1) == 0(1)

def process2(l):
    t= 0        #0(n)

    t += l[0]   #0(n)

    for i in l: # 0(n) <--- loops get the 0(num_of_loops)
        t +=i       #0(n)
        
    t += l[1]   #0(n)

    return t

# 0(1 + 1) + 0(n * 1) + 0(1 + 1)
# 0(1) + 0(n)
# 0(n + 1)
# 0(n)

def process3(l):
    t = 0 #0(1)

    for i in range(10000): # 0(10000)
        t += l[0]  # 0(1)

    return t # 0(1)

# 0(1 + 10000 * 1 + 1) == 0(10002) == 0(10000 *1) 