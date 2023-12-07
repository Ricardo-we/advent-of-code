input_ = open("./input_1.txt", "r").read().split('\n')
letters_values = {
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


class FullHand:
    hand = []
    bid = 0
    score = 0
    same_of_kind = {}

    def __init__(self, hand, bid, score, same_of_kind):
        self.hand = hand
        self.bid = bid
        self.score = score
        self.same_of_kind = same_of_kind


def calc_strength(hand):
    card_values = {}
    strength = 0

    for card in hand:
        if not card in card_values:
            card_values[card] = 0

        card_values[card] += 1

        if card_values[card] > 5:
            return 5

        if card_values[card] > 4:
            strength += 4
        elif card_values[card] > 3:
            strength += 3
        elif card_values[card] > 2:
            strength += 2
        elif card_values[card] > 1:
            strength += 1

    return strength, card_values


def replace_card_letters(hand):
    result = []
    for char in hand.hand:
        result.append(letters_values[char])

    return sorted(result, key=lambda x: -x)


def main(input_):
    hands = []

    for hand in input_:
        hand = hand.split(" ")
        hand[0] = sorted(
            [x for x in hand[0]],
            key=lambda x: -letters_values[x]
        )
        hand[0] = ''.join(hand[0])
        hand[1] = int(hand[1])
        strength, results = calc_strength(hand[0])

        hands.append(FullHand(hand[0], hand[1], strength, results))

    hands.sort(key=lambda x: x.score,)
    result = []

    for hand in hands:
        hand.hand = replace_card_letters(hand)
        result.append(hand)
        # print([letters_values[num[0]] * num[1] for num in hand.same_of_kind.items() if num[1] > 1])
    for num in result[0].same_of_kind.items():
        print(num)            

    result.sort(key=lambda x: -sum([letters_values[num[0]] * num[1] for num in x.same_of_kind.items() if num[1] > 1]))#sum(num for num in x.same_of_kind.values() if num > 1),)

    result_ = 0
    for i, hand in enumerate(result):
        print(hand.bid, i+1)
        result_ += (i+1) * hand.bid

    print(result_)


if __name__ == "__main__":
    main(input_)
