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

    def __init__(self, memory, reg):
        self.memory = memory
        self.reg = reg

    def fun(self, inst):
        """for finding what command the binary line means
    
        Args:
            inst ([string]): [the instruction]

        Returns:
            name of function
        """
        return opcode[inst[0:5]][0]

    def type(self, inst):
        return opcode[inst[0:5][1]]

    def reg(self, n):
        """takes the address of register and returns the name of register

        Args:
            n ([string]): [address of register]

        Returns:
            [mane]
        """
        return register[n]

    def execute(self, inst, cycle):

        if type(inst) == "A":

            if self.fun(inst) == "add":
                n = binToDec(self.reg.get(self.reg(inst[10, 13]))) + binToDec(self.reg.get(self.reg(inst[13, 16])))
                if n > 65535:
                    n = 0
                    self.reg.setOverFlow()
                self.reg.set(self.reg(inst[7, 10]), decToBinary16(n))

            elif self.fun(inst) == "sub":
                n = binToDec(self.reg.get(self.reg(inst[10, 13]))) - binToDec(
                    self.reg.get(self.reg(inst[13, 16])))
                if n < 0:
                    n = 0
                    self.reg.setOverFlow()
                self.reg.set(self.reg(inst[7, 10]), decToBinary16(n))

            elif self.fun(inst) == "mul":
                n = binToDec(self.reg.get(self.reg(inst[10, 13]))) * binToDec(
                    self.reg.get(self.reg(inst[13, 16])))
                if n > 65535:
                    n = 0
                    self.reg.setOverFlow()
                self.reg.set(self.reg(inst[7, 10]), decToBinary16(n))

            elif self.fun(inst) == "xor":
                n = binToDec(self.reg.get(self.reg(inst[10, 13])) ^ binToDec(
                    self.reg.get(self.reg(inst[13, 16]))))
                self.reg.set(self.reg(inst[7, 10]), decToBinary16(n))

            elif self.fun(inst) == "or":
                n = binToDec(self.reg.get(self.reg(inst[10, 13])) | binToDec(
                    self.reg.get(self.reg(inst[13, 16]))))
                self.reg.set(self.reg(inst[7, 10]), decToBinary16(n))

            elif self.fun(inst) == "or":
                n = binToDec(self.reg.get(self.reg(inst[10, 13])) & binToDec(
                    self.reg.get(self.reg(inst[13, 16]))))
                self.reg.set(self.reg(inst[7, 10]), decToBinary16(n))

        elif type(inst) == "B":
            if self.fun(inst) == "mov":
                self.reg.set(self.reg(inst[5, 8]), inst[8, 16])

            elif self.fun(inst) == "rs":
                n = self.reg.get(self.reg(inst[5, 8])) >> decToBinary16(inst[8, 16])
                self.reg.set(self.reg(inst[5, 8]), decToBinary16(inst[8, 16]))

            elif self.fun(inst) == "ls":
                n = self.reg.get(self.reg(inst[5, 8])) << decToBinary16(inst[8, 16])
                self.reg.set(self.reg(inst[5, 8]), decToBinary16(inst[8, 16]))

        elif type(inst) == "C":
            if self.fun(inst) == "mov":
                self.reg.set(self.reg(inst[10, 13]), self.reg.get(self.reg(inst[13, 16])))

            elif self.fun(inst) == "not":
                n = ~ self.reg.get(self.reg(inst[13, 16]))
                self.reg.set(self.reg(inst[10, 13]), decToBinary16(n))

            elif self.fun(inst) == "cmp":
                n1 = self.reg.get(self.reg(inst[10, 13]))
                n2 = self.reg.get(self.reg(inst[13, 16]))
                self.reg.setFlag(n1, n2)

            elif self.fun(inst) == "div":
                quotient = self.reg.get(self.reg(inst[10, 13])) // self.reg.get(
                    self.reg(inst[13, 16]))
                remainder = self.reg.get(self.reg(inst[10, 13])) % self.reg.get(
                    self.reg(inst[13, 16]))
                self.reg.set("R0", decToBinary16(quotient))
                self.reg.set("R1", decToBinary16(remainder))

        elif type(inst) == "D":
            if self.fun(inst) == "ld":
                n = self.memory.get(inst[8, 16])
                self.reg.set(self.reg(inst[5, 8]), decToBinary16(n))

            elif self.fun(inst) == "st":
                n = self.reg.get(self.reg[inst[5, 8]])
                self.memory.set(inst[8, 16], decToBinary16(n))

        elif type(inst) == "E":
            if self.fun(inst) == "jmp":
                ProgramCounter.update(inst[8, 16])

            elif self.fun(inst) == "jlt":
                if self.reg.get("FLAGS")[-3] == "1":
                    ProgramCounter.update(inst[8, 16])

            elif self.fun(inst) == "jgt":
                if self.reg.get("FLAGS")[-2] == "1":
                    ProgramCounter.update(inst[8, 16])

            elif self.fun(inst) == "je":
                if self.reg.get("FLAGS")[-1] == "1":
                    ProgramCounter.update(inst[8, 16])

        elif type(inst) == "F":
            halted = True

        if self.fun(inst) == "hlt":
            return True  # TODO return updated register
        else:
            return False  # TODO return updated register


def main():
    # change
    address = input()

    inst = memory.get(address)

    halted = False


if __name__ == "__main__":
    main()
