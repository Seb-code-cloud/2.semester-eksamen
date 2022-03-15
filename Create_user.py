#PLUGDK Prototype
#Authors Sebastian, Andreas, Jakob, Jakob og Simon (Gruppe 1)
#Date: 2021-06/09
#Created for educational use

#Please see README.txt before initiating the program


import Databaseconnect as thisDatabase

#connect to database
thisConn = thisDatabase.dbconnect()

title4 = "\t\t\tCREATE NEW USER\t\t\t\n"

def hello4():
    print("\033[H\033[J") 
    print(title4)


def Create_new_user():
	hello4()
	First_name = input("Insert First name: \n")
	hello4()
	Last_name = input("Insert Last name: \n")
	hello4()
	Email = input("Insert Email: \n")
	hello4()
	Country = input("Insert Country: \n")
	hello4()
	Zip_code = input("Insert Zip Code \n")
	hello4()
	Password = input("Insert password: \n")
	
	
	sql = "INSERT INTO Bruger(Navn, Efternavn, Email, Land, Postnummer, Adgangskode) VALUES (%s,%s,%s,%s,%s,%s)"
	val = (First_name, Last_name, Email, Country, Zip_code, Password)

	mycursor = thisConn.cursor()
	mycursor.execute(sql, val)
	thisConn.commit()
	print("User succesfully created")
	thisConn.close()

