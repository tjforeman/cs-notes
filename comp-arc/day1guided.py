import sys

# sys.exit(sys.argv)

PRINT_TYLER = 1
HALT = 2 
SAVE_REG = 3 # like LDI
PRINT_REG = 4 # like PRN
PUSH = 5
POP = 6
CALL = 7
RET = 8

memory = [0] * 256
# memory = [
#     PRINT_TYLER,
#     SAVE_REG,
#     0,
#     99,
#     PRINT_REG,
#     0,
#     HALT
# ]
# int(s ,2 (base 2 number))
registers = [0] * 8

SP = 7

filename = sys.argv[1]
address = 0

with open(filename) as f:
    for line in f:
        n= line.split('#')
        n2 = n[0].strip()        
        if n2 == '':
            continue

        val = int(n2)
        memory[address] = val
        address += 1 

running = True
pc = 0 # program counter index into memory of current instruction

while running:
    current_instruction = memory[pc]

    if current_instruction == PRINT_TYLER:
        print('Tyler!')
        pc += 1

    elif current_instruction == HALT:
        running = False

    elif current_instruction == SAVE_REG:
        reg_num = memory[pc + 1] # operand A
        value = memory[pc + 2] # operand B 
        registers[reg_num] = value
        pc += 3

    elif current_instruction == PRINT_REG:
        reg_num = memory[pc+1]
        print (registers[reg_num])
        pc += 2

    elif current_instruction == PUSH:
        # decrement stack pointer(reg7)
        # copy value from register to memory at sp
        registers[SP] -= 1

        reg_num = memory[pc + 1]
        value = registers[reg_num]
        memory[registers[SP]] = value

        pc += 2

    elif current_instruction == POP:
        # copy the value from the top of the stack into the given register
        reg_num = memory[pc + 1]
        value = memory[registers[SP]]
        registers[reg_num] = value

        # increment SP
        registers[SP] +=1
        pc += 2

    elif current_instruction == CALL:
        # push the return address onto the stack
        return_address = pc + 2
        registers[SP] -= 1
        memory[registers[SP]] = return_address

        # set the PC to the value in the register
        reg_num = memory[pc + 1]
        sub_address = registers[reg_num]
        pc = sub_address

        # pc += 2 DON'T DO THIS

    elif current_instruction == RET:
        # pop the return address off of the stack
        return_address= memory[registers[SP]]
        registers[SP] += 1
        # store it in the pc 
        pc = return_address

    else:
        print(f'unknown instruction at address{pc} ')