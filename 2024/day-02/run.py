import math

def run():
    levels = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            level = []
            numbers = line.split()
            for number in numbers:
                level.append(int(number))
            levels.append(level)

    num_safe = 0
    num_potentially_safe = 0
    for level in levels:
        deltas = []
        current = level[0]
        for next in level[1:]:
            deltas.append(next - current)
            current = next
        if all(-4 < x < 0 for x in deltas) or all(4 > x > 0 for x in deltas):
            num_safe += 1
            continue

        for i in range(len(level)):
            level2 = level.copy()
            level2.pop(i)

            deltas2 = []
            current = level2[0]
            for next in level2[1:]:
                deltas2.append(next - current)
                current = next
            if all(-4 < x < 0 for x in deltas2) or all(4 > x > 0 for x in deltas2):
                num_potentially_safe += 1
                break

    print(f"Num safe: {num_safe}")
    print(f"Num potentially safe: {num_potentially_safe}")
    print(f"Total: {num_safe + num_potentially_safe}")


if __name__ == "__main__":
    run()
