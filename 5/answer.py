import sys
import os 

input_file = sys.argv[1] 

with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
    lines = file.readlines()

def part_one():
    score = 0
    print(f"The answer for part one is: {score}")

def part_two():
    score = 0

    print("-----------------")
    print(f"The answer for part two is: {score}")

if __name__ == '__main__':
    part_one()
    part_two()
