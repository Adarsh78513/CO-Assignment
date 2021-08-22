instList = []

while True:
    try:
        temp = input()
        if len(temp) == 0:
            break
        instList.append(temp)
    except EOFError:
        break
    
def binToDec(num):
    """[summary]

    Args:
        num ([string]): [binary number]

    Returns:
        [integer]: [description]
    """
    return int(num, 2)

class Memory:
    def __init__(self):
        mem = []

        # empty memory
        for j in range(256):
            mem.append("0" * 16)

        self.mem = mem
        self.instList = instList
        for index in range(len(self.instList)):
            mem[index] = self.instList[index]

    def get(self, index, cycle):
        return self.mem[binToDec(str(index))]

    def dump(self):
        for k in self.mem:
            print(k)
