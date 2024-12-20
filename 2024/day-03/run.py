import re

def run():
    with open("input.txt", "r") as file:
        code = file.read()

    regex = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
    operations = re.findall(regex, code)

    sum = 0
    enabled = True
    for op in operations:
        match op[:3]:
            case "don":
                enabled = False
            case "do(":
                enabled = True
            case _:
                mul_regex = r"mul\((\d+),(\d+)\)"
                match = re.fullmatch(mul_regex, op)
                if enabled:
                     sum += int(match.group(1)) * int(match.group(2))

    print(sum)


if __name__ == "__main__":
    run()
