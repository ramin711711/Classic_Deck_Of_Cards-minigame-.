import random

player1 = []
player2 = []
deck = []

for suit in ["clubs", "diamonds", "hearts", "spades"]:
    for face in ["6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]:
        deck.append((face, suit))

def card_giving(playerhand):
    if deck:
        card = random.choice(deck)
        playerhand.append(card)
        deck.remove(card)

print('Giving each player 6 cards: ')
for _ in range(6): 
    card_giving(player1)
    card_giving(player2)

print('You (player 1), have ', player1)
print('You (player 2), have ', player2)

print('\n')

def card_value(card):
    face, suit = card
    values = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
    return values.get(face, suit)

def valid_card(card, opponent_card):
    return card_value(card) > card_value(opponent_card)

def get_card_from_input(player_hand, input_str):
    for card in player_hand:
        if f"{card[0]} of {card[1]}" == input_str:
            return card
    return None


def play_turn():
    global player1, player2

    while True:
        print('You (player 1), have ', [f"{card[0]} of {card[1]}" for card in player1])
        ans1 = input('Which card do you want to play? (Example: "7 of hearts") ')
        
        card_to_play = get_card_from_input(player1, ans1)
        if card_to_play:
            player1.remove(card_to_play)
            print('\nPlayer 2, you need to defend yourself against:', str(ans1), '\nIf you have a card that can defend you, use it. Otherwise, take the card.')
            print('\nYou (player 2), have ', [f"{card[0]} of {card[1]}" for card in player2])
            ab = input('\nDo you want to defend? Yes/No ')

            if ab == 'Yes':
                ab1 = input('\nWith which card will you defend yourself? (Example: "8 of hearts") ')
                
                defend_card = get_card_from_input(player2, ab1)
                if defend_card and defend_card[1] == card_to_play[1] and valid_card(defend_card, card_to_play):
                    player2.remove(defend_card)
                    print('\nCongrats! You defended yourself.')
                    print('\nYou (player 2), have ', [f"{card[0]} of {card[1]}" for card in player2])
                    
                    ab2 = input('Which card do you want to play? (Example: "9 of diamonds") ')
                    
                    card_to_play2 = get_card_from_input(player2, ab2)
                    if card_to_play2:
                        player2.remove(card_to_play2)
                        print('\nPlayer 1, you need to defend yourself against:', str(ab2), '\nIf you have a card that can defend you, use it. Otherwise, take the card.')
                        print('You (player 1), have ', [f"{card[0]} of {card[1]}" for card in player1])
                        ab3 = input('\nDo you want to defend? Yes/No ')

                        if ab3 == 'Yes':
                            ab4 = input('\nWith which card will you defend yourself? (Example: "10 of spades") ')
                            
                            defend_card2 = get_card_from_input(player1, ab4)
                            if defend_card2 and defend_card2[1] == card_to_play2[1] and valid_card(defend_card2, card_to_play2):
                                player1.remove(defend_card2)
                                print('\nCongrats! You defended yourself.')
                                print('\nYou (player 1), have ', [f"{card[0]} of {card[1]}" for card in player1])
                                print('The game is over! Thanks for playing!')
                                return
                            else:
                                print("You didn't have the card you needed.")
                                player1.append(card_to_play)
                                print('The game is over! Thanks for playing!')
                                return
                        else:
                            print("You didn't have the card you needed.")
                            player2.append(card_to_play)
                            return
                    else:
                        print('Card is not found in your hand.')
                        player2.append(card_to_play)
                        break
                    
                else:
                    print("You didn't have a valid defending card or the suit didn't match.")
                    player2.append(card_to_play)
                    return
            else:
                print("You didn't have the card you needed.")
                player2.append(card_to_play)
                return
        else:
            print('Card is not found in your hand.')
            break
            
                    

# Main game loop
pick = 'Stay'
while pick == 'Stay':
    play_turn()
    pick = input("Do you want to play one more time or not? Leave/Stay ")