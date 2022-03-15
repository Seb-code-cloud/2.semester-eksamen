#PLUGDK Prototype
#Authors Sebastian, Andreas, Jakob, Jakob og Simon (Gruppe 1)
#Date: 2021-06/09
#Created for educational use

#Please see README.txt before initiating the program


from Specifications_about_charger import *
from Data_over_ladestander import *
from Create_user import *
import time


title = "\t\t\tMENU\t\t\t"

def hello():
    print("\033[H\033[J") 
    print(title)
    print("\n")

def main_menu2():
	hello()
	options = [
		"Coordinates and information about operator",
		"Specifications of a charger",
		"Create new user",
		"Exit Program\n"]
	print("Enter a number to select an option:\n")
	for d, options in enumerate(options):
		print("[" + str(d + 1) + "] " + options)

	choice = int(input("Select an option [1] - [4]: "))


	if choice in range(1,5):
		if choice == 1:
			time.sleep(1)
			Coordinates_Operator(myRecords)
			time.sleep(5)
			main_menu2()
			

		elif choice == 2:
			time.sleep(1)
			information_about_charger()
			time.sleep(4)
			main_menu2()

		elif choice == 3:
			time.sleep(1)
			Create_new_user()

		elif choice == 4:
			hello()
			print("\n")
			print("Quitting.....")
			time.sleep(1.5)
			exit()

	else:
		print("I dont know this action..")
		time.sleep(2)
		main_menu2()