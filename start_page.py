#PLUGDK Prototype
#Authors Sebastian, Andreas, Jakob, Jakob og Simon (Gruppe 1)
#Date: 2021-06/09
#Created for educational use

#Please see README.txt before initiating the program

#From XXXXX import * Is a import method where the Main file import all information 
from main_menu2 import *
from Create_user import *
from Data_over_ladestander import *
from Specifications_about_charger import *
#importing time, as it is used to make the program run more realistic
import time, sys


title1 = "\t\t\tLOGIN\t\t\t\n"

#Creating a function that will makes the program look smooth 
def hello1():
    print("\033[H\033[J") 
    print(title1)

#This function works as a authenticator to verify the user is created in the database 
def login():
	hello1()
	#global is a built in keyword in python we use to acces Email1, Password1 and Bruger_ID outside of this function
	global Email1
	global Password1
	global Bruger_ID
	#Here we ask the user to enter their password and email.
	Email1 = input("Insert your email: \t")
	Password1 = input("Insert your password: \t")

	mycursor = thisConn.cursor()
	#This line Runs an sql statement in MySQL workbench
	mycursor.execute('SELECT * from Bruger WHERE Email="%s" AND Adgangskode="%s"' % (Email1, Password1))
	#Here we use fetchone to get the information from the above MySQL statement and we put in a variable so we can call i later
	Bruger_ID = mycursor.fetchone()
	#We create a IF/ELSE Statement to check that the user have entered the correct Email and Pasword, if they have they will continue in the program, if not they will return
	if Bruger_ID is not None:
		print("Welcome")
		time.sleep(1)
		main_menu()
	else:
		print("Login failed")
		time.sleep(1.5)
		Start_page()


#------------------------------------------------------------------------------------------------------------------------------------------------

title2 = "\t\t\tPLUGDK\t\t\t\n"

def hello2():
    print("\033[H\033[J") 
    print(title2)


#this is the first menu the user will interact with and the different menu's works as a way to visualize the programs function/features to the user
def Start_page():
	hello2()
	options = [
		"Create new user",
		"Log in",
		"Continue without login",
		"Exit program"]
	print("Enter a number to select an option:\n")
	#in this for loop we use enumrate() we get both a counter and the value from the iterable
	for d, options in enumerate(options):
		print("[" + str(d + 1) + "] " + options)

	choice = int(input("Select an option [1] - [4]: "))

	#We create a IF/ELSE statment combined with the choices above to give the user some different options
	#This IF/ELSE statement depends on the users input, and will run the if statment that is equal the what the user have inserted
	if choice in range(1,5):
		if choice == 1:
			time.sleep(1)
			Create_new_user()
			time.sleep(1)
			Start_page()
			

		elif choice == 2:
			time.sleep(1)
			login()


		elif choice == 3:
			time.sleep(1)
			main_menu2()
			

		elif choice == 4:
			hello2()
			print("\n")
			print("Quitting.....")
			time.sleep(1.5)
			exit()
	else:
		print("I dont know this action..")
		time.sleep(2)
		main_menu()


#---------------------------------------------------------------------------------------------------------------------------------------------------

title = "\t\t\tMENU\t\t\t"

def hello():
    print("\033[H\033[J") 
    print(title)
    print("\n")


def main_menu():
	hello()
	options = [
		"Coordinates and information about operator",
		"Specifications of a charger",
		"Start Chargning",
		"Show personal consumption",
		"Exit Program\n"
		]
	print("Enter a number to select an option:\n")
	for d, options in enumerate(options):
		print("[" + str(d + 1) + "] " + options)

	choice = int(input("Select an option [1] - [5]: "))


	if choice in range(1,6):
		if choice == 1:
			time.sleep(1)
			Coordinates_Operator(myRecords)
			time.sleep(5)
			main_menu()
			

		elif choice == 2:
			time.sleep(1)
			information_about_charger()
			print("\n")
			time.sleep(4)
			main_menu()

		elif choice == 3:
			time.sleep(1)
			start_charging()
			time.sleep(5)
			main_menu()


		elif choice == 4:
			time.sleep(1)
			consumption(myRecords)
			time.sleep(5)
			main_menu()

		elif choice == 5:
			hello()
			print("\n")
			print("Quitting.....")
			time.sleep(1.5)
			exit()
	else:
		print("I dont know this action..")
		time.sleep(2)
		main_menu()

#-----------------------------------------------------------------------------------------------------------------------------------


def consumption(login):
	thisConn = thisDatabase.dbconnect()
	mycursor = thisConn.cursor()
	mycursor.execute('SELECT Forbrug_Kr, Energiforbrug_kWH from Bruger WHERE Email="%s" AND Adgangskode="%s"' % (Email1, Password1))

	myRecords = mycursor.fetchall()
	hello2()

	table = BeautifulTable()
	table.columns.header = ["Consumption in Kr", "Consumption in kWh"]
	for row in myRecords: 
		table.rows.append(row)
	print("\n")
	print(table) 
	thisConn.close()

#----------------------------------------------------------------------------------------------------------------------------------

#This function create a progress bar that visualize how long the the charging will take
def update_progress(progress):
    barLength = 40 
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

#---------------------------------------------------------------------------------------------------------------------------------

#In function update() we update the colomns pris, Ladestander_ID and kWh_Total in the table ordre when the user is charging his/her car.
def update():
    hello2()
    global CS_ID
    hello2()
    CS_ID = int(input("Insert desired charging stations ID: \n"))


    #connect to database
    thisConn = thisDatabase.dbconnect()

    mycursor = thisConn.cursor()

    #We make sure that the user inputs a valid Ladestander_ID with this IF/else statment
    if CS_ID <= 430:
        hello2()
        print("")
        print("progress for charging your EV car : 0->100%\n")
        #this for loop is used with the above function update_progress()
        for i in range(101):
            time.sleep(0.1)
            update_progress(i/100.0)
        print("")
        print("Chargning done please pick up your car")

        
        #Here we insert the values that match the user input into Ordre, so the table gets updated in MySQL
        mycursor.execute('INSERT INTO Ordre (Pris, Ladestander_ID, KWH_Total) SELECT (Pris_KWH*40), Ladestander_ID, (KW*40) FROM Ladestander WHERE Ladestander_ID="%s"' % (CS_ID))
        #ThisConn.commmit() is commiting the changes we just have made to the database
        thisConn.commit()

        update_User_ID()
        update_price()
        
        mycursor.execute('SELECT Pris, kWH_Total FROM Ordre ORDER BY Tidspunkt DESC LIMIT 1')

        Price = mycursor.fetchall()
    
        table = BeautifulTable()
        table.columns.header = ["Price for charging", "kWH for this charge"]
        for row in Price: 
            table.rows.append(row)
            hello2()
            print("\n")
            print(table)
            time.sleep(3) 


        time.sleep(1)
        main_menu()
        thisConn.close()

    else:
        hello2()
        print("dont know this charger ID, try another:       (HINT: Try something between 1-430")
        time.sleep(1)
        update()

#----------------------------------------------------------------------------------------------------------------------------------


def start_charging():
     #connect to database
    thisConn = thisDatabase.dbconnect()
    mycursor = thisConn.cursor()
    hello2()

    Email2 = input("To start the chargning you need to verify you Email:  \n")
    hello2()
    Password2 = input("To start the chargning you need to verify your password:  \n")

    #here we verify the user again, to make sure they want to start the charging
    global Bruger_ID2
    mycursor.execute('SELECT Bruger_ID from Bruger WHERE Email="%s" AND Adgangskode="%s"' % (Email2, Password2))
    Bruger_ID2 = mycursor.fetchone()

    if Bruger_ID2 is not None:
        update()
        time.sleep(1)
    else:
        print("Login failed")
        time.sleep(1.5)
        main_menu()


#----------------------------------------------------------------------------------------------------------------------------------

def update_User_ID():
    thisConn = thisDatabase.dbconnect()
    mycursor = thisConn.cursor()

    sql = "UPDATE Ordre SET Bruger_ID = %s order by Tidspunkt desc limit 1"
    #bruger_ID2 comes from start_charging function where we verify the user
    val = (Bruger_ID2)

    mycursor.execute(sql, val)

    thisConn.commit()
    thisConn.close()

#----------------------------------------------------------------------------------------------------------------------------------

#this function update the Total consumption in DKK and the total consumption in kWh

def update_price():
	thisConn = thisDatabase.dbconnect()
	mycursor = thisConn.cursor()

	#MySQL does not accept to use Update and Orderby in same querie, thats why we have made a subquerie to make sure it gets order by.
	#furthermore we have used join to get access to different values in different tables and to insert the values in one table.


	sql = """UPDATE Bruger as B
	JOIN (SELECT O.Bruger_ID 
	FROM Ordre as O
	JOIN Bruger as B 
	ON O.Bruger_ID=B.Bruger_ID 
	ORDER BY O.Tidspunkt DESC LIMIT 1
	) AS BB
	ON B.Bruger_ID= BB.Bruger_ID
	join ordre as K on b.bruger_id = K.Bruger_Id
	SET B.Forbrug_kr = (B.Forbrug_Kr + K.Pris), B.Energiforbrug_kWH = (B.Energiforbrug_kWH + k.KWH_Total)"""


	mycursor.execute(sql)

	thisConn.commit()
	thisConn.close()


Start_page()
