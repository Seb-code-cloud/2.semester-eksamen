#Statement <Create database Ladestander_database;> Her oprettes en database med navnet Ladestander_database.
CREATE DATABASE Ladestander_database;

#Statement <Use Ladestander_database;> Dette statement gør det muligt at opperere i databasen og oprette tabeller.
USE Ladestander_database;

#Statement <CREATE TABLE `Bruger`> opretter tabellen bruger
#I paratesen tilføjes attributter/kolonner
# <VARCHAR(55)> er en datatype som betyder at det er muligt at skrive 55 tegn i hver række under den kolonne
# <INT> betyder at kolonnens rækker udelukkende indeholder tal
# Statement <PRIMARY KEY (`Bruger_ID`> betyder at vi ønsker at gøre kolonnen "Bruger_ID" til den primære nøgle i tabellen
CREATE TABLE `Bruger` (
  `Bruger_ID` INT NOT NULL AUTO_INCREMENT,
  `Navn` VARCHAR(55),
  `Efternavn` VARCHAR(55),
  `Email` VARCHAR(55) UNIQUE,
  `Land` VARCHAR(55),
  `Postnummer` INT,
  `Adgangskode` VARCHAR(55),
  `Forbrug_Kr` INT DEFAULT 0,
  `Energiforbrug_kWH` INT DEFAULT 0,
  PRIMARY KEY (`Bruger_ID`)
);


#Her er gentagelses af statements fra foreige tabel, hvorfor de ikke kommenteres igen.
#Datatypen TIMESTAMP definerer et konkret tidspunkt 'YYYY-MM-DD HH:MM:SS' 
#DEFAULT Gør den automatisk har en default, med mindre andet bliver fortalt til den. Vores default, er det nøjagtige tidpunkt den bliver oprettet
#Statement <KEY `PK, FK` (`Bruger_ID`, `Ladestander_ID`)> betyder at tabellen Bruger_ID og Ladestander_ID 
# gøres til bådde primær nøgle og sekundær nøgle
CREATE TABLE `Ordre` (
  `Bruger_ID` INT,
  `Ladestander_ID` INT,
  `Pris` INT,
  `kWH_Total` INT,
  `Tidspunkt` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  KEY `PK, FK` (`Bruger_ID`, `Ladestander_ID`)
);

# Datatypen FLOAT minder om INT: Det er udelukkende tal, men decimaler kan også tilføjes.
# NOT NULL, betyder blot at feltet ikke må være tomt.
CREATE TABLE `Ladestander` (
  `Ladestander_ID` INT NOT NULL,
  `Virksomheds_ID` INT(55),
  `Longitude` VARCHAR(55) NOT NUlL,
  `Latitude` VARCHAR(55) NOT NULL,
  `Adresse` VARCHAR(55),
  `Hus_nr` VARCHAR(55),
  `Parkeringszone` VARCHAR(55),
  `kW` INT,
  `Antal_Udtag` INT,
  `Pris_KWH` FLOAT,
  PRIMARY KEY (`Ladestander_ID`)
);

CREATE TABLE `Operatør` (
  `Virksomheds_ID` INT NOT NULL,
  `Virksomheds_Navn` VARCHAR(55),
  `Virksomheds_Tlf` INT,
  `Virksomheds_Mail` VARCHAR(55),
  `Virksomheds_Hjemmeside` VARCHAR(55),
  PRIMARY KEY (`Virksomheds_ID`)
);
