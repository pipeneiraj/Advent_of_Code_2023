from typing import Any

with open("inputs\\input7.txt") as f:
    file = f.read().splitlines()

lines = [i.split(" ") for i in file]

hands = [{"id": i, "cards": hand[0], "bid": hand[1]} for i, hand in enumerate(lines)]


def order_by_type(hands: list[dict[Any, Any]]):
    # 6: Five of a kind
    # 5: Four of a kind
    # 4: Full house (pair and trio)
    # 3: Three of a kind
    # 2: Two pair
    # 1: One pair
    # 0: High card
    five, four, full, three, two, one, grater = [], [], [], [], [], [], []
    for hand in hands:
        card_s = set()
        for card in hand["cards"]:
            card_s.add(card)

        size = len(card_s)

        if size == 5:
            hand["type"] = 0
            grater.append(hand)
        elif size == 4:
            hand["type"] = 1
            one.append(hand)
        elif size == 3:
            if (
                hand["cards"].count(hand["cards"][0]) == 2
                or hand["cards"].count(hand["cards"][1]) == 2
            ):
                two.append(hand)
                hand["type"] = 2
            else:
                three.append(hand)
                hand["type"] = 3
        elif size == 2:
            if (
                hand["cards"].count(hand["cards"][0]) == 2
                or hand["cards"].count(hand["cards"][0]) == 3
            ):
                full.append(hand)
                hand["type"] = 4
            else:
                four.append(hand)
                hand["type"] = 5
        else:
            five.append(hand)
            hand["type"] = 6

    five = ordering(five)
    four = ordering(four)
    full = ordering(full)
    three = ordering(three)
    two = ordering(two)
    one = ordering(one)
    grater = ordering(grater)

    return five + four + full + three + two + one + grater


def ordering(hand_list=list[dict[Any, Any]]) -> list[dict[Any, Any]]:
    n = len(hand_list)
    swapped = False
    for i in range(n - 1):  # itera sobre la lista
        for j in range(n - i - 1):  # itera sobre la lista + 1
            if compare_cards(hand_list[j]["cards"], hand_list[j + 1]["cards"], 0):
                swapped = True
                hand_list[j], hand_list[j + 1] = hand_list[j + 1], hand_list[j]
        if not swapped:
            break
    return hand_list


def compare_cards(cards1: str, cards2: str, index: int) -> bool:
    if index == 5:
        return True
    else:
        card1 = card_to_num(cards1[index])
        card2 = card_to_num(cards2[index])
        if card1 < card2:
            return True
        elif card1 > card2:
            return False
        else:
            return True * compare_cards(cards1, cards2, index + 1)


def card_to_num(card: str) -> int:
    if card == "A":
        return 14
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 11
    elif card == "T":
        return 10
    else:
        return int(card)


if __name__ == "__main__":
    ordered_hands = order_by_type(hands)

    for i, hand in enumerate(ordered_hands):
        hand["rank"] = len(ordered_hands) - i

    sum = 0
    for hand in ordered_hands:
        sum += int(hand["bid"]) * hand["rank"]

    print(sum)
