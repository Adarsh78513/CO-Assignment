counter = "00000000"

def binToDec(num):
    """[summary]

    Args:
        num ([string]): [binary number]

    Returns:
        [integer]: [description]
    """
    return int(num,2)

def decToBinary8(n):
    s = bin(n)
    s = s[2::]
    s = "0" * (8 - len(s)) + s
    return s

class ProgramCounter:
    
    def __init__(self, counter):
        self.counter = decToBinary8(counter)
    
    def getVal(self):
        return self.counter

    def next(self):
        a = int(self.counter)
        a = decToBinary8(a)
        a += 1
        self.counter = binToDec(a)
    
    def jump(self, mem_addr):
        self.counter = mem_addr