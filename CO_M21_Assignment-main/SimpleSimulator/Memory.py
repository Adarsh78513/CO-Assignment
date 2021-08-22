mem = []
for i in 256:
    mem.append("0"*16)
    


class Memory:
    def __init__(self, mem, instList):
        self.mem = mem
        self.instList = instList
        for i in len(self.instList):
            mem[i] = self.instList[i]
    
    def get(self, line):
        return mem[int(line)]
    