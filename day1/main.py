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


if __name__ == "__main__":
    print(problem1())
