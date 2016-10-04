# Python:  2.7.11
#
# Author:  Michael Harrison
#
# Iteration: 1.1
#
# Purpose: The Tech Academy - Python Course, Step 38 of 64, "Databases and Python"
#          Purpose of exercise is to establish understanding of how to communicate with
#          SQLite

## ESTABLISHING CONNECTION TO SQLITE AND CREATING TABLE

import sqlite3

with sqlite3.connect('test_database.db') as connection:

    c=connection.cursor()

    c.executescript("""

    DROP TABLE IF EXISTS People;

    CREATE TABLE People (FirstName TEXT, LastName TEXT, Age INT);

    INSERT INTO People Values('Ron','Obvious','42');

    """)



## USING TUPLE OF VALUES AND RUNNING EXECUTE MANY STATEMENT TO INSERT VALUES INTO TABLE

peopleValues = (

    ('Ron','Obvious',42),
    ('Luigi','Vercotti',43),
    ('Arthur','Belling',28)
    )

import sqlite3

with sqlite3.connect('test_database.db') as connection:

    c=connection.cursor()

    c.executemany("INSERT INTO People VALUES(?,?,?)",peopleValues)



## INSERTING VALUES INTO TABLE USING USER SUPPLIED INFORMATION

import sqlite3

firstName=raw_input("Enter your first name: ")

lastName=raw_input("Enter your last name: ")

age=int(raw_input("Enter your age: "))

with sqlite3.connect('test_database.db') as connection:

    c = connection.cursor()

    line="INSERT INTO People Values('"+ firstName + "','"+lastName+"',"+str(age)+")"

    c.execute(line)



## USING PLACEHOLDER AND INSERTING DATA AS TUPLE

import sqlite3

#get person data from user and insert into a tuple

firstName=raw_input("Enter your first name: ")

lastName=raw_input("Enter your last name: ")

age=int(raw_input("Enter your age: "))

personData=(firstName,lastName,age)

#execute insert Statement for supplied person data

with sqlite3.connect('test_database.db') as connection:

    c=connection.cursor()

    c.execute("INSERT INTO People VALUES(?,?,?)",personData)




## UPDATING CONTENT BY USING SQL UPDATE STATEMENT

import sqlite3

with sqlite3.connect('test_database.db') as connection:

    c=connection.cursor()

    c.execute("UPDATE People SET age=? WHERE FirstName=? AND LastName=?",

          (45,'Luigi','Vercotti'))


## INSERTING NAMES INTO TABLE AND RETRIEVING INFORMATION

import sqlite3

peopleValues = (

    ('Ron','Obvious',42),
    ('Luigi','Vercotti',43),
    ('Arthur','Belling',28)
    )

with sqlite3.connect('test_database.db') as connection:

    c=connection.cursor()

    c.execute("DROP TABLE IF EXISTS People")

    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

    c.executemany("INSERT INTO People VALUES(?,?,?)",peopleValues)

    #select all first and last names form people over age 30

    c.execute("SELECT FirstName,LastName,Age FROM People WHERE Age>30")

    for row in c.fetchall():

        print row


##USING WHILE LOOP TO PROCESS SQL QUERY

import sqlite3

peopleValues = (

    ('Ron','Obvious',42),
    ('Luigi','Vercotti',43),
    ('Arthur','Belling',28)
    )

with sqlite3.connect('test_database.db') as connection:

    c=connection.cursor()

    c.execute("DROP TABLE IF EXISTS People")

    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

    c.executemany("INSERT INTO People VALUES(?,?,?)",peopleValues)

    #select all first and last names form people over age 30

    c.execute("SELECT FirstName,LastName,Age FROM People WHERE Age>30")

    while True:

        row=c.fetchone()

    if row is None:

    break 

    print row

        

## DRILL
## Step 1 - Create database in RAM named Roster w/ fields Name, Species, and IQ
## Step 2 - Populate table with values 
## Step 3 - Update Species of Korben Dallas to Human
## Step 4 - Display names and IQs of everyone in table classified as Human


###Step 2

import sqlite3

rosterValues = (

    ('Jean-Baptiste Zord','Human',122),
    ('Korben Dallas','Meat Popsicle',100),
    ('Ak\'not','Mangalore',-5)
    )

###Step 1
   
with sqlite3.connect(':memory:') as connection:

     c=connection.cursor()

     c.execute("DROP TABLE IF EXISTS Roster")

     c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")

     c.executemany("INSERT INTO Roster VALUES(?,?,?)",rosterValues)
    
###Step 3
     c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",

          ('Human','Korben Dallas','100'))

     c.execute("SELECT Name,IQ FROM Roster WHERE Species = 'Human'")

     for row in c.fetchall():

         print row

