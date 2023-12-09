# abrir el archivo
from typing import Any


with open("day4\\input.txt") as file:
    content = file.read()
    lines = content.splitlines()  # guardar las filas en la lista

# lines = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
#          'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
#          'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
#          'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
#          'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
#          'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']


def to_dict(line: str) -> dict[str, Any]:
    card, numbers = line.split(":")
    _, card_number = card.split()
    winners, card_numbers = numbers.split("|")
    return {
        "number": int(card_number),
        "winners": [int(i) for i in winners.split()],
        "card_numbers": [int(i) for i in card_numbers.split()],
        "count": 1,
    }


def count_wins(card: dict[str, Any]) -> int:
    count = 0
    for win_number in card["winners"]:
        count += card["card_numbers"].count(win_number)
    return count


def copies(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for i, card in enumerate(cards):
        matches = count_wins(card)
        if count_wins(card) > 0:
            matches = count_wins(card)
            while matches > 0:
                cards[matches + i]["count"] += card["count"]
                matches -= 1
    return cards


def test(line: str) -> None:
    return print(count_wins(to_dict(line)))


if __name__ == "__main__":
    total_points = []
    cards = []
    for card in lines:
        cards.append(to_dict(card))

    print(sum(card["count"] for card in copies(cards)))
