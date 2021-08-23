from ExecutionEngine import ExecutionEngine
from Memory import Memory
from ProgramCounter import ProgramCounter
from RegisterFile import RegisterFile


def main():
    memory = Memory()
    pc = ProgramCounter(0)
    halted = False
    reg = RegisterFile()
    executionEngine = ExecutionEngine(memory, reg, pc)
    cycle = 0

    while not halted:
        inst = memory.get(pc.getVal(), cycle)
        halted, newPc = executionEngine.execute(inst, cycle)

        pc.dump()
        reg.dump()
        pc.update(newPc)

        cycle += 1

    memory.dump()


if __name__ == "__main__":
    main()
