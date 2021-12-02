import random, time
#blackjack game

playerwins = 0
playerlose = 0
play_again = "Y"
autolose = "n"
games = 0

while play_again == "Y":
    games = games + 1
    # Dealer cards
    dealer_cards = []
    # player cards
    player_cards = []
    # deal the cards
   
    #dealer cards
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1,11))
        if len(dealer_cards) == 2:
            print("Dealer has ? & ", dealer_cards[1])
    
    #player_cards

    while len(player_cards) != 2:
        player_cards.append(random.randint(1,11))
        if len(player_cards) == 2:
            print("You have " + str(player_cards[1]) + " & " + str(player_cards[0]) + " which equals " + str(sum(player_cards)))

    if sum(player_cards) < 21:
        action_taken = input("Do you want to (stay) or (hit)? " )
        while action_taken == "hit":
            new_card = random.randint(1,11)
            if new_card + sum(player_cards) >= 21:
                player_cards.append(new_card)
                action_taken = "stay"
            else:
                player_cards.append(new_card)
                print("You now have a total of " + str(sum(player_cards)) + " from these cards", player_cards)
                action_taken = input("Do you want to (stay) or (hit)? ")

    if sum(player_cards) == 21:
        print("Your cards are now " + str(player_cards) + " calculating " + str(sum(player_cards)) + ". Blackjack!")
    elif sum(player_cards) > 21:
        print("Your cards are now " + str(player_cards) + " calculating " + str(sum(player_cards)) + ". You bust!")
    else:
        print("You now have a total of " + str(sum(player_cards)) + " from these cards", player_cards)

#dealer plays

    if sum(player_cards) > 21:
        print("\n")
        print("You lose the game.")
        autolose = "y"
    else:
        print("Now the Dealer plays")
        time.sleep(2)
        if sum(dealer_cards) > 17:
            print("Dealer has " + str(dealer_cards) + " calculating " + str(sum(dealer_cards)))
        else:
            print("Dealer has ",dealer_cards)
            dealer_hits = True
            while dealer_hits == True:
                print("Dealer hits...")
                new_dealer_card = random.randint(1,11)
                dealer_cards.append(new_dealer_card)
                time.sleep(1)
                print("Dealer cards are now " + str(dealer_cards) + " calculating " + str(sum(dealer_cards)))
                time.sleep(2)
                if sum(dealer_cards) < 17:
                    dealer_hits = True
                else:
                    dealer_hits = False

    # compare the sums of the cards between Dealer and Player
    # if Player card sum is greater than 21 = Bust
    # if Player card sum is less than 21 = option hit or stay
    # if Player option stay compare sum of Dealer v Player
    # if Player sum < 21 && > Dealer sum = Player Wins!
    # if Player sum is < Dealer sum = Player loses

    if autolose == "y":
        print("\n")
    else:
        if sum(dealer_cards) > 21:
            print("You win the Dealer over went 21 and busted!")
        elif sum(dealer_cards) == 21:
            print("The Dealer has blackjack! ")
        else:
            print()
    if sum(dealer_cards) > 21:
        if sum(player_cards) <= 21:
            print("\n")
            print("You win the Game!")
            playerwins = playerwins+1
        else:
            print("\n")
            print("You lose the game.")
            playerlose = playerlose +1
    else:
        if sum(player_cards) == sum(dealer_cards):
            print("\n")
            print("You tied with the dealer, It's a Draw.")
            playerwins = playerwins + 0
            playerlose = playerlose + 0
        else:
            if sum(player_cards) > 21:
                playerlose = playerlose + 1
            elif sum(player_cards) > sum(dealer_cards):
                print("\n")
                print("You win the game!")
                playerwins = playerwins + 1
            else:
                print("\n")
                print("You lose the game.")
                playerlose = playerlose + 1

    time.sleep(1)
    
    time.sleep(1)
    play_again = input("\nDo you want to play again? y/n ")
    play_again = play_again.upper()
    print("Thank you for playing Blackjack, you played " + str(games) + " games. You won " + str(playerwins) + " time(s), and lost " + str(playerlose) + " time(s).")

    win_percent = (playerwins/games)*100
    win_percent = round(win_percent)
    
#win rate percentage
print("Winning Percentage = " + str(win_percent) + "%")