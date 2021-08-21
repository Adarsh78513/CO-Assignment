from ExecutionEngine import ExecutionEngine
from Memory import Memory
from ProgramCounter import ProgramCounter
from RegisterFile import RegisterFile


def main():
    memory = Memory()
    pc = ProgramCounter()
    reg = RegisterFile()
    halted = False
    while not halted:
        inst = memory.get()
        
        
    #print memory 

if __name__ == "__main__":
    main()