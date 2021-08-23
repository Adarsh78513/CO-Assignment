from ExecutionEngine import ExecutionEngine
from Memory import Memory
from ProgramCounter import ProgramCounter
from RegisterFile import RegisterFile
import matplotlib.pyplot as plt
from plotlist import plot_list

def main():
    memory = Memory()
    pc = ProgramCounter(0)
    halted = False
    reg = RegisterFile()
    executionEngine = ExecutionEngine(memory, reg, pc)
    cycle = 0

    while not halted:
        inst = memory.get(pc.getVal(), cycle)
        plot_list.add([cycle,pc.getVal])
        halted, newPc = executionEngine.execute(inst, cycle)

        pc.dump()
        reg.dump()
        pc.update(newPc)

        cycle += 1

    memory.dump()
    x,y=zip(*plot_list)
    plt.plot(x,y)
    plt.savefig("ploted_graph.png")


if __name__ == "__main__":
    main()
