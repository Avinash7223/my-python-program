import sqlite3

conn = sqlite3.connect('student_info.db')
conn.execute('''CREATE TABLE DETAILS4
         (ROLLNO INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         GENDER            TEXT     NOT NULL,
         GRADE        TEXT);''')

print("Table created successfully");

conn.execute("INSERT INTO DETAILS4(ROLLNO,NAME,GENDER,GRADE) \
      VALUES (1,'p.avinash','male','A')")
conn.execute("INSERT INTO DETAILS4 (ROLLNO,NAME,GENDER,GRADE) \
      VALUES (2,'n.lokesh','male','O')")
conn.execute("INSERT INTO DETAILS4 (ROLLNO,NAME,GENDER,GRADE) \
      VALUES (3,'komal rani','female','A')")
conn.execute("INSERT INTO DETAILS4 (ROLLNO,NAME,GENDER,GRADE) \
      VALUES (4,'k.vishal venkat','male','B')")

print("Inserting the data in table is done")

coursor=conn.execute("SELECT ROLLNO,NAME,GENDER,GRADE from DETAILS4")

for row in coursor:
  print("ROLLNO=",row[0])
  print("NAME=",row[1])
  print("GENDER=",row[2])
  print("GRADE=",row[3],"\n")
print("selecting data is done")

conn.execute("UPDATE DETAILS4 set GRADE='A' where ROLLNO= 4")
conn.commit()
print("updating is done")

conn.execute("DELETE from DETAILS4 where ROLLNO= 3")
conn.commit()
print("deleting is done")

coursor=conn.execute("SELECT ROLLNO,NAME,GENDER,GRADE from DETAILS4")

for row in coursor:
  print("ROLLNO=",row[0])
  print("NAME=",row[1])
  print("GENDER=",row[2])
  print("GRADE=",row[3],"\n")



    
    

