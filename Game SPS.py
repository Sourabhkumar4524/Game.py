import random

def game():
    while True:
        n = input("Enter choice (stone,paper,scissors):")     # user input their choice 
        x = random.choice(["stone","paper","scissors"])       # Computer pick random choice from the list
        print("Computer choice",x)                            # print computer choice

        if n == x:
            print("it's draw")                                
    # Stone beats scissors,Paper beats stone, Scissors beat paper
    # If any of these are true, the user wins
        elif (n == "stone" and x == "scissors") or \
             (n == "paper" and x == "stone") or \
             (n == "scissors" and x == "paper"):
            print("You win!")
        else:
            print("you lost!")                          # If it’s not a draw and the user didn’t win, then the computer must have won.

game()

