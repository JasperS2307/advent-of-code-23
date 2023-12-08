import sys
import os 

input_file = sys.argv[1] 

with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
    lines = file.readlines()

def part_one():
    time = 0
    time_list = lines[0].strip().split(":")[1].split(" ")
    distance_list = lines[1].strip().split(":")[1].split(" ")

    time_list = [t for t in time_list if t.isdigit()]
    distance_list = [t for t in distance_list if t.isdigit()]

    print(time_list)
    print(distance_list)

    print(f"The answer for part one is: {time}")

def part_two():
    score = 0

    print("-----------------")
    print(f"The answer for part two is: {score}")

if __name__ == '__main__':
    part_one()
    part_two()
