import sys
import os 

input_file = sys.argv[1] 

with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
    lines = file.readlines()

INSTRUCTIONS = lines[0].strip()
STEPS_MAP = {}
for line in lines[2:]:
    line = line.strip()
    step_key, step_insructions = line.split("=")
    step_insructions = step_insructions.replace("(", "").replace(")", "").replace(" ", "")
    left_instruction, right_instruction = step_insructions.split(",")
    STEPS_MAP[step_key.strip()] = {"L": left_instruction.strip(), "R": right_instruction.strip()}


def part_one():
    step_count = 0
    current_step = "AAA"
    while current_step != "ZZZ":
        i = 0
        while i < len(INSTRUCTIONS) and current_step != "ZZZ":
            step_count += 1
            current_step = STEPS_MAP[current_step][INSTRUCTIONS[i]]
            i += 1
        
    print(f"The answer for part one is: {step_count}")

def part_two():
    score = 1
    ends_with_a_paths = {}
    for step_key in STEPS_MAP:
        if step_key[2] == "A":
            ends_with_a_paths[step_key] = []

    instruction_index = 0
    for step in ends_with_a_paths:
        while instruction_index >= len(INSTRUCTIONS):
            instruction_index -= len(INSTRUCTIONS)
        
        while STEPS_MAP[step][INSTRUCTIONS[instruction_index]][2] != "Z":
            ends_with_a_paths[step].append()

        print(ends_with_a_paths[step][-1])
        # while 
        ends_with_a_paths[step]

    # all_end_with_z = True
    # checked_all = False
    # while all_end_with_z:
    #     for step in ends_with_a_paths:
    #         step_index = len(ends_with_a_paths[step])
    #         while step_index >= len(INSTRUCTIONS):
    #             step_index -= len(INSTRUCTIONS)

    #         # print(step_index)
    #         ends_with_a_paths[step].append(STEPS_MAP[ends_with_a_paths[step][-1]][INSTRUCTIONS[step_index]])
    #         # print(STEPS_MAP[])
    #         # print(ends_with_a_paths[step])
    #         print(ends_with_a_paths[step][-1][2])
    #         print(step)
    #         # if ends_with_a_paths[step][-1][2] != "Z":
    #         #     print("Continue")
    #         #     continue
    #         # else:
    #         #     print("Break")
    #     for step in ends_with_a_paths:
    #         if ends_with_a_paths[step][-1][2] != "Z":
    #             continue
            
    #     break
            # STEPS_MAP[current_step][INSTRUCTIONS[i]]
            # ends_with_a_paths[step].append()
    # for path in ends_with_a_paths:
    #     current_step = path
    #     while current_step[2] != "Z":
    #         i = 0
    #         while i < len(INSTRUCTIONS) and current_step[2] != "Z":
    #             current_step = STEPS_MAP[current_step][INSTRUCTIONS[i]]
    #             ends_with_a_paths[path].append(current_step)
    #             i += 1
                
    #     print(f"Stopped at {len(ends_with_a_paths[path])} for {path}")

        # ends_with_a_paths[path] = counter

    # print(ends_with_a_paths)
    # for path in ends_with_a_paths:
    #     score = (score * ends_with_a_paths[path])

    # print(f"{len(ends_with_a_paths)} paths ends with an A")
    print("-----------------")
    print(f"The answer for part two is: {score}")

if __name__ == '__main__':
    # part_one()
    part_two()
