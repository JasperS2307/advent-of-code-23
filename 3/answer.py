import sys
import os
import re 
from pprint import pprint

input_file = sys.argv[1] 

with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
    lines = file.readlines()

def part_one():
    previous_line_count, current_line_count, next_line_count = [-1, 0, 1]
    previous_line = next_line = ""
    total = 0
    while current_line_count < len(lines):
        first_digit_pos = last_digit_pos = 0
        is_at_digit = False
        
        previous_line = lines[previous_line_count].strip() if current_line_count > 0 else ""
        next_line = lines[next_line_count].strip() if current_line_count < 139 else ""

        current_line = lines[current_line_count].strip()
        for i, c in enumerate(current_line):
            if c.isdigit() and is_at_digit is False:
                first_digit_pos = i
                is_at_digit = True 

            if (c.isdigit() is False or i + 1 == len(current_line)) and is_at_digit:
                last_digit_pos = i
                is_at_digit = False

                first_search_pos = max((first_digit_pos - 1), 0)
                last_search_pos = min((last_digit_pos + 1), len(current_line))
                nmbr = int(re.search(r'\d+', current_line[first_search_pos:last_search_pos]).group())
                print(f"Digit in line {current_line_count} started at {first_digit_pos} and ended at {last_digit_pos} and was {nmbr} ")
                
                def part_has_sym(l):
                    return re.search(r'[^\d\.]', l[first_search_pos:last_search_pos]) is not None

                if (previous_line != "" and part_has_sym(previous_line)) or (next_line != "" and part_has_sym(next_line)) or part_has_sym(current_line):
                    total += nmbr
                    continue

                print("Skipping...")

        previous_line_count += 1
        current_line_count += 1
        next_line_count += 1

    print("-----------------------")
    print(f"The answer for part one is: {total}")

def part_two():
    previous_line_count, current_line_count, next_line_count = [-1, 0, 1]
    previous_line = next_line = ""
    total = 0

    gear_map = {}

    for line_index, line in enumerate(lines):
        line = line.strip()
        for char_index, c in enumerate(line):
            if c == "*":
                gear_map.append({line_index: {}})
                # gear_map[line_index]. = {char_index}

        # numbers_in_line = re.findall(r'\d+', line)
        # print(numbers_in_line)
        # gears = re.match
    pprint(gear_map)
    # while current_line_count < len(lines):
    #     first_digit_pos = last_digit_pos = 0
    #     is_at_digit = False
        
    #     previous_line = lines[previous_line_count].strip() if current_line_count > 0 else ""
    #     next_line = lines[next_line_count].strip() if current_line_count < 139 else ""

    #     current_line = lines[current_line_count].strip()
    #     for i, c in enumerate(current_line):
    #         if c.isdigit() and is_at_digit is False:
    #             first_digit_pos = i
    #             is_at_digit = True 

    #         if (c.isdigit() is False or i + 1 == len(current_line)) and is_at_digit:
    #             last_digit_pos = i
    #             is_at_digit = False

    #             first_search_pos = max((first_digit_pos - 1), 0)
    #             last_search_pos = min((last_digit_pos + 1), len(current_line))
    #             nmbr = int(re.search(r'\d+', current_line[first_search_pos:last_search_pos]).group())
    #             print(f"Digit in line {current_line_count} started at {first_digit_pos} and ended at {last_digit_pos} and was {nmbr} ")
                
    #             def part_has_sym(l):
    #                 return re.search(r'[^\d\.]', l[first_search_pos:last_search_pos]) is not None

    #             if (previous_line != "" and part_has_sym(previous_line)) or (next_line != "" and part_has_sym(next_line)) or part_has_sym(current_line):
    #                 total += nmbr
    #                 continue

    #             print("Skipping...")

    #     previous_line_count += 1
    #     current_line_count += 1
    #     next_line_count += 1

    print("-----------------")
    print("The answer for part two is:")
    print("")

if __name__ == '__main__':
    # part_one()
    part_two()
