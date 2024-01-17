import random
from art import logo

game_on = False
game_alive = False
repeat = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(logo)

to_play = input("Would you like to play Blackjack? (y or n): ")

def play_blackjack():
    to_play == "y" 
    computer_card1 = random.choice(cards)
    computer_card2 = random.choice(cards)
    player_card1 = random.choice(cards)
    player_card2 = random.choice(cards)
    player_hand = []
    dealer_hand = []

    def computer_sum():
        dealer_hand.append(computer_card1)
        dealer_hand.append(computer_card2)
        return computer_card1 + computer_card2
    def player_sum():
         player_hand.append(player_card1)
         player_hand.append(player_card2)
         return player_card1 + player_card2
    def computer_add(): 
         dealer_hand.append(random.choice(cards))
         return computer_sum() + random.choice(cards)
    def player_add():
         player_hand.append(random.choice(cards))
         return  player_sum() + random.choice(cards)
    

    if to_play == "y":
        game_on = True
        game_alive = True
        computer_sum()
        player_sum()
        print(f"You have drawn {player_hand} for a total of {player_sum()}")
    elif to_play == "n":
        print("See you later")
        game_on = False
        game_alive = False
    else: 
        print("Enter valid number")
        game_on = False
        game_alive = False




    if computer_sum() < 21 and player_sum() < 21:
        while game_alive:
            go_again = input(f"Hit me? (y or n): ")
            computer_add()
            player_add()

            if go_again == "y" and game_alive == True:
                new_computer_sum = computer_sum() + random.choice(cards)
                new_player_sum = player_sum() + random.choice(cards)
                print(f"New total for you is {player_add()}")
            
                if new_computer_sum == 21 and new_player_sum != 21:
                    game_alive = False
                    print(f"Game Over! Dealer wins with a total of {new_computer_sum}")
                elif new_computer_sum != 21 and new_player_sum == 21:
                    game_alive = False
                    print("Game Over! You win")
                elif new_computer_sum > 21: 
                    game_alive = False
                    print(f"Dealer over 21 with a score of {new_computer_sum} -  you win!")
                elif new_player_sum > 21:
                    game_alive = False
                    print("You're over 21. You lose! ") 
                elif new_player_sum == new_computer_sum:
                    game_alive = False
                    print("Draw. So you win. ")
            else: 
                game_alive = False
                if computer_sum() > player_sum():
                    print("Dealer wins with score of {new_computer_sum}") 
                else:
                    print("you win")   

    elif player_sum() == 21 and computer_sum() != 21:
                game_alive = False
                print(f"Game over! You win. Dealer had {computer_sum}")
    elif player_sum() == computer_sum():
         game_alive = False
         print("Draw")
    elif computer_sum() == 21 and player_sum() != 21:
                game_alive = False
                print("Game over! You lose. Dealer had 21 ")
    elif computer_sum() > 21 and player_sum() > 21: 
        game_alive = False
        print(f'You are both out. You had {player_sum} and dealer had {computer_sum}')
    elif player_sum() > 21:
        game_alive= False
        print("You've gone bust")
    elif computer_sum() > 21:
        print(f"Dealer is bust with {computer_sum}")
        game_alive = False
    else: 
        print("Something happened")


    playAgain = input("Would you like to play again? Enter y for Yes and n for No: ")

    if playAgain == "y":
        return True
    else:
        return False


playing = True
while playing == True:
    playing = play_blackjack()



