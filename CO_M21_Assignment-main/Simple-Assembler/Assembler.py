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


def assemblyCode(inst,labels):
    # For deciding if it is immediate move or register move
    if inst[0] == "mov":
        if inst[2][0] == "R":
            inst[0] = "movr"
        else:
            inst[0] = "movi"
    #
    i = 0
    if inst[0]!="hlt":
        if inst[1] in opcode :
            i += 1
        
    type = opcode[inst[i]][1]
    op = opcode[inst[i]][0]
    
        
    if type == "A":
        return(op + "0" * 2 + register[inst[i + 1]] + register[inst[i + 2]] + register[inst[i + 3]])
    elif type == "B":
        return(op + register[inst[i + 1]] + decToBinary(int(inst[i + 2][1::])))
    elif type == "C":
        return(op + "0" * 5 + register[inst[i + 1]] + register[inst[i + 2]])
    elif type == "D":
        return(op + "0" * 3 + decToBinary(int(labels.get(inst[1]))))
    elif type == "E":
        return(op + "0" * 3 + decToBinary(int(labels.get(inst[1]))))
    elif type == "F":
        return(op + "0" * 11)
    else:
        #TODO make error
        return 0

def main():
    #todo
    
    allInsts = []
    
    while(True):
        st = input().strip()
        allInsts.append(st.split())
        if ( st == "hlt"):
            break
        elif(len(st) == 0):
            continue
        
    labels  = {}
   
    for i in range (len(allInsts)):
        if(allInsts[i][0]=="mov"):
            continue
        if ( allInsts[i][0] not in opcode):
            labels[allInsts[i][0]] = i
    
    for i in allInsts:
        print(assemblyCode(i,labels))
    
    
    
if __name__ == "__main__":
    main()
