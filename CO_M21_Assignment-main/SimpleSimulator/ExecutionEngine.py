import plotlist
from Memory import binToDec
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
    s = bin(int(n))
    s = s[2::]
    if len(s) > 16:
        s = s[-16:]
    else:
        s = "0" * (16 - len(s)) + s
    return s

def decToBinary8(n):
    s = bin(n)
    s = s[2::]
    s = "0" * (8 - len(s)) + s
    return s

class ExecutionEngine:

    def __init__(self, memory, reg, pc):
        self.memory = memory
        self.reg = reg
        self.pc = pc

    def fun(self, inst):
        """for finding what command the binary line means
    
        Args:
            inst ([string]): [the instruction]

        Returns:
            name of function
        """
        return opcode[inst[0:5]][0]

    def type(self, inst):
        return opcode[inst[0:5]][1]

    def regist(self, n):
        """takes the address of register and returns the name of register

        Args:
            n ([string]): [address of register]

        Returns:
            [mane]
        """
        return register[n]

    def execute(self, inst, cycle):

        newPc = decToBinary8(binToDec(self.pc.getVal()) + 1)

        if self.type(inst) == "A":

            if self.fun(inst) == "add":
                n = binToDec(self.reg.get(self.regist(inst[10: 13]))) + binToDec(self.reg.get(self.regist(inst[13: 16])))
                if n > 65535:
                    self.reg.setOverFlow()
                else:
                    self.reg.set("FLAGS", "0"*16)
                self.reg.set(self.regist(inst[7: 10]), decToBinary16(n))

            elif self.fun(inst) == "sub":
                n = binToDec(self.reg.get(self.regist(inst[10: 13]))) - binToDec(self.reg.get(self.regist(inst[13: 16])))
                if n < 0:
                    n = 0
                    self.reg.setOverFlow()
                else:
                    self.reg.set("FLAGS", "0" * 16)
                self.reg.set(self.regist(inst[7: 10]), decToBinary16(n))

            elif self.fun(inst) == "mul":
                n = binToDec(self.reg.get(self.regist(inst[10: 13]))) * binToDec(self.reg.get(self.regist(inst[13: 16])))
                if n > 65535:
                    self.reg.setOverFlow()
                else:
                    self.reg.set("FLAGS", "0" * 16)
                self.reg.set(self.regist(inst[7: 10]), decToBinary16(n))

            elif self.fun(inst) == "xor":
                n = binToDec(self.reg.get(self.regist(inst[10: 13]))) ^ binToDec(self.reg.get(self.regist(inst[13: 16])))
                self.reg.set(self.regist(inst[7: 10]), decToBinary16(n))
                self.reg.set("FLAGS", "0" * 16)

            elif self.fun(inst) == "or":
                n = binToDec(self.reg.get(self.regist(inst[10: 13]))) | binToDec(self.reg.get(self.regist(inst[13: 16])))
                self.reg.set(self.regist(inst[7: 10]), decToBinary16(n))
                self.reg.set("FLAGS", "0" * 16)

            elif self.fun(inst) == "and":
                self.reg.set("FLAGS", "0" * 16)
                n = binToDec(self.reg.get(self.regist(inst[10: 13]))) & binToDec(self.reg.get(self.regist(inst[13: 16])))
                self.reg.set(self.regist(inst[7: 10]), decToBinary16(n))

        elif self.type(inst) == "B":
            if self.fun(inst) == "movi":
                self.reg.set("FLAGS", "0" * 16)
                self.reg.set(self.regist(inst[5: 8]), "0"*8 + inst[8: 16])

            elif self.fun(inst) == "rs":
                self.reg.set("FLAGS", "0" * 16)
                n = self.reg.get(self.regist(inst[5: 8]))
                shifter = binToDec(inst[8: 16])
                a = n[0:-1*(shifter)]
                n = "0"*shifter + a
                self.reg.set(self.regist(inst[5: 8]),  n)

            elif self.fun(inst) == "ls":
                self.reg.set("FLAGS", "0" * 16)
                n = self.reg.get(self.regist(inst[5: 8]))
                shifter = binToDec(inst[8: 16])
                n = n[shifter::]+"0"*shifter
                self.reg.set(self.regist(inst[5: 8]), n)

        elif self.type(inst) == "C":
            if self.fun(inst) == "movr":
                self.reg.set(self.regist(inst[10: 13]), self.reg.get(self.regist(inst[13: 16])))
                self.reg.set("FLAGS", "0" * 16)

            elif self.fun(inst) == "not":
                self.reg.set("FLAGS", "0" * 16)
                n = self.reg.get(self.regist(inst[13: 16]))
                n = n.replace("0", ".")
                n = n.replace("1", "0")
                n = n.replace(".", "1")
                self.reg.set(self.regist(inst[10: 13]), n)

            elif self.fun(inst) == "cmp":
                self.reg.set("FLAGS", "0" * 16)
                n1 = self.reg.get(self.regist(inst[10: 13]))
                n2 = self.reg.get(self.regist(inst[13: 16]))
                self.reg.setFLAG(n1, n2)

            elif self.fun(inst) == "div":
                self.reg.set("FLAGS", "0" * 16)
                quotient = binToDec(self.reg.get(self.regist(inst[10: 13]))) // binToDec(self.reg.get(self.regist(inst[13: 16])))
                remainder = binToDec(self.reg.get(self.regist(inst[10: 13]))) % binToDec(self.reg.get(self.regist(inst[13: 16])))

                self.reg.set("R0", decToBinary16(quotient))
                self.reg.set("R1", decToBinary16(remainder))

        elif self.type(inst) == "D":
            if self.fun(inst) == "ld":
                self.reg.set("FLAGS", "0" * 16)
                n = self.memory.get(inst[8: 16], cycle)
                plotlist.plot_list.append([cycle,int(binToDec(inst[8: 16]))])
                self.reg.set(self.regist(inst[5: 8]), n)

            elif self.fun(inst) == "st":
                self.reg.set("FLAGS", "0" * 16)
                n = self.reg.get(self.regist(inst[5: 8]))
                i = binToDec(inst[8: 16])
                plotlist.plot_list.append([cycle,int(binToDec(inst[8: 16]))])
                self.memory.setI(n, i)

        elif self.type(inst) == "E":
            if self.fun(inst) == "jmp":
                newPc = inst[8: 16]
                self.reg.set("FLAGS", "0" * 16)

            elif self.fun(inst) == "jlt":
                if self.reg.get("FLAGS")[-3] == "1":
                    newPc = inst[8: 16]
                self.reg.set("FLAGS", "0" * 16)

            elif self.fun(inst) == "jgt":
                if self.reg.get("FLAGS")[-2] == "1":
                    newPc = inst[8: 16]
                self.reg.set("FLAGS", "0" * 16)

            elif self.fun(inst) == "je":
                if self.reg.get("FLAGS")[-1] == "1":
                    newPc = inst[8: 16]
                self.reg.set("FLAGS", "0" * 16)

        elif self.type(inst) == "F":
            self.reg.set("FLAGS", "0" * 16)
            halted = True

        if self.fun(inst) == "hlt":
            return True, newPc
        else:
            return False,  newPc