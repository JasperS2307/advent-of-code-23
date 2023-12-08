import sys
import os

input_file = sys.argv[1] 

RED = 12
GREEN = 13
BLUE = 14

def parse_line(game_line: str): 
    game_id, game_set = game_line.split(': ', 1)
    game_id = int(game_id.split(' ')[1])

    for set in game_set.split("; "):
        for count_color in set.split(", "):
            count, color = count_color.split(" ")
            if color == "red" and int(count) > RED:
                return 0
            elif color == "green" and int(count) > GREEN:
                return 0
            elif color == "blue" and int(count) > BLUE:
                return 0
    
    return game_id

def get_lowest_value(game_line: str): 
    game_id, game_set = game_line.split(': ', 1)
    game_id = int(game_id.split(' ')[1])

    red = blue = green = 1
    for set in game_set.split("; "):
        for count_color in set.split(", "):
            count, color = count_color.split(" ")
            count = int(count)
            if color == "red" and int(count) > int(red):
                red = count
            elif color == "green" and int(count) > int(green):
                green = count
            elif color == "blue" and int(count) > int(blue):
                blue = count
    
    return red * green * blue

def part_one():
    with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
        lines = file.readlines()

    score = 0
    for line in lines:
        score += parse_line(line.strip())

    print(f"The answer for part one is: {score}")
    print(score) 

def part_two():
    with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
        lines = file.readlines()

    score = 0
    for line in lines:
        score += get_lowest_value(line.strip())

    print("-----------------")
    print(f"The answer for part two is: {score}")


if __name__ == '__main__':
    # part_one()
    part_two()
