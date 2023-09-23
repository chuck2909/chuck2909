#**********************************
# File: roshambo.py
# This program plays a game
# Written by Cannon
#*********************************
import random


# now let's make some constants to keep track of the move choice and winner
HUMANWINS=1
COMPUTERWINS=2
TIE=0
ROCK=1
PAPER=2
SCISSORS=3
        
#winner = 0 is a tie (we can use the constant TIE for this)
#winner = 1 means human wins (we can use the constant HUMANWINS for this)
#winner = 2 means computer wins (we can use the constant COMPUTERWINS for this)

winner=HUMANWINS #let's initialize the winner to be the human player


#Print greeting

print("Welcome to the true test of personhood")
print("Welcome to roshambo death match")

playerMove = int(input("pick rock/paper/scissors 1/2/3: "))

computerMove = int(random.random()*3+1)
if computerMove==ROCK:
    computerChoice='Rock'
if computerMove==PAPER:
    computerChoice='Paper'
if computerMove==SCISSORS:
    computerChoice='Scissors'
    
print("Player 2 chooses " + computerChoice +" !") 
    

# Determine who the winner is,
# Remember we set the default to the human player
# so we only need to check for ties or computer vicory

if playerMove==ROCK and computerMove==PAPER:
  winner=COMPUTERWINS
if playerMove==PAPER and computerMove==SCISSORS:
  winner=COMPUTERWINS
if playerMove==SCISSORS and computerMove==ROCK:
  winner=COMPUTERWINS
if playerMove==computerMove:
  winner=TIE

# Print who the winner is

if winner==HUMANWINS:
  print("you win!")
if winner==COMPUTERWINS:
  print("Player 2 wins!")
if winner==TIE:
  print("It's a tie!")


 

    # print goodbye

print( "so long sucker")
