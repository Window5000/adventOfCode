def get_point(char) -> int:
    if char == char.lower():
        return ord(char) - 96
    else:
        return ord(char) - 38


def part1():
    f = open("input.txt")
    score = 0
    for x in f:
        comp1 = x[:int(len(x) / 2)]
        comp2 = x[int(len(x) / 2):]

        finished = False

        for y in comp1:
            for z in comp2:
                if y == z and not finished:
                    print(get_point(y))
                    score += get_point(y)
                    finished = True

    print("\nScore: " + str(score))


def part2():
    f = open("input.txt")
    print("")
    score = 0
    i = 0
    arr = []
    finished = False
    for x in f:
        i += 1
        arr.append(x.strip())
        answer = ""
        if i == 3:
            i = 0
            print(arr)
            strarr1 = set(arr[0])
            strarr2 = set(arr[1])
            strarr3 = set(arr[2])
            answer = list(strarr1.intersection(strarr2, strarr3))
            score += get_point(answer[0])
            print(answer[0] + ": " + str(get_point(answer[0])))
            arr = []
    print("\nScore: " + str(score))
