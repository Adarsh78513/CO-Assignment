registerValues = {
    "R0": "0000000000000000",
    "R1": "0000000000000000",
    "R2": "0000000000000000",
    "R3": "0000000000000000",
    "R4": "0000000000000000",
    "R5": "0000000000000000",
    "R6": "0000000000000000",
    "FLAGS": "0000000000000000",
}

class RegisterFile:

    def get(self, registerName):
        return registerValues[registerName]

    def set(self, registerName, setValue):
        registerValues[registerName] = setValue

    def setFLAG(self, n1, n2):
        if n1 == n2:
            a = registerValues["FLAGS"]
            a = a[0:-1] + "1"
            registerValues["FLAGS"] = a

        elif n1 > n2:
            a = registerValues["FLAGS"]
            a = a[0:-2] + "1" + a[-1]
            registerValues["FLAGS"] = a

        elif n1 < n2:
            a = registerValues["FLAGS"]
            a = a[0:-3] + "1" + a[-2:]
            registerValues["FLAGS"] = a                   

    def setOverFlow(self):
        a = a = registerValues["FLAGS"]
        a = a[0:-3] + "1" + a[-2]
        registerValues["FLAGS"] = a