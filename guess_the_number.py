# Mastermind game

chances=0
continue_game=True
player_1_chances=0
player_2_chances=0


def game_start():
    global chances
    while chances<2:
        chances += 1
        if chances % 2!=0:
            player_1 = int(input("Enter Number player 1"))
            guessing_number(player_1, pl=2)
        elif chances % 2==0:
            player_2 = int(input("Enter Number player 2"))
            guessing_number(player_2, pl=1)
    else:
        if player_2_chances > player_1_chances:
            print("player 2 is MASTERMIND")
        elif player_2_chances < player_1_chances:
            print("player 1 is MASTERMIND")


def guessing_number(guessed_number, pl):
    global player_1_chances
    global player_2_chances
    ask_player=int(input(f"What do you think the number is player {pl} ?"))
    if ask_player==guessed_number:
        print(f"player {pl} Guessed it!!")
        game_start()
    else:
        for i in str(guessed_number):
            for j in str(ask_player):
                if i==j:
                    print(f"Digits that you guessed correctly are {i}")

        if pl==1:
            guessing_number(guessed_number,pl)
            player_2_chances+=1
        else:
            guessing_number(guessed_number, pl)
            player_1_chances+=1


game_start()
# This project is made by ANUSHKA.
