from importlib import import_module
from os import chdir

if __name__ == '__main__':
    chdir("2022/3")
    import_module("2022.3.run").part2()