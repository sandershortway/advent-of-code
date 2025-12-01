def problem1():
    num_zeros = 0

    with open("day1/input.txt") as f:
        dial = 50
        for line in f:
            multiplier = -1 if line[0] == "L" else 1
            num_ticks = int(line[1:])
            dial = (dial + multiplier * num_ticks) % 100
            if dial == 0:
                num_zeros += 1
    return num_zeros


def problem2():
    num_zero_crosses = 0

    with open("day1/input.txt") as f:
        dial = 50
        for line in f:
            multiplier = -1 if line[0] == "L" else 1
            num_ticks = int(line[1:])
            new_dial = dial + multiplier * num_ticks
            dial = new_dial % 100
            num_zero_crosses += abs(new_dial // 100)
    return num_zero_crosses


if __name__ == "__main__":
    print(problem2())
