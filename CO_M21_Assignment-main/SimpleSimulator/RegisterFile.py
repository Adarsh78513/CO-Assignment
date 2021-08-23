# registerValues = {
#     "R0": "0000000000000000",
#     "R1": "0000000000000000",
#     "R2": "0000000000000000",
#     "R3": "0000000000000000",
#     "R4": "0000000000000000",
#     "R5": "0000000000000000",
#     "R6": "0000000000000000",
#     "FLAGS": "0000000000000000",
# }


class RegisterFile:

    def __init__(self):
        self.registerValues = {
            "R0": "0000000000000000",
            "R1": "0000000000000000",
            "R2": "0000000000000000",
            "R3": "0000000000000000",
            "R4": "0000000000000000",
            "R5": "0000000000000000",
            "R6": "0000000000000000",
            "FLAGS": "0000000000000000",
        }

    def get(self, registerName):
        return self.registerValues[registerName]

    def set(self, registerName, setValue):
        self.registerValues[registerName] = setValue

    def setFLAG(self, n1, n2):
        a = self.registerValues["FLAGS"]
        if n1 == n2:
            a = a[0:-1] + "1"
            self.registerValues["FLAGS"] = a

        elif n1 > n2:
            a = a[0:-2] + "1" + a[-1]
            self.registerValues["FLAGS"] = a

        elif n1 < n2:
            a = a[0:-3] + "1" + a[-2:]
            self.registerValues["FLAGS"] = a

    def setOverFlow(self):
        a = self.registerValues["FLAGS"]
        a = a[0:-3] + "1" + a[-2]
        self.registerValues["FLAGS"] = a

    def dump(self):
        print(self.registerValues["R0"] + " " +
              self.registerValues["R1"] + " " +
              self.registerValues["R2"] + " " +
              self.registerValues["R3"] + " " +
              self.registerValues["R4"] + " " +
              self.registerValues["R5"] + " " +
              self.registerValues["R6"] + " " +
              self.registerValues["FLAGS"] + " ")
