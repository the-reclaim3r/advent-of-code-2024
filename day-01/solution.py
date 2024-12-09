import heapq
from collections import defaultdict

# Runtime: O(nlogn)
# Spacetime: O(n)
def part1(lines):
    list1 = []
    list2 = []
    diff = 0
      
    for line in lines:
        curr = line.split()
        list1.append(int(curr[0]))
        list2.append(int(curr[1]))

    heapq.heapify(list1)
    heapq.heapify(list2)

    for i in range(len(list1)):
        diff += abs(heapq.heappop(list1) - heapq.heappop(list2))
      
    return diff

# Runtime: O(n)
# Spacetime: O(n)
def part2(lines):
    dict = defaultdict(int)
    list1 = []
    list2 = []
    similarity = 0

    for line in lines:
        curr = line.split()
        list1.append(int(curr[0]))
        list2.append(int(curr[1]))

    for num in list2:
        dict[num] += 1

    for num in list1:
        similarity += dict[num] * num
          
    return similarity

def main():
    sample_input = False
    main_input = True
    part_two = True

    if sample_input:
        with open('example-input.txt') as f:
            lines = f.read().splitlines()
            print("Part 1 Example Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Example Answer: {}".format(part2(lines)))

    if main_input:
        with open('input.txt') as f:
            lines = f.read().splitlines()
            print("Part 1 Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Answer: {}".format(part2(lines)))
        
if __name__ == "__main__":
    main()