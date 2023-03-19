#importing sqlite3
import sqlite3

#creating a variable to serve as the connection token, and creating db
conn = sqlite3.connect('assignment.db')


#with the active connection, creating an empty table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fileName TEXT \
    )")
    conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect('assignment.db')
#tuple to be queried
fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

cur = conn.cursor()

#iterates through the tuple, and enters 
for i in fileList:
        if i.endswith('.txt'):
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files (col_fileName) VALUES (?)", (i,))
                print(i)
conn.close
        
    

