import random 

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10 ]
    card=random.choice(cards)
    return card
 


    
def calculate_score(cards):
    """ Take a List of cards and return the score calculated from the cards  """
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1 )
    return sum (cards)


def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose,oppent has Blackjack"
    elif user_score>21:
        return "Youe went over .you loss"
    elif computer_score>21:
        return "Oppent went over . You win"
    elif user_score>computer_score:
        return "You win"
    else:
        return"You loss"
    
def play_game():
    user_cards=[]
    computer_cards=[]
    is_game_over=False
    for n in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f" your cards:{user_cards},current scroe:{user_score}")
        print(f"Computer's first card:{computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            draw_another_card=input(' do you went to draw another card')
            if draw_another_card=='yes':
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards) 
    print(f"you final hand:{user_cards},final score:{user_score}")
    print(f"Computer's final hand:{computer_cards},final score:{computer_score}")
    print(compare(user_score,computer_score))
while input("Do you want to play a game of BlackJak ? Type 'y' or 'n':\n")=='y':
    play_game()
 