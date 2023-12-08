import sys
import os 
from pprint import pprint

input_file = sys.argv[1] 

with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
    lines = file.readlines()

def part_one():
    time_list = lines[0].strip().split(":")[1].split(" ")
    distance_list = lines[1].strip().split(":")[1].split(" ")

    time_list = [t for t in time_list if t.isdigit()]
    distance_list = [t for t in distance_list if t.isdigit()]

    print(time_list)
    print(distance_list)

    races = []
    for i, t in enumerate(time_list):
        races.append({
            "time": int(time_list[i]),
            "distance": int(distance_list[i])
        })

    possibilities_sum = 1
    for race in races:
        hold_ms = 0
        race_time = race["time"]
        race_possibilities = 0
        while hold_ms < race_time:
            time_left = race_time - hold_ms
            distance_travelled = hold_ms * time_left
            if distance_travelled > race["distance"]:
                race_possibilities += 1

            print(f"Holding it {hold_ms}ms, {time_left}ms left, {distance_travelled} distance travelled")
            hold_ms += 1
        
        possibilities_sum = possibilities_sum * race_possibilities
        print(f"Next race! Possibilities: {race_possibilities}")

    pprint(races)
    print(f"The answer for part one is: {possibilities_sum}")

def part_two():
    race_time = int(lines[0].strip().split(":")[1].replace(" ", ""))
    race_distance = int(lines[1].strip().split(":")[1].replace(" ", ""))

    hold_ms = 0
    race_possibilities = 0

    while hold_ms < race_time:
        time_left = race_time - hold_ms
        distance_travelled = hold_ms * time_left
        if distance_travelled > race_distance:
            race_possibilities += 1
        hold_ms += 1

    print("-----------------")
    print(f"The answer for part two is: {race_possibilities}")

if __name__ == '__main__':
    # part_one()
    part_two()
