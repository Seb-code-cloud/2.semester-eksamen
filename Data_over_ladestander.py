#PLUGDK Prototype
#Authors Sebastian, Andreas, Jakob, Jakob og Simon (Gruppe 1)
#Date: 2021-06/09
#Created for educational use

#Please see README.txt before initiating the program

import Databaseconnect as thisDatabase
from beautifultable import BeautifulTable


#connect to database
thisConn = thisDatabase.dbconnect()


def Coordinates_Operator(result):
	table = BeautifulTable()
	table.columns.header = ["Ladestander_ID", "Adresse", "Virksomheds_Navn", "virksomheds_Hjemmeside", "Longitude", "Latitude"]
	for row in result:
		table.rows.append(row)

	print(table)

sql = """SELECT 
  Ladestander.Ladestander_ID, Ladestander.Adresse, Operatør.Virksomheds_Navn, Operatør.Virksomheds_Hjemmeside, Ladestander.Longitude, Ladestander.Latitude 
  FROM Ladestander 
  JOIN Operatør ON Ladestander.Virksomheds_ID = Operatør.Virksomheds_ID"""


mycursor = thisConn.cursor()
mycursor.execute(sql)
myRecords = mycursor.fetchall()


