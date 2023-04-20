
#SQLite Assignment Pt1
#importing sqlite3, creating var for connection, creating first table
import sqlite3
connection = sqlite3.connect("C:/Users/Charissa/Documents/GitHub/Python_Projects/test_database.db")

c = connection.cursor()

c.execute("CREATE TABLE IF NOT EXISTS People(FirstName TEXT, LastName TEXT, Age INT)")

#Pt2
# inserting values into People table
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()

#creating a temporary one time db to test code or table structures SUPER USEFUL
connection = sqlite3.connect(':memory:')

#deleting a table
c.execute("DROP TABLE IF EXISTS People")

#Pt3
#make sure to close the connection
connection.close()

#db connection can be used with with to simplify code and auto commit, and close all files opened in connection
with sqlite3.connect("test_database.db") as connection:
    #perform any SQL operations using connection here
    #still need to commit() change to see immediately before closing

#pt4
#running more than one line of code at a time can use executescript() method - can use for multi line strings

import sqlite3
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT):
                    INSERT INTO People VALUES('Ron', 'Obvious', '42'):
                    """)

#can also use executemany() method by using tuple
peoplesValues = (('Luigi', 'Varcotti', 43), ('Arthur', 'Belling', 28))

#can insert all lines at once - ?'s as placeholders for inserted values
c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)

#Pt5
#changing data type to avoid sql injections - turning age into integer to validate, then back to string
import sqlite3

#get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

#execute insert statement for supplied personal data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.execute(line)

#pt6
#dealing with potentional breaks from names - apostrophies - using placegikders and inserting as tuple

import sqlite3

#get personal data from user and insert into a tuple
#get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

#execute insert statement for supplied personal data
with sqlite3.connect('test_database.dv') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)
 
#can also update the content by using sql update statement
c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
          (45, 'Luigi', 'Vercotti'))

#pt7
#retreiving date, through fetchall() or fetchone()

import sqlite3
peoplesValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_databaste.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execite("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)",
                  peoplesValues)

# select all first and last names from people over age 30
    c.execute("SELECT FirstName, LastName, FROM People WHERE Age > 30")
    for row in c.fetchall():
        print(row)

#pt8
# looping over result rows one at a time
c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
while True:
    row = c.fetchone()
    if row is None:
        break
    print(row)
