import random

cards = [11 ,2 ,3 ,4,5,6,7,8,9,10,10,10,10]

def dealer():
    """add a random card from deck / return a random choice"""
    card = random.choice(cards)
    return card


def scoring(cards):
    """calculate the total of the score of the cards of user/computer"""
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def copmpare(u_s, c_s):
    if u_s == c_s:
        print("draw nigga")
    elif u_s == 0:
        print("win u have a black jack")
    elif c_s == 0:
        print("lose computer have a black jack")
    elif u_s > 21:
        print("bust")
    elif c_s > 21:
        print(f"computer bust computer score was {computer_score}")
    elif u_s > c_s and u_s < 21:
        print("u win")
    else:
        print("u lose ")



user_card1 = []
computer_card1 = []

game_over = False

user_start = random.choices(cards, k=2)

computer_start = random.choices(cards, k=2)

user_card1.extend(user_start)

computer_card1.extend(computer_start)

while not game_over:

    user_score = scoring(user_card1)
    computer_score = scoring(computer_card1)

    print(f"user cards are {user_card1} and user score is {user_score}")
    print(f"computer first card is {computer_card1[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        user_add_card = input("u wanna add another card ? y or n \n").lower()
        if user_add_card == "y":
            user_card1.append(dealer())
            print(f"{user_card1}")

        elif user_add_card == "n":
            game_over = True
            
        else:
            print("not valid")
            game_over = True
while computer_score != 0 and computer_score < 17:
    computer_card1.append(dealer())
    computer_score = scoring(computer_card1)

copmpare(user_score, computer_score)
print(f"the user score was {user_score} and the cards were{user_card1}")
print(f"computer score was {computer_score}and cards were {computer_card1}")