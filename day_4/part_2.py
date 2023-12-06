
def main():
    ocurrences = {}
    for i, row in enumerate(open('input2.txt', 'r')):
        if not i in ocurrences:
            ocurrences[i] = 1

        row = row.split(":")[1].strip()
        card, winning_card = [list(map(int, card.split())) for card in row.split(" | ")]
        winned_game = sum(q in card for q in winning_card)        

        print(winned_game)
        print(card, winning_card)

        for game_id in range(i + 1, i + winned_game + 1):
            ocurrences[game_id] = ocurrences.get(game_id, 1) + ocurrences[i]

    return ocurrences
if __name__ == '__main__':
    print(sum(main().values()))