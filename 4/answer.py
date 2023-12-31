import sys
import os
import re

input_file = sys.argv[1] 

with open(os.path.join(os.path.dirname(__file__), input_file), 'r') as file:
    lines = file.readlines()

def part_one():
    score = 0
    for line in lines:
        line = line.strip()
        game, cards = line.split(":")
        winning_cards_set, my_cards_set = cards.split("|")
        winning_cards = winning_cards_set.split(" ")
        my_cards = my_cards_set.split(" ")
        
        card_score = 0
        for my_card in my_cards:
            if my_card.isdigit() and my_card in winning_cards:
                if card_score == 0:
                    card_score = 1
                    continue

                card_score = card_score * 2
        score += card_score

    print(f"The answer for part one is: {score}") # 22488

def part_two():
    card_count = 0
    extra_cards = {}

    for card_set, line in enumerate(lines, start=1):
        if card_set not in extra_cards:
            extra_cards.update({card_set: 1})

        i = 1
        while i <= extra_cards[card_set]:
            card_count += 1
            line = line.strip()
            game, cards = line.split(":")
            game = int(re.search(r'\d+', game).group()[0])
            winning_cards_set, my_cards_set = cards.split("|")
            winning_cards = winning_cards_set.split(" ")
            my_cards = my_cards_set.split(" ")
            
            winning_cards_count = 0
            for my_card in my_cards:
                if my_card.isdigit() and my_card in winning_cards:
                    winning_cards_count += 1
                    if card_set + winning_cards_count not in extra_cards:
                        extra_cards.update({card_set + winning_cards_count: 1})
                    
                    extra_cards[card_set + winning_cards_count] += 1

            
            i += 1
    
    print("-----------------")
    print(f"The answer for part two is: {card_count}")

if __name__ == '__main__':
    part_one()
    part_two()
