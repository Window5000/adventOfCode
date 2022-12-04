
def main():
    f = open("input.txt")
    score = 0
    for x in f:
        enemy = x[0]
        player = x[1]

        curr = 0

        # rock (A)
        if player == 'X':
            if enemy == 'A':
                curr += 3
            if enemy == 'B':
                curr += 1
            if enemy == 'C':
                curr += 2

        # paper (B)
        if player == 'Y':
            curr += 3
            if enemy == 'A':
                curr += 1
            if enemy == 'B':
                curr += 2
            if enemy == 'C':
                curr += 3

        # scissors (C)
        if player == 'Z':
            curr += 6
            if enemy == 'A':
                curr += 2
            if enemy == 'B':
                curr += 3
            if enemy == 'C':
                curr += 1

        score += curr
        print(curr)

    print("Score: " + str(score))
