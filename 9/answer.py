import sys
import os

input_file =  sys.argv[1] if len(sys.argv) > 1 else "test.txt"

with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
    lines = file.readlines()

def part_one():
    total = 0
    for line in lines:
        line = line.strip()
        breakdown = []
        breakdown_index = 0
        i = 1
        first_line = [int(i) for i in line.split(" ")]
        breakdown.append(first_line)
        while sum(breakdown[breakdown_index]) > 0:
            breakdown.append([])
            row = breakdown[breakdown_index]
            while len(row) > i:
                l, r = int(row[i]), int(row[i - 1])
                breakdown[breakdown_index + 1].append(l - r)
                i += 1

            i = 1
            breakdown_index += 1

        print("-------------")
        breakdown_index -= 1
        base = breakdown[breakdown_index][-1]
        breakdown_index -= 1
        while breakdown_index >= 0:
            bdi = breakdown[breakdown_index]
            base += bdi[len(bdi) - 1]
            breakdown_index -= 1

        print(base)
        total += base

    print(f"The answer for part one is: {total}")

def part_two():
    score = 0

    print("-----------------")
    print(f"The answer for part two is: {score}")

if __name__ == '__main__':
    part_one()
    # part_two()
