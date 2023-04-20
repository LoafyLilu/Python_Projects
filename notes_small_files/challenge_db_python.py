#importing sqlite3, establishing temporary db & connection with :memory:
import sqlite3

conn = sqlite3.connect(":memory:")

rosterValues = (('Jean-Babtiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'knot', 'Mangalore', -5))

#telling the program what to do with the connection
#create a table named roster, but not inserting any data
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, IQ INT)")
    cur.executemany("INSERT INTO Roster VALUES(?, ?, ?)",
                  rosterValues)

#displaying all values in the table
    cur.execute("SELECT * FROM Roster")
    for row in cur.fetchall():
        print(row)

#updating species for Korben Daaa-laaaaaas
    cur.execute("UPDATE Roster SET Species = 'Human' WHERE Species = 'Meat Popsicle'")
#selecting
    cur.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
    for row in cur.fetchall():
        print(row)

    cur.close()




    
    
    

