PRINT_TYLER = 1
HALT = 2 
SAVE_REG = 3 # like LDI
PRINT_REG = 4 # like PRN

memory = [
    PRINT_TYLER,
    SAVE_REG,
    0,
    99,
    PRINT_REG,
    0,
    HALT
]

registers = [0] * 8


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

    else:
        print(f'unknown instruction at address{pc} ')