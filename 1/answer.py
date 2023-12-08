import os
import re
import sys

input_file = sys.argv[1] 

def extract(line): 
    first_match = re.search(r'\d{1,}', line).group()[0]
    last_match = re.search(r'\d{1,}', line[::-1]).group()[0]

    return int(first_match + last_match)

def part_one():
    with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
        lines = file.readlines()

    total = 0
    for line in lines:
        total = total + extract(line)

    print(f"The answer for part one is: {total}")

def part_two():
    mapped_numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }

    with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
        lines = file.readlines()

    total = 0
    for line in lines:
        linelen = len(line)
        c = 0
        newline = ""
        while c < linelen:
            for k in mapped_numbers:
                if line[c].isdigit():
                    newline = newline + line[c]
                    break
                if line.startswith(k, c):
                    newline = newline + mapped_numbers[k]
                    break
            c += 1
        total = total + extract(newline)

    print("-----------------")
    print(f"The answer for part two is: {total}")

if __name__ == '__main__':
    part_one()
    part_two()
