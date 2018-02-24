"""
Compare two playing cards.
Print a winner card.
Print "Error" if there is no winner.
"""
suit = ("C", "D", "H", "S")
value = ("6", "7", "8", "9", "10", "J", "Q", "K", "A")

card_in = input()
card = card_in.split()
trump_card = input()

first_card = card[0]
first_card_suit = first_card[-1:]
first_card_value = first_card[:-1]

second_card = card[1]
second_card_suit = second_card[-1:]
second_card_value = second_card[:-1]

if first_card_suit == second_card_suit:
    if value.index(first_card_value) > value.index(second_card_value):
        print("First")
    else:
        if value.index(first_card_value) < value.index(second_card_value):
            print("Second")
        else:
            print("Error")
else:
    if trump_card != first_card_suit and trump_card != second_card_suit:
        print("Error")
    else:
        if trump_card == first_card_suit:
            print("First")
        else:
            print("Second")
