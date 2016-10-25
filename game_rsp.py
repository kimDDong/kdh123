"""

This game is called rock-scissors-paper.

When you pay rock and com pays scissors, you can win.
When you pay scissors and com pays paper, you can win.
When you pay paper and com pays rock, you can win.

"""

import random

i = 0
com_win = 0
user_win = 0
a = ["Rock", "Scissors", "Paper"]


while (i < 10):
	computer = random.choice(a)
	print("============================")
	print("Rock Scissors Paper!!")
	user = input("What do you want to pay? :")
	print("============================")
	if computer == "Rock":
		if user == "Rock":
			print("Draw!")
		if user == "Scissors":
			print("You lose..")
			com_win += 1
		if user == "Paper":
			print("You win!!")
			user_win += 1
	if computer == "Scissors":
		if user == "Rock":
			print("You win!!!!!!!!!!!")
			user_win += 1
		if user == "Scissors":
			print("Draw!")
		if user == "Paper":
			print("You lose.!!!!!!!!!!!.")
			com_win += 1
	if computer == "Paper":
		if user == "Rock":
			print("You lose..")
			com_win += 1
		if user == "Scissors":
			print("You win!!")
			user_win += 1
		if user == "Paper":
			print("Draw!")
	i += 1

print("10 games are over.")
print("And....")

if (user_win < com_win):
	print("You are loser.")
elif (com_win < user_win):
	print("You are winner!!")
else:
	print("Draw, bro....")



