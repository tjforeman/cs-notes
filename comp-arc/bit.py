# Bitwise opperations

# A B  A AND B & operator
# -------------
# F F    F
# T F    F
# F T    F
# T T    T

# A B  A AND B
# -------------
# 0 0    0
# 1 0    0
# 0 1    0
# 1 1    1

if False and False:
    print('hello')
    # prints nothing
if True and False:
    print('hello')
    # prints nothing

if True and True:
    print('hello')
    # prints hello

# A B   A OR B | operator 
# -------------
# F F     F
# T F     T
# F T     T
# T T     T  

# A B   A OR B 
# -------------
# 0 0     0
# 1 0     1
# 0 1     1
# 1 1     T  



#   1010101 
# & 1101011
# ---------
#   1000001
# ---------
#      65 

#     vv
#   1110101
# & 0011000   Mask (how to pull individual bits)
# -----------
#   0010000

# Shifting 
#   0010000
#    001000   


#   vv
#   10100010
# & 11000000
# ----------
#   10000000 >> 6
#   ^^

#   >> right shift  

# ir = 0b10100010  MUL
# length = ((ir &0b10100010 ) >> 6) +1