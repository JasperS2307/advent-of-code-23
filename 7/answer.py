import sys
import os
from pprint import pprint
import re
input_file = sys.argv[1]

with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
    lines = file.readlines()


class Hand:
    def __init__(self, line: str):
       self.cards, self.bid = line.split(" ")
       self.cards = self.cards\
        .replace("A", "Z")\
        .replace("K", "Y")\
        .replace("T", "A")

CARDS_MAP = {
    "HIGH_CARDS": [], "ONE_PAIR": [], "TWO_PAIR": [], "THREE_OAK": [],
    "FULL_HOUSE": [], "FOUR_OAK": [], "FIVE_OAK": [],
}

hands = [Hand(l.strip()) for l in lines]

CARDS_TO_VALUES_MAP = {
    "A": 0,
    "K": 1,
    "Q": 2,
    "J": 3,
    "T": 4,
    "9": 5,
    "8": 6,
    "7": 7,
    "6": 8,
    "5": 9,
    "4": 10,
    "3": 11,
    "2": 12
}

MULTIPLIER = 1
TOTAL_SCORE = 0
def calculate_score():
    multiplier = 1
    total_score = 0

    print("HIGH CARDS:")
    for set_hand in CARDS_MAP["HIGH_CARDS"]:
        print(set_hand.cards)
        total_score += (int(set_hand.bid) * multiplier)
        multiplier += 1

    print("ONE PAIR:")
    for set_hand in CARDS_MAP["ONE_PAIR"]:
        print(set_hand.cards)
        total_score += (int(set_hand.bid) * multiplier)
        multiplier += 1

    print("TWO PAIR:")
    for set_hand in CARDS_MAP["TWO_PAIR"]:
        print(set_hand.cards)
        total_score += (int(set_hand.bid) * multiplier)
        multiplier += 1

    print("THREE OAK:")
    for set_hand in CARDS_MAP["THREE_OAK"]:
        print(set_hand.cards)
        total_score += (int(set_hand.bid) * multiplier)
        multiplier += 1

    print("FULL HOUSE:")
    for set_hand in CARDS_MAP["FULL_HOUSE"]:
        print(set_hand.cards)
        total_score += (int(set_hand.bid) * multiplier)
        multiplier += 1

    print("FOUR OAK:")
    for set_hand in CARDS_MAP["FOUR_OAK"]:
        print(set_hand.cards)
        total_score += (int(set_hand.bid) * multiplier)
        multiplier += 1

    print("FIVE OAK:")
    for set_hand in CARDS_MAP["FIVE_OAK"]:
        print(set_hand.cards)
        total_score += (int(set_hand.bid) * multiplier)
        multiplier += 1

    return total_score

def part_one():
    for hand in hands:
        card_set_count = {}
        for card in hand.cards:
            card_set_count[card] = len(re.findall(rf'{card}', hand.cards))

        cards_map_key = ""
        if len(card_set_count) == 1:
            cards_map_key = "FIVE_OAK"
        elif len(card_set_count) == 2:
            for card in card_set_count:
                count = card_set_count[card]
                cards_map_key = "FULL_HOUSE" if count == 3 or count == 2 else "FOUR_OAK"
                break
        elif len(card_set_count) == 3:
            for card in card_set_count:
                count = card_set_count[card]
                if count == 1: continue
                cards_map_key = "TWO_PAIR" if count == 2 else "THREE_OAK"
                break
        elif len(card_set_count) == 4:
            cards_map_key = "ONE_PAIR"
        elif len(card_set_count) == 5:
            cards_map_key = "HIGH_CARDS"

        # print(cards_map_key)
        CARDS_MAP[cards_map_key].append(hand)

    for cards_map_key in CARDS_MAP:
        CARDS_MAP[cards_map_key] = sorted(CARDS_MAP[cards_map_key], key=lambda x:x.cards)

    print(f"The answer for part one is: {calculate_score()}")

def part_two():
    for hand in hands:
        card_set_count = {}
        for card in hand.cards:
            card_set_count[card] = len(re.findall(rf'{card}', hand.cards))

        cards_map_key = ""
        jokers_in_hand = len(re.findall(r'J', hand.cards))

        if len(card_set_count) == 1:
            cards_map_key = "FIVE_OAK"
        elif len(card_set_count) == 2:
            for card in card_set_count:
                count = card_set_count[card]
                if count == 3 or count == 2:
                    if jokers_in_hand == 2:
                        cards_map_key = "FIVE_OAK"
                    elif jokers_in_hand == 1:
                        cards_map_key = "FOUR_OAK"
                    else:
                        cards_map_key = "FULL_HOUSE"
                else:
                    if jokers_in_hand == 1:
                        cards_map_key = "FIVE_OAK"
                    else:
                        cards_map_key = "FOUR_OAK"
                break
        elif len(card_set_count) == 3:
            for card in card_set_count:
                count = card_set_count[card]
                if count == 1: continue
                if count == 2:
                    if jokers_in_hand == 2:
                        cards_map_key = "FOUR_OAK"
                    elif jokers_in_hand == 1:
                        cards_map_key = "FULL_HOUSE"
                    else:
                        cards_map_key = "TWO_PAIR"
                else:
                    if jokers_in_hand == 1:
                        cards_map_key = "FOUR_OAK"
                    else:
                        cards_map_key = "THREE_OAK"
                break
        elif len(card_set_count) == 4:
            if jokers_in_hand == 1:
                cards_map_key = "THREE_OAK"
            else:
                cards_map_key = "ONE_PAIR"
        elif len(card_set_count) == 5:
            if jokers_in_hand == 1:
                cards_map_key = "ONE_PAIR"
            else:
                cards_map_key = "HIGH_CARDS"

        # print(cards_map_key)
        CARDS_MAP[cards_map_key].append(hand)

    for cards_map_key in CARDS_MAP:
        CARDS_MAP[cards_map_key] = sorted(CARDS_MAP[cards_map_key], key=lambda x:x.cards)

    print("-----------------")
    print(f"The answer for part two is: {calculate_score()}") # 249726565

    # 251371044 TOO HIGH
    # 249726565 TOO LOW

if __name__ == '__main__':
    part_one()
    # part_two()
