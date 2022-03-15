#PLUGDK Prototype
#Authors Sebastian, Andreas, Jakob, Jakob og Simon (Gruppe 1)
#Date: 2021-06/09
#Created for educational use

#Please see README.txt before initiating the program






#this module is imported to help connect to out SQL database and makes it possible to access and manipulate it 
import mysql.connector

#this function will work as our personal connector, with the users own SQL information. We will use dbconnect() multiple times thourgh our program
def dbconnect():
	connection = mysql.connector.connect(
		host="localhost",
		user="root",
		password="YOUR CODE HERE",
		database="Ladestander_database")
	return connection
