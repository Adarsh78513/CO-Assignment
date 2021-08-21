from Memory import Memory
from ProgramCounter import ProgramCounter
from RegisterFile import RegisterFile

opcode = {
    "00000": ("add", "A"),
    "00001": ("sub", "A"),
    "00010": ("movi", "B"),
    "00011": ("movr", "C"),
    "00100": ("ld", "D"),
    "00101": ("st", "D"),
    "00110": ("mul", "A"),
    "00111": ("div", "C"),
    "01000": ("rs", "B"),
    "01001": ("ls", "B"),
    "01010": ("xor", "A"),
    "01011": ("or", "A"),
    "01100": ("and", "A"),
    "01101": ("not", "C"),
    "01110": ("cmp", "C"),
    "01111": ("jmp", "E"),
    "10000": ("jlt", "E"),
    "10001": ("jgt", "E"),
    "10010": ("je", "E"),
    "10011": ("hlt", "F")
}

register = {
    "000": "R0",
    "001": "R1",
    "010": "R2",
    "011": "R3",
    "100": "R4",
    "101": "R5",
    "110": " R6",
    "111": "FLAGS"
}

class ExecutionEngine:
    
    def __init__(self, address):
        self.address = address
    
    def fun(inst):
        """for finding what command the binary line means
    
        Args:
            n ([string]): [the instruction]

        Returns:
            name of function
        """
        return opcode[inst[0:5]][0]
    
    def type(inst):
        return opcode[inst[0:5][1]]
        
    def reg(n):
        """takes the adress of register and returns the name of register

        Args:
            n ([string]): [address of register]

        Returns:
            [mane]
        """
        return register[n]
    def binToDec(num):
        """[summary]

        Args:
            num ([string]): [binary number]

        Returns:
            [integer]: [description]
        """
        return int(num,2)
    
    inst = Memory.getInst(address)
    
    if ( type(inst) == "A"):
        if ( fun(inst) == "add"):
            
            RegisterFile.set(reg(inst[7,10]), reg(inst[10, 13]), reg(inst[13, 16]))
    elif (type(inst) == "B"):
        RegisterFile.set(reg(inst[5, 8]), inst[8, 16])
    elif (type(inst) == "C"):
        RegisterFile.set(reg(inst[10, 13]), reg(inst[13, 16]))
    elif (type(inst) == "D"):
        RegisterFile.set( reg(inst[5,8]) , inst[8, 16])
    
    print(ProgramCounter.pc + " " + RegisterFile.R0 +  " " + RegisterFile.R1 + " " + RegisterFile.R2 + " " + 
          RegisterFile.R3 + RegisterFile.R4 + " " + RegisterFile.R5 + RegisterFile.R6 + " " + 
          RegisterFile.Flag)