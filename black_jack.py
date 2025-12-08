import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
delare_cards=[]
# delare_cards.append(random.choice(cards))

player_cards=[]
# player_cards.append(int(input('select your  card ? \n')))

for n in range(2):
    delare_cards.append(random.choice(cards))
    player_cards.append(int(input('select your  card ? \n')))

sum_delare=delare_cards[0]+delare_cards[1]
sum_player=player_cards[0]+player_cards[1]

while sum_player and sum_delare <21:

    if sum_delare <17:
        delare_cards.append(random.choice(cards))
        sum_delare+=delare_cards[2]
    else:
        player_cards.append(int(input('select your  card ? \n')))
        sum_player+=player_cards[2]
if sum_player and sum_delare <21:
    player_cards.append(int(input('select your  card ? \n')))
    sum_player+=player_cards[3]
    if sum_player <21:
        print('you win')
print(sum_delare)
print(sum_player)
