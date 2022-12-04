from importlib import import_module, reload
from os import chdir


def main(day, part):
    chdir(day.replace(".", "/"))
    if part == 1:
        import_module(day + ".run").part1()
    if part == 2:
        import_module(day + ".run").part2()
    else:
        print("dawd")
        import_module(day + ".run").main()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Enter year followed by dot and then day: ", end='')
    day = input()
    print("Enter which part to run (1 or 2): ", end='')
    part = input()
    main(day, part)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
