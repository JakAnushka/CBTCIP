import random
# printing or initializing the symbols.
d={"rock": '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

    "paper": '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

    "scissors": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}

sym='''
╦═╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔═╗╔═╗╦═╗  ╔═╗╔═╗╦╔═╗╔═╗╔═╗╦═╗╔═╗
╠╦╝║ ║║  ╠╩╗  ╠═╝╠═╣╠═╝║╣ ╠╦╝  ╚═╗║  ║╚═╗╚═╗║ ║╠╦╝╚═╗
╩╚═╚═╝╚═╝╩ ╩  ╩  ╩ ╩╩  ╚═╝╩╚═  ╚═╝╚═╝╩╚═╝╚═╝╚═╝╩╚═╚═╝'''

# defining the function that we will use


def game_start():
    print(sym)
    user_chance()


def user_chance():
    user_turn = input("So what you gonna throw(rock/paper/scissors)").lower()
    if user_turn=="rock":
        print(d["rock"])
        comp_chance(user_turn)
    elif user_turn=="paper":
        print(d["paper"])
        comp_chance(user_turn)
    elif user_turn=="scissors":
        print(d["scissors"])
        comp_chance(user_turn)
    else:
        print("I think you forgot to put your input :(")


def comp_chance(u_c):
    L = ["rock", "paper", "scissors"]
    l = len(L)-1
    random_choice = random.randint(0, l)
    computer_turn=L[random_choice]
    print("Now comp turn")
    if computer_turn=="rock":
        print(d["rock"])
        win_loss(u_c, computer_turn)

    elif computer_turn=="paper":
        print(d["paper"])
        win_loss(u_c, computer_turn)

    elif computer_turn=="scissors":
        print(d["scissors"])
        win_loss(u_c, computer_turn)

# win or loose


def win_loss(u, c):
    if u==c:
        print("It's a draw match")
    elif u=="rock" and c=="scissors":
        print("YOU WON!!")
    elif u=="paper" and c=="rock":
        print("you won!!")
    elif u=="scissors" and c=="paper":
        print("you won")
    else:
        print("You loose")


game_play = True
while game_play:
    user_choice=input("wanna play this game(yes/no):").lower()
    if user_choice=="yes":
        game_start()
        game_play=True
    else:
        game_play=False

# this project is made by ANUSHKA.