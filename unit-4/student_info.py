import sqlite3

conn = sqlite3.connect('student_info.db')

conn.execute('''CREATE TABLE STUDENT1
         (ROLLNUMBER CHAR(15) PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         GENDER            TEXT     NOT NULL,
         GRADE        INT        NOT NULL);''')

print("Table created successfully");

st=int(input("enter the number students:"))

roll=[1,2,3,4,5,6]
nme=['a','b','c','d','e','g']
gnde=['m','m','f','m','f','f']
gra=[8,2,7,6,5,9]
for x in range(st):
    conn.execute("INSERT INTO STUDENT (ROLLNUMBER,NAME,GENDER,GRADE) \
      VALUES (roll[x],nme[x],gnde[x],gra[x])")
    
    

