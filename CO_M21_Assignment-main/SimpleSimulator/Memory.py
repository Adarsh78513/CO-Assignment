instList = []

while True:
    temp = input()
    if len(temp) == 0:
        break
    instList.append(temp)


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
        return self.mem[int(index)]

    def dump(self):
        for k in self.mem:
            print(k)
