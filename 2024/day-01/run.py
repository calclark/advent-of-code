def run():
    left = []
    right = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            numbers = line.split()
            assert len(numbers) == 2
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))
    left = sorted(left)
    right = sorted(right)
    distance = sum((abs(l - r) for l, r in zip(left, right)))
    print(f"Distance is: {distance}")
    score = 0
    for curr_value in left:
        score += curr_value * right.count(curr_value)
    print(f"Score is: {score}")


if __name__ == "__main__":
    run()
