from art import logo
import random
print(logo)

def random_card_generator(c):
    number = c[random.randint(0,12)]
    return number

def hit_function(total_number,random):
    return total_number + random

def stand_function(number,random):
    return number+random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
users_cards1 = random_card_generator(cards)
users_cards2 = random_card_generator(cards)
dealer_cards = random_card_generator(cards)

input("are u ready to play blackjack")
exit_flag = True
while exit_flag:
    total = users_cards1 + users_cards2

    if total == 21:
        print("you win")
        exit_flag = False

    choice = input(f"your cars {users_cards1} & {users_cards2} and the dealer cars is {dealer_cards} so for hit h and for stand s")

    if choice == "h":
        total = hit_function(total_number=total,random=random_card_generator(cards))
    elif choice == "s":
        stand_return = stand_function(number=dealer_cards,random=random_card_generator(cards))
        if stand_return > total:
            print(f"house wins {stand_return} and user=={total}")
            exit_flag = False
        else:
            print(f"you win{total} and {stand_return}")
            exit_flag = False

