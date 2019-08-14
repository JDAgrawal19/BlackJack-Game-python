from Table import Table
from GameRunner import GameRunner

print("Welcome to BlackJack")

while True:
    number_of_decks = int(input("Number of decks in range (1, 8) you want to play with  "))
    if GameRunner.validate_no_of_decks(number_of_decks) is False:
        print("Entered Number Out of Range, Enter Again")
    else:
        break


while True:
    number_of_players = int(input("Numbers of players between 3 to 10 "))
    if GameRunner.validate_no_of_players(number_of_players) is False:
        print("Entered Number out of Range, Enter Again")
    else:
        break


print("Enter Name Of players")
name_of_players = [input() for i in range(number_of_players)]


table = Table(number_of_decks, number_of_players, name_of_players)


# distribute first card to everyone
table.distribute_card_to_dealer()
for player in table.players:
    table.distribute_card_to_player(player)


# distribute second card to everyone
table.distribute_card_to_dealer()
for player in table.players:
    table.distribute_card_to_player(player)



# final card distribution to players

for player in table.players:
    print("Dealer {}".format(table.show_first_card_of_dealer()))
    print("Players {}".format(table.show_cards_of_players()))
    print("{} your cards are {}".format(player.name, player.hand))
    while True:
        x = input("Hit Or Stand ")
        if x.lower() == 'hit':
            table.distribute_card_to_player(player)
            print("{} your cards Now {} and Your Score is {}"
                  .format(player.name, player.hand, table.calc_score(player)))
            if player.check_if_player_is_busted() is True:
                print("{} you are Busted".format(player.name))
                break
        elif x.lower() == 'stand':
            print("{} your cards Now {} and Your Score is {}"
                  .format(player.name, player.hand, table.calc_score(player)))
            break
        else:
            print("Type only Hit or Stand")

# final cards to dealer

while True:
    print("Dealer {} cards are {}".format(table.dealer.name, table.dealer.hand))
    dealer_score = table.calc_score(table.dealer)
    print("Score of Dealer is {}".format(dealer_score))
    if dealer_score < 17:
        table.distribute_card_to_dealer()
    else:
        break


# get the winners
results = table.get_the_results_of_game()
print(results)

