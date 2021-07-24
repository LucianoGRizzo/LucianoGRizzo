p1_input = input("Player 1, please input your selection (rock, paper, scissors): ").lower()
p2_input = input("Player 2, please input your selection (rock, paper, scissors): ").lower()
r = 'rock'
p = 'paper'
s = 'scissors'
import os

inputs = [r, p, s]
winner = []
loser = []
tie = False

if p1_input in inputs and p2_input in inputs:
    if p1_input == p2_input:
        tie = True
    elif p1_input == r and p2_input == s:
        winner = ['Player 1', p1_input]
        loser = ['Player 2', p2_input]
    elif p1_input == p and p2_input == r:
        winner = ['Player 1', p1_input]
        loser = ['Player 2', p2_input]
    elif p1_input == s and p2_input == p:
        winner = ['Player 1', p1_input]
        loser = ['Player 2', p2_input]
    elif p2_input == r and p1_input == s:
        winner = ['Player 2', p2_input]
        loser = ['Player 1', p1_input]
    elif p2_input == p and p1_input == r:
        winner = ['Player 2', p2_input]
        loser = ['Player 1', p1_input]
    elif p2_input == s and p1_input == p:
        winner = ['Player 2', p2_input]
        loser = ['Player 1', p1_input]
else:
    print("Please input either rock, paper, or scissors for both Player 1 and Player 2.")

if tie:
    print("Tie game")
elif winner != [] and loser != []:
    print(winner[0] + " beats " + loser[0] + " in an epic battle between " + winner[1] + " and " + loser[1] + "!")
else:
    print("ERROR please restart")