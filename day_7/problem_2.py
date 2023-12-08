input_ = open("./input_1.txt", "r").readlines()

letters_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}

def typeof_hand(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0

def calc_strength(hand):
    result = (typeof_hand(hand), [letters_map.get(char, char) for char in hand])    
    return result

plays = []

for line in input_:
    hand = line.split(" ")[0]
    bid = int(line.split(" ")[1])

    plays.append((hand, bid))
    
plays.sort(key=lambda play: calc_strength(play[0]))


total = 0 
for i, play in enumerate(plays):
    total += play[1] * (i + 1) 

print(total)
