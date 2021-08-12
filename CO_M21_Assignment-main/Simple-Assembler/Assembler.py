opcode = {"add": "00000", "sub": "00001", "movi": "00010", "movr": "00011", "ld": "00100",
          "st": "00101", "mul": "00110", "div": "00111", "rs": "01000", " ls": "01001",
          "xor": "01010", "or": "01011", "and": "01100", "not": "01101", "cmp": "01110",
          "jmp": "01111", "jlt": "10000", "jgt": "10001", "je": "10010", "hlt": "10011"}

register = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101",
            "R6": " 110", "FLAGS": "111"}

types = {"add": "A", "sub": "A", "movi": "B", "movr": "C", "ld": "D",
         "st": "D", "mul": "A", "div": "C", "rs": "B", " ls": "B",
         "xor": "A", "or": "A", "and": "A", "not": "C", "cmp": "C",
         "jmp": "E", "jlt": "E", "jgt": "E", "je": "E", "hlt": "F"}


def decToBinary(n):
    s = bin(n)
    s = s[2::]
    s = "0" * (8 - len(s)) + s
    return s


def assemblyCode(line):
    inst = line.split()
    # For deciding if it is immediate move or register move
    if inst[0] == "mov":
        if inst[2][1] == "R":
            inst[0] = "movr"
        else:
            inst[0] = "movi"

    #
    if types[inst[0]] == "A":
        return(opcode[inst[0]] + "0" * 2 + register[inst[1]] + register[inst[2]] + register[inst[3]])
    elif types[inst[0]] == "B":
        return(opcode[inst[0]] + register[inst[1]] + decToBinary(int(inst[2])))
    elif types[inst[0]] == "C":
        return(opcode[inst[0]] + "0" * 5 + register[inst[1]] + register[inst[2]])
    elif types[inst[0]] == "D":
        return(opcode[inst[0]] + "0" * 3 + decToBinary(int(inst[1])))
    elif types[inst[0]] == "E":
        return(opcode[inst[0]] + "0" * 3 + decToBinary(int(inst[1])))
    elif types[inst[0]] == "F":
        return(opcode[inst[0]] + "0" * 11)


# st = input("code:  ")
# assemblyCode(st)
