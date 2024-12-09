import re

def part1(lines):
    matches = []
    sum = 0

    for line in lines:
        curr = re.findall("mul\(\d*,\d*\)", line)
        matches += curr

    for match in matches:
        formatted = match.split("(")[1].split(",")
        sum += int(formatted[0]) * int(formatted[1][:-1])
    
    return sum

def part2(lines):
    matches = []
    sum = 0

    for line in lines:
        curr = re.findall("mul\(\d*,\d*\)|do\(\)|don't\(\)", line)
        matches += curr

    do = True
    for match in matches:
        if match == "don't()":
            do = False
            continue
        
        if match == "do()":
            do = True
            continue

        if do:
            formatted = match.split("(")[1].split(",")
            sum += int(formatted[0]) * int(formatted[1][:-1])

    return sum

def main():
    sample_input = False
    part_two = True

    if sample_input:
        with open('example-input.txt') as f:
            lines = f.read().splitlines()
            print("Part 1 Example Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Example Answer: {}".format(part2(lines)))

    else:
        with open('input.txt') as f:
            lines = f.read().splitlines()
            print("Part 1 Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Answer: {}".format(part2(lines)))
        
if __name__ == "__main__":
    main()