# 1. When we call:
    #save the return address on the stack
    #set the PC to the subroutine address 
# 2 When we return:
    # Pop return address off the stack and store in PC 

    
# 00 CALL sub1
# 01 CALL sub1
# 02 CALL sub1
# 03 HALT

# sub1:

# 04 PRINT_TYLER sub1
# 05 PRINT_TYLER
# 06 CALL sub2
# 07 PRINT_TYLER
# 08 RET

# 09 PRINT_NUM 99 sub2
# 0A RET

# .
# .
# .
# F1: 00
# F2: 07
# F3: 01 
# F4: 00  <-- SP