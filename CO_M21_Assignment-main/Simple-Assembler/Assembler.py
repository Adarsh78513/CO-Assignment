import re

opcode = {
    "add": ("00000", "A"),
    "sub": ("00001", "A"),
    "movi": ("00010", "B"),
    "movr": ("00011", "C"),
    "ld": ("00100", "D"),
    "st": ("00101", "D"),
    "mul": ("00110", "A"),
    "div": ("00111", "C"),
    "rs": ("01000", "B"),
    "ls": ("01001", "B"),
    "xor": ("01010", "A"),
    "or": ("01011", "A"),
    "and": ("01100", "A"),
    "not": ("01101", "C"),
    "cmp": ("01110", "C"),
    "jmp": ("01111", "E"),
    "jlt": ("10000", "E"),
    "jgt": ("10001", "E"),
    "je": ("10010", "E"),
    "hlt": ("10011", "F")
}

register = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": " 110",
    "FLAGS": "111"
}


def decToBinary(n):
    s = bin(n)
    s = s[2::]
    s = "0" * (8 - len(s)) + s
    return s


def assemblyCode(inst, labels, varIdx):
    if inst[-1] == "FLAGS" and inst[-3] != "mov":
        print("Illegal use of FLAGS")
        exit()    

    if inst[0][0:-1] in labels:
        if len(inst) < 2:
            print("Wrong Syntax")
            exit()
        try:
            b = inst[1] in opcode
        except:
            print("Wrong Syntax")
            exit()      

    if inst[0] in opcode or inst[0] == "mov":
        if inst[0] != "hlt":
            if len(inst) < 2:
                print("Wrong Syntax")
                exit()

    i = 0
    if inst[0] != "hlt" and (inst[1] in opcode):
        i += 1

    # For deciding if it is immediate move or register move
    if inst[i] == "mov":
        if inst[i + 2][0] == "R" or inst[i + 2] == "FLAGS":
            inst[i] = "movr"
        else:
            inst[i] = "movi"

    if (inst[i] not in opcode):
        print("invalid instruction name")
        exit()

    type = opcode[inst[i]][1]
    op = opcode[inst[i]][0]

    if type == "A":
        if len(inst) != i + 4:
            print("Wrong Syntax")
            exit()
        
        for j in range(1, 4):
            if inst[i + j] not in register:
                print("Invalid register")
                exit()
        return op + "0" * 2 + register[inst[i + 1]] + register[inst[i + 2]] + register[inst[i + 3]]

    elif type == "B":
        if len(inst) != i + 3:
            print("Wrong Syntax")
            exit()
        
        if inst[i+1] == "FLAGS":
            print("Illegal use of FLAGS")
            exit()

        for j in range(1, 2):
            if inst[i + j] not in register:
                print("Invalid register")
                exit()
                
        if 255 < int(inst[i + 2][1::]) < 0:
            print("Invalid immediate value")
            exit()
            
        return op + register[inst[i + 1]] + decToBinary(int(inst[i + 2][1::]))

    elif type == "C":
        if len(inst) != i + 3:
            print("Wrong Syntax")
            exit()
        
        for j in range(1, 3):
            if inst[i + j] not in register:
                print("Invalid register")
                exit()

        if inst[i+1] == "FLAGS":
            print("Illegal use of FLAGS")
            exit()
        
        return op + "0" * 5 + register[inst[i + 1]] + register[inst[i + 2]]

    elif type == "D":
        if len(inst) != i + 3:
            print("Wrong Syntax")
            exit()
        
        for j in range(1, 2):
            if inst[i + j] not in register:
                print("Invalid register")
                exit()
                
        if inst[i + 2] in labels:
            print("Misuse of label as variable")
            exit()
        if inst[i + 2] not in varIdx:
            print("Use of undefined variable")
            exit()
        return op + register[inst[i + 1]] + decToBinary(int(varIdx[inst[i + 2]]))

    elif type == "E":
        if len(inst) != i + 2:
            print("Wrong Syntax")
            exit()
        
        if inst[i + 1] in varIdx:
            print("Misuse of variable as label")
            exit()
        if inst[i + 1] not in labels:
            print("Use of undefined label")
            exit()
        return op + "0" * 3 + decToBinary(int(labels[inst[i + 1]]))

    elif type == "F":
        if len(inst) != i + 1:
            print("Wrong Syntax")
            exit()
        
        return op + "0" * 11

    else:
        return 0


def main():
    # storing all the instructions in from of lists
    allInsts = []
    # storing all the labels and variable
    labels = {}
    # storing all the var instructions
    varInsts = []
    # storing all the var index
    varIdx = {}
    # storing all the answers
    answer = []  

    while True:
        try:
            st = input().strip().split()
            if len(st) == 0:
                break
            elif st[0] == "var":
                if len(st) != 2:
                    print("Wrong Syntax")
                    exit()
                a = bool(re.match("^[A-Za-z0-9_]*$",st[1])) 
                if a == False:
                    print("Invalid variable name")
                    exit()

                if len(allInsts) == 0:
                    if st in varInsts:
                        print("same variable used again")
                        exit()
                        
                    else:    
                        varInsts.append(st)
                else:
                    print("Declare variable first")
                    exit()
                
            # adding instructions
            elif st[0] != "var":
                allInsts.append(st)
        except EOFError:
            break       
    
    if len(allInsts) == 0:
        print("Blank line in the beginning of the code")
        exit()
    
    for i in range(len(allInsts)):
        if allInsts[i][0] == "mov":
            continue
        if allInsts[i][0] not in opcode:
            if allInsts[i][0][-1] == ":":
                labels[allInsts[i][0][0:-1]] = i
            else:
                print("Wrong Syntax")
                exit()

    j = len(allInsts)
    for i in range(len(varInsts)):
        varIdx[varInsts[i][1]] = j
        j += 1

    for i in range (len(allInsts)-1):
        if allInsts[i][0] == "hlt":
            print("hlt not being used as the last instruction")
            exit()

    if allInsts[-1][0] != "hlt" and (allInsts[-1][1] != "hlt" and allInsts[-1][0][0:-1] in labels):
        print("missing hlt instruction in the end")
        exit()

    for line in allInsts:
        answer.append(assemblyCode(line, labels, varIdx))
    
    for line in labels:
        a = bool(re.match("^[A-Za-z0-9_]*$", line)) 
        if a == False:
            print("Invalid label name")
            exit()

    for i in answer:
        print(i)

if __name__ == "__main__":
    main()
