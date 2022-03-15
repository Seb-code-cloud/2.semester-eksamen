#PLUGDK Prototype
#Authors Sebastian, Andreas, Jakob, Jakob og Simon (Gruppe 1)
#Date: 2021-06/09
#Created for educational use

#Please see README.txt before initiating the program


#importning the file Databaseconnect.py to connect to the MySQL database 
#importing beautifultable gives us some more tools to print out nice tables insted of boring normal looking lists.
import Databaseconnect as thisDatabase
from beautifultable import BeautifulTable

#connect to database
thisConn = thisDatabase.dbconnect()

title5 = "\t\t\tPLUGDK\t\t\t\n"

def hello5():
    print("\033[H\033[J") 
    print(title5)


#here we create a search function where we the user can search on a street, the street need to match one of the streets in the Ladestandertable. 
# It will return information about all the chargers on that specifik street the user have entered.
def information_about_charger():
	hello5()
	Streetname = input("Insert Streetname: \n")

	mycursor = thisConn.cursor()

#this execute statment, goes in and select our desired information about the streetname our user have entered. 
#it takes all the data from the table "Ladestander" and make sure only print the information where the adress matches the user input
	mycursor.execute("SELECT Ladestander_ID, Adresse, Hus_nr, Parkeringszone, kW, Antal_Udtag, Pris_KWH FROM Ladestander WHERE Adresse = %s;", (Streetname,))
#the variable myrecords saves the result of the above SQL statement. 
	myrecords = mycursor.fetchall()

#We make use of beautifultable to create a more manageable list for the user
#we define table to beautifultable() which is a build in function for the library "beautifultable". It works like a normal list in python
#afterwards we create our desired Column headers for the table and makes a for loop to insert all the information the SQL statement gave us
#lastly we print our table so the user can see the result 
	table = BeautifulTable()
	table.columns.header = ["Ladestander ID", "Adresse", "Hus nr", "Parkeringszone", "kW", "Antal Udtag", "Pris pr.kWh"]
	for row in myrecords: 
		table.rows.append(row)
	print("\n")
	print(table) 

