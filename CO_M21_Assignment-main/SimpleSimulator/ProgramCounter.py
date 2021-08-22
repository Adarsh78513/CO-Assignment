

def binToDec(num):
    """[summary]

    Args:
        num ([string]): [binary number]

    Returns:
        [integer]: [description]
    """
    return int(num, 2)


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

    def update(self, mem_address):
        self.counter = mem_address

    def dump(self):
        print(self.counter + " ", end=" ")
