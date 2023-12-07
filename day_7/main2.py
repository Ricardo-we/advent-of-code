# Calc strengths of each hand
# Order by strength
# Compare each hand with the sorted next one 
# Re order the list based on each element strength

input_ = open("./input_1.txt", "r").read().split('\n')

ranks = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "1": 1,
}

combos = {
    "five_of_a_kind": 6,
    "four_of_a_kind": 5,
    "full_house": 4,
    "three_of_a_kind": 3,
    "two_pair": 2,
    "one_pair": 1,
}

class Hand:
    hand = []
    bid = 0
    score = 0

    def __init__(self, hand, bid, score,):
        self.hand = hand
        self.bid = bid
        self.score = score



def calc_strn():
    pass

def calc_strength(hand):
    pass


# def calc_strength(hand):
#     repeated = {}

#     for card in hand:
#         repeated[card] = 1 if not card in repeated else repeated[card] + 1

#     return sum([x for x in repeated.values() if x > 1]) - 1


# hands = []

# for hand in input_:
#     hand = hand.split(" ")
#     hand[1] = int(hand[1])
#     strength = calc_strength(hand[0])
#     hands.append(Hand(hand[0], hand[1], strength,))

# hands.sort(key=lambda x: x.score,)
# # hands = list(map(lambda x: Hand(sorted([ranks[card] for card in x.hand], key=lambda x: -x),x.bid, x.score), hands))
# # hands.sort(key=lambda x: x.hand[0],)
# # hands.sort(key=lambda x: x.score,)

# sorted(hands, key=lambda x: -ranks[x.hand[0]],)

# for hand in hands:
#     print(hand.score, hand.hand, hand.bid)

# 1 765
# 2 220
# 3 28
# 4 684
# 5 483


