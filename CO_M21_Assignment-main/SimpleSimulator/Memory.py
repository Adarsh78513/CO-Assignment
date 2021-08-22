instList = []
i = input()
while len(i) != 0:
    instList.append(i)


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

    def get(self, line):
        return self.mem[int(line)]

    def dump(self):
        for k in self.mem:
            print(k)
