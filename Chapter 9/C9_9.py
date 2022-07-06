import random

deck = {
    "Ace of Spades": 1,
    "2 of Spades": 2,
    "3 of Spades": 3,
    "4 of Spades": 4,
    "5 of Spades": 5,
    "6 of Spades": 6,
    "7 of Spades": 7,
    "8 of Spades": 8,
    "9 of Spades": 9,
    "10 of Spades": 10,
    "Jack of Spades": 10,
    "Queen of Spades": 10,
    "King of Spades": 10,
    "Ace of Hearts": 1,
    "2 of Hearts": 2,
    "3 of Hearts": 3,
    "4 of Hearts": 4,
    "5 of Hearts": 5,
    "6 of Hearts": 6,
    "7 of Hearts": 7,
    "8 of Hearts": 8,
    "9 of Hearts": 9,
    "10 of Hearts": 10,
    "Jack of Hearts": 10,
    "Queen of Hearts": 10,
    "King of Hearts": 10,
    "Ace of Clubs": 1,
    "2 of Clubs": 2,
    "3 of Clubs": 3,
    "4 of Clubs": 4,
    "5 of Clubs": 5,
    "6 of Clubs": 6,
    "7 of Clubs": 7,
    "8 of Clubs": 8,
    "9 of Clubs": 9,
    "10 of Clubs": 10,
    "Jack of Clubs": 10,
    "Queen of Clubs": 10,
    "King of Clubs": 10,
    "Ace of Diamonds": 1,
    "2 of Diamonds": 2,
    "3 of Diamonds": 3,
    "4 of Diamonds": 4,
    "5 of Diamonds": 5,
    "6 of Diamonds": 6,
    "7 of Diamonds": 7,
    "8 of Diamonds": 8,
    "9 of Diamonds": 9,
    "10 of Diamonds": 10,
    "Jack of Diamonds": 10,
    "Queen of Diamonds": 10,
    "King of Diamonds": 10,
}
hand_value1 = 0
hand_value2 = 0
card1_set = set()
card2_set = set()
deck_list = list(deck)
deck_set = set(deck_list)
print(deck_set)

while hand_value1 < 21 or hand_value2 < 21:

    for count in range(len(deck)):
        if count % 2 == 0:
            card = random.choice(deck_list)
            print(card)
            card1_set = card1_set.update(card)
            print(card1_set)
            hand_value1 += deck[card]
            count += 1
        if count % 2 == 1:
            card = random.choice(deck_list)
            card2_set = card2_set.update(card)
            hand_value2 += deck[card]
            count += 1
        deck_set = deck_set - card1_set - card2_set
        deck_list = list(deck_set)
    print("Cards dor player 1 are : ")
    print(card1_set)
    print("Cards dor player 2 are : ")
    print(card2_set)

    if hand_value1 > hand_value2:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
