#DESIGN A ROCK PAPER SCISSOR GAME IN PYTHON [TASK 2]
import random
options=("ROCK" ,"PAPER" ,"SCISSOR")
player=None
computer=random.choice(options)
while player not in options:
    player=input("ENTER A CHOICE(ROCK ,PAPER, SCISSOR):")
print(f"Player:{player}")
print(f"computer:{computer}")
if player==computer:
    print("IT IS A TIE")
elif player=="ROCK" and computer=="SCISSOR":
    print("IT'S AMAZING YOU WIN")
elif player=="PAPER" and computer=="ROCK":
    print("IT'S AMAZING YOU WIN")
elif player=="SCISSOR" and computer=="PAPER":
    print("IT'S AMAZING YOU WIN")
else:
    print("AH! YOU LOSE ")
    print("TRY AGAIN")
