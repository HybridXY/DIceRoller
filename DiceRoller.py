import sys
import random
import os

#This the dice game, whoever rolls the higher amount pvcpu

def game_logics(dice,rounds):
 

	cpu_score = 0

	user_score = 0

	for x in range(0,rounds):

		ur = random.randrange(1,dice)

		cpr = random.randrange(1,dice)

		if(cpr == ur):

			print("\nLooks like we have a tie!!!")

			print("Computer rolled: %d  User rolled: %d" %(cpr,ur))


		elif(cpr > ur):
					
			print("\nSorry you lost this round!!!")

			print("Computer rolled: %d  User rolled: %d" %(cpr,ur))

			cpu_score += 1

		elif(cpr < ur):
					
			print("\nCongrats you WON this round!!!")

			print("Computer rolled: %d  User rolled: %d" %(cpr,ur))

			user_score += 1

		input("Next Round...Press enter to roll the dice")

	print("Game Results: Cpu: %d  User: %d" %(cpu_score,user_score))

#******************************************************************************

ans = "Yes"

print("\t\t\t--------------------------------------------------------------\n")

print ("\t\t\t***WELCOME TO THE DICE ROLLER GAME......TEST YOUR LUCK AND ENJOY***\n")

print("\t\t\t---------------------------------------------------------------\n\n\n")


while(ans != "No"):
	
	response = input("\t\t\t\t\t\t\tAre you ready to test your luck?\n\n"+"\n"+"\t\t\t\t\t\t\tType Yes or  No: ").capitalize().rstrip()

	if response == "Yes" :
				
		print("\n\t\t\t\t\t\t\tChoose a dice to roll: \n")
	
		print("\t\t\t\t\t\t\t\t1----6-side\n")
				
		print("\t\t\t\t\t\t\t\t2----12-side\n")
				
		print("\t\t\t\t\t\t\t\t3----32-side\n")

		dice_choice = int(input("Your choice is: "))
				
		if dice_choice == 1:

			rounds = int(input("\nEnter the amount of rounds you would like to play: "))
					
			game_logics(6,rounds)
				
		elif dice_choice == 2:
					
			rounds = int(input("\nEnter the amount of rounds you would like to play: "))
					
			game_logics(12,rounds)
					
		elif dice_choice == 3:

			rounds = int(input("\nEnter the amount of rounds you would like to play: "))
					
			game_logics(32,rounds)

		ans = input("\nHavent had enough? You can always play again :D\n Yes or No: ").strip()

print("Thanks for playing IT WAS FUN :D!!!")
