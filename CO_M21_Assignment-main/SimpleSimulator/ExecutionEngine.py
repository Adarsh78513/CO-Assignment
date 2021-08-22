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
    "110": "R6",
    "111": "FLAGS"
}


def binToDec(num):
    """[summary]

    Args:
        num ([string]): [binary number]

    Returns:
        [integer]: [description]
    """
    return int(num, 2)

def decToBinary16(n):
    s = bin(n)
    s = s[2::]
    s = "0" * (16 - len(s)) + s
    return s

class ExecutionEngine:

    def __init__(self, address):
        self.address = address

    def fun(self, inst):
        """for finding what command the binary line means
    
        Args:
            n ([string]): [the instruction]

        Returns:
            name of function
        """
        return opcode[self.inst[0:5]][0]

    def type(self, inst):
        return opcode[self.inst[0:5][1]]

    def reg(self, n):
        """takes the adress of register and returns the name of register

        Args:
            n ([string]): [address of register]

        Returns:
            [mane]
        """
        return register[self.n]

def main():
    # change
    address = input()

    inst = memory.get(address)

    halted = False

    if type(inst) == "A":
        if ExecutionEngine.fun(inst) == "add":
            n = binToDec(RegisterFile.get(ExecutionEngine.reg(inst[10, 13]))) + binToDec(RegisterFile.get(ExecutionEngine.reg(inst[13, 16])))
            if n > 65535:
                n = 0
                RegisterFile.setOverFlow()
            RegisterFile.set(ExecutionEngine.reg(inst[7, 10]), decToBinary16(n))

        elif ExecutionEngine.fun(inst) == "sub":
            n = binToDec(RegisterFile.get(ExecutionEngine.reg(inst[10, 13]))) - binToDec(RegisterFile.get(ExecutionEngine.reg(inst[13, 16])))
            if n < 0:
                n = 0
                RegisterFile.setOverFlow()
            RegisterFile.set(ExecutionEngine.reg(inst[7, 10]), decToBinary16(n))

        elif ExecutionEngine.fun(inst) == "mul":
            n = binToDec(RegisterFile.get(ExecutionEngine.reg(inst[10, 13]))) * binToDec(RegisterFile.get(ExecutionEngine.reg(inst[13, 16])))
            if n > 65535:
                n = 0
                RegisterFile.setOverFlow()
            RegisterFile.set(ExecutionEngine.reg(inst[7, 10]), decToBinary16(n))

        elif ExecutionEngine.fun(inst) == "xor":
            n = binToDec(RegisterFile.get(ExecutionEngine.reg(inst[10, 13])) ^ binToDec(RegisterFile.get(ExecutionEngine.reg(inst[13, 16]))))
            RegisterFile.set(ExecutionEngine.reg(inst[7, 10]), decToBinary16(n))

        elif ExecutionEngine.fun(inst) == "or":
            n = binToDec(RegisterFile.get(ExecutionEngine.reg(inst[10, 13])) | binToDec(RegisterFile.get(ExecutionEngine.reg(inst[13, 16]))))
            RegisterFile.set(ExecutionEngine.reg(inst[7, 10]), decToBinary16(n))

        elif ExecutionEngine.fun(inst) == "or":
            n = binToDec(RegisterFile.get(ExecutionEngine.reg(inst[10, 13])) & binToDec(RegisterFile.get(ExecutionEngine.reg(inst[13, 16]))))
            RegisterFile.set(ExecutionEngine.reg(inst[7, 10]), decToBinary16(n))

    elif type(inst) == "B":
        if ExecutionEngine.fun(inst) == "mov":
            RegisterFile.set(ExecutionEngine.reg(inst[5, 8]), inst[8, 16])

        elif ExecutionEngine.fun(inst) == "rs":
            n = RegisterFile.get(ExecutionEngine.reg(inst[5, 8])) >> decToBinary16(inst[8, 16])
            RegisterFile.set(ExecutionEngine.reg(inst[5, 8]), decToBinary16(inst[8, 16]))

        elif ExecutionEngine.fun(inst) == "ls":
            n = RegisterFile.get(ExecutionEngine.reg(inst[5, 8])) << decToBinary16(inst[8, 16])
            RegisterFile.set(ExecutionEngine.reg(inst[5, 8]), decToBinary16(inst[8, 16]))

    elif type(inst) == "C":
        if ExecutionEngine.fun(inst) == "mov":
            RegisterFile.set(ExecutionEngine.reg(inst[10, 13]), RegisterFile.get(ExecutionEngine.reg(inst[13, 16])))

        elif ExecutionEngine.fun(inst) == "not":
            n = ~ RegisterFile.get(ExecutionEngine.reg(inst[13, 16]))
            RegisterFile.set(ExecutionEngine.reg(inst[10, 13]), decToBinary16(n))

        elif ExecutionEngine.fun(inst) == "cmp":
            n1 = RegisterFile.get(ExecutionEngine.reg(inst[10, 13]))
            n2 = RegisterFile.get(ExecutionEngine.reg(inst[13, 16]))
            RegisterFile.setFlag(n1, n2)

        elif ExecutionEngine.fun(inst) == "div":
            quotient = RegisterFile.get(ExecutionEngine.reg(inst[10, 13])) // RegisterFile.get(ExecutionEngine.reg(inst[13, 16]))
            remainder = RegisterFile.get(ExecutionEngine.reg(inst[10, 13])) % RegisterFile.get(ExecutionEngine.reg(inst[13, 16]))
            RegisterFile.set("R0", decToBinary16(quotient))
            RegisterFile.set("R1", decToBinary16(remainder))

    elif type(inst) == "D":
        if ExecutionEngine.fun(inst) == "ld":
            n = Memory.get(inst[8, 16])
            RegisterFile.set(ExecutionEngine.reg(inst[5, 8]), decToBinary16(n))

        elif ExecutionEngine.fun(inst) == "st":
            n = RegisterFile.get(ExecutionEngine.reg[inst[5, 8]])
            Memory.set(inst[8, 16], decToBinary16(n))

    elif type(inst) == "E":
        if ExecutionEngine.fun(inst) == "jmp":
            ProgramCounter.jump(inst[8, 16])

        elif ExecutionEngine.fun(inst) == "jlt":
            if RegisterFile.get("FLAGS")[-3] == "1":
                ProgramCounter.jump(inst[8, 16])

        elif ExecutionEngine.fun(inst) == "jgt":
            if RegisterFile.get("FLAGS")[-2] == "1":
                ProgramCounter.jump(inst[8, 16])

        elif ExecutionEngine.fun(inst) == "je":
            if RegisterFile.get("FLAGS")[-1] == "1":
                ProgramCounter.jump(inst[8, 16])

    elif type(inst) == "F":
        halted = True

    print(ProgramCounter.getVal() + " " +
          RegisterFile.get("R0") + " " +
          RegisterFile.get("R1") + " " +
          RegisterFile.get("R2") + " " +
          RegisterFile.get("R3") + " " +
          RegisterFile.get("R4") + " " +
          RegisterFile.get("R5") + " " +
          RegisterFile.get("R6") + " " +
          RegisterFile.get("FLAGS"))


if __name__ == "__main__":
    main()
