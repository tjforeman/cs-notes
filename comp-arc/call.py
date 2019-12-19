3 # SAVE_REG RO,SUB1
0
8 
7 # CALL sub1 R0
0
7 # CALL sub2 R0
0
2 # HALT

# ----sub1-----
1 # PRINT_TYLER sub1
1 # PRINT_TYLER
3 # SAVE_REG R1, sub2
1 # PRINT_TYLER
17
7 # call r1
1
1
8 # RET

# -----sub2-----
4 # PRINT_REG R1
1
8 # RET