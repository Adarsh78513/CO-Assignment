from ExecutionEngine import ExecutionEngine
from Memory import Memory 
from Memory import binToDec
from ProgramCounter import ProgramCounter
from RegisterFile import RegisterFile
import matplotlib.pyplot as plt
import plotlist


def main():
    memory = Memory()
    pc = ProgramCounter(0)
    halted = False
    reg = RegisterFile()
    executionEngine = ExecutionEngine(memory, reg, pc)
    cycle = 0

    while not halted:
        inst = memory.get(pc.getVal(), cycle)
        plotlist.plot_list.append([cycle,binToDec(pc.getVal())])
        halted, newPc = executionEngine.execute(inst, cycle)

        pc.dump()
        reg.dump()
        pc.update(newPc)

        cycle += 1

    memory.dump()
    x,y=zip(*plotlist.plot_list)
    plt.plot(x,y)
    plt.savefig("ploted_graph.png")


if __name__ == "__main__":
    main()
