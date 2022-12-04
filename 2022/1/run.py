
def main():
    f = open("input.txt")
    arr = []
    current = 0
    second = 0
    third = 0
    for x in f:
        empty = x.strip() == ""
        if not empty:
            if not x == "end":
                current += int(x)
            else:
                arr.append(current)
                current = 0
        else:
            arr.append(current)
            current = 0
    for x in arr:
        print(x)
        if x > current:
            current = x
    for x in arr:
        if x > second and not x == current:
            second = x
    for x in arr:
        if x > third and not x == current and not x == second:
            third = x

    print("\nFirst: " + str(current))
    print("Second: " + str(second))
    print("Third: " + str(third))

    print("\nTotal: " + str(current + second + third))
