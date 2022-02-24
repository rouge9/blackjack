import random
from art import logo

print(logo)

def deal_card():
    """Random card Generator"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """calculates card"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user,computer):
    if user == computer:
        return "its a draw"
    elif computer == 0:
        return "sorry computer wins"
    elif user == 0:
        return "user wins"
    elif user > 21:
        return "you went over users loses"
    elif computer > 21:
        return "you went over computer loses"
    elif user > computer:
        return "computer wins you lose"
    else:
        return "you lose"

def play_game():
    user_card = []
    computer_card = []
    is_game_over = False
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    endgame = False
    while not endgame:

        while not is_game_over:
            user_score = calculate_score(user_card)
            computer_score = calculate_score(computer_card)
            print(f"users cards {user_card}")
            print(f"computer card {computer_card[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                user_should_deal = input("to continue press 'y' to end press'n'")
                if user_should_deal == "y":
                    user_card.append(deal_card())
                else:
                    is_game_over = True

        while computer_score !=0 and computer_score < 17:
            computer_card.append(deal_card())
            computer_score = computer_score(computer_card)

        print(f"users final card {user_card}")
        print(f"computers final card{computer_card}")
        print(compare(user_score,computer_score))
play_game()
while input("do u want to continue y for yes or n for no") == "y":
    play_game()
