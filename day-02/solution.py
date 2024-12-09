import copy

def safe(report):
    increasing = True if report[1] - report[0] > 0 else False
    safe = True
    prev = report[1]

    if not 0 < abs(report[1] - report[0]) < 4:
        return False

    for i in range(2, len(report)):
        # if it isn't increasing/decreasing
        if (increasing and report[i] - prev < 0) or (not increasing and report[i] - prev > 0):
            safe = False
            break
        # is it safe
        if abs(report[i] - prev) < 1 or abs(report[i] - prev) > 3:
            safe = False
            break
    
        prev = report[i]
    
    return safe

def part1(lines):
    numSafe = 0
    reports = []

    for line in lines:
        curr = line.split()
        reports.append([int(str) for str in curr])
    
    for report in reports:
        if (safe(report)):
            numSafe += 1
        
    return numSafe

def part2(lines):
    numSafe = 0
    reports = []

    for line in lines:
        curr = line.split()
        reports.append([int(str) for str in curr])

    for report in reports:
        # do i need to figure out which to exclude
        if (safe(report)):
            numSafe += 1
            continue

        # report is not safe without excluding
        for excluded_index in range(len(report)):
            fil_rep = copy.deepcopy(report)
            fil_rep.pop(excluded_index)
            
            if safe(fil_rep):
                numSafe += 1
                break

    return numSafe

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