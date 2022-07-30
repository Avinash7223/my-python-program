'''1.	Execute and display the output screens with code on CRUD operations (Create, Read, Update, and Delete) to manage data stored in a Student database'''

#   P.Avinash--VU21CSEN0101554
#   Komal Rani--VU21CSEN0100389
#   N.Lokesh Reddy--VU21CSEN0100088
#   K.Vishal Venkat--VU21CSEN0100142

import sqlite3

conn = sqlite3.connect('student_database.db')
print("Opened database successfully")

#creating a table

conn.execute('''CREATE TABLE STUDENT_INFO
         (REGD_NO   TEXT   NOT NULL,
         NAME           TEXT    NOT NULL,
         GMAIL          CHAR(20)     NOT NULL,
         GENDER        CHAR(10)  NOT NULL,
         MOBILE      INT       NOT NULL,
         ENGLISH       INT      NOT NULL,
         PYTHON       INT       NOT NULL,
         CLAD       INT       NOT NULL,
         MATHS_P1   INT     NOT NULL,
         MATHS_P2   INT    NOT NULL,
         BEEE      INT    NOT NULL,
         WORKSHOP    INT   NOT NULL,
         EVPR     INT     NOT NULL);''')
print("Table created successfully")

#adding the information to the table

conn.execute("INSERT INTO STUDENT_INFO (REGD_NO,NAME,GMAIL,GENDER,MOBILE,ENGLISH,PYTHON,CLAD,MATHS_P1,MATHS_P2,BEEE,WORKSHOP,EVPR)\
      VALUES ('VU21CSEN0101554', 'P.AVINASH', 'apuram@gitam.in', 'MALE', 8008191065, 97, 89, 86, 85, 84, 79, 82, 78 )")
conn.execute("INSERT INTO STUDENT_INFO (REGD_NO,NAME,GMAIL,GENDER,MOBILE,ENGLISH,PYTHON,CLAD,MATHS_P1,MATHS_P2,BEEE,WORKSHOP,EVPR)\
      VALUES ('VU21CSEN0100088', 'N.LOKESH REDDY', 'lnalla@gitam.in', 'MALE', 7672035301, 95, 85, 83, 82, 89, 74, 81, 75 )")
conn.execute("INSERT INTO STUDENT_INFO (REGD_NO,NAME,GMAIL,GENDER,MOBILE,ENGLISH,PYTHON,CLAD,MATHS_P1,MATHS_P2,BEEE,WORKSHOP,EVPR)\
      VALUES ('VU21CSEN0100142', 'K.VISHAL VENKAT', 'vvenkat@gitam.in', 'MALE', 7337240835, 77, 88, 83, 65, 84, 75, 83, 72 )")
conn.execute("INSERT INTO STUDENT_INFO (REGD_NO,NAME,GMAIL,GENDER,MOBILE,ENGLISH,PYTHON,CLAD,MATHS_P1,MATHS_P2,BEEE,WORKSHOP,EVPR)\
      VALUES ('VU21CSEN0100389', 'KOMAL RANI', 'krani@gitam.in', 'FEMALE', 7869462848, 96, 79, 88, 87, 81, 89, 87, 88 )")
conn.execute("INSERT INTO STUDENT_INFO (REGD_NO,NAME,GMAIL,GENDER,MOBILE,ENGLISH,PYTHON,CLAD,MATHS_P1,MATHS_P2,BEEE,WORKSHOP,EVPR)\
      VALUES ('VU21CSEN0101231','B. AMRUTHY REDDY', 'abokka@gitam.in', 'MALE',7416250479, 69, 73, 87, 96, 57, 89, 69, 69)")
conn.execute("INSERT INTO STUDENT_INFO (REGD_NO,NAME,GMAIL,GENDER,MOBILE,ENGLISH,PYTHON,CLAD,MATHS_P1,MATHS_P2,BEEE,WORKSHOP,EVPR)\
      VALUES ('VU21CSEN0101343','J.MANI KRISHNA', 'jmani@gitam.in' , 'MALE', 9063073982, 68, 74, 77, 93, 57, 88, 79, 89)")
conn.execute("INSERT INTO STUDENT_INFO (REGD_NO,NAME,GMAIL,GENDER,MOBILE,ENGLISH,PYTHON,CLAD,MATHS_P1,MATHS_P2,BEEE,WORKSHOP,EVPR)\
      VALUES ('VU21CSEN0101608','T SAI NARAYANA MURTHY', 'storati2@gitam.in', 'MALE', 7386009112, 59, 83, 86, 96, 55, 80, 62, 69)")
conn.execute("INSERT INTO STUDENT_INFO (REGD_NO,NAME,GMAIL,GENDER,MOBILE,ENGLISH,PYTHON,CLAD,MATHS_P1,MATHS_P2,BEEE,WORKSHOP,EVPR)\
      VALUES ('VU21CSEN010341','GUNDA VAMSHI', 'vgunda@gitam.in', 'MALE', 8317609597, 79, 82, 85, 86, 75, 81, 72, 89)")

conn.commit()
print("Records created successfully")

#reading the table

cursor = conn.execute("SELECT REGD_NO, NAME, GMAIL, GENDER, MOBILE, ENGLISH, PYTHON,CLAD,MATHS_P1,MATHS_P2,BEEE,WORKSHOP,EVPR from STUDENT_INFO")

for row in cursor:
    print("RERD_NO = ", row[0])
    print("NAME = ", row[1])
    print("GMAIL = ", row[2])
    print("GENDER = ", row[3])
    print("MOBILE = ", row[4])
    print("ENGLISH = ", row[5])
    print("PYTHON = ", row[6])
    print("CLAD = ", row[7])
    print("MATHS_P1 = ", row[8])
    print("MATHS_P2 = ", row[9])
    print("BEEE = ", row[10])
    print("WORKSHOP = ", row[11])
    print("EVPR= ", row[12], "\n")

print("reading done successfully")

#updating the table

conn.execute("UPDATE STUDENT_INFO set MOBILE = 8897953377 where REGD_NO = 'VU21CSEN0101554'")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)
conn.execute("UPDATE STUDENT_INFO set GMAIL = 'komalrani@gitam.in' where REGD_NO = 'VU21CSEN0100389'")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)
conn.execute("UPDATE STUDENT_INFO set MATHS_P1 = 56 where REGD_NO = 'VU21CSEN0100142'")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)
conn.execute("UPDATE STUDENT_INFO set MATHS_P2 = 59 where REGD_NO = 'VU21CSEN0100341'")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)
conn.execute("UPDATE STUDENT_INFO set ENGLISH = 86 where REGD_NO = 'VU21CSEN0101343'")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)

print("updating done successfully")

#deleting the table information

conn.execute("DELETE from STUDENT_INFO where REGD_NO = 'VU21CSEN0101608'")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)

print("deleting done successfully")

#printing the overall output
cursor = conn.execute("SELECT REGD_NO, NAME, GMAIL, GENDER, MOBILE, ENGLISH, PYTHON,CLAD,MATHS_P1,MATHS_P2,BEEE,WORKSHOP,EVPR from STUDENT_INFO")

for row in cursor:
    print("RERD_NO = ", row[0])
    print("NAME = ", row[1])
    print("GMAIL = ", row[2])
    print("GENDER = ", row[3])
    print("MOBILE = ", row[4])
    print("ENGLISH = ", row[5])
    print("PYTHON = ", row[6])
    print("CLAD = ", row[7])
    print("MATHS_P1 = ", row[8])
    print("MATHS_P2 = ", row[9])
    print("BEEE = ", row[10])
    print("WORKSHOP = ", row[11])
    print("EVPR= ", row[12], "\n")

conn.close()

print("P.Avinash--VU21CSEN0101554,\n Komal Rani--VU21CSEN0100389,\n N.Lokesh Reddy--VU21CSEN0100088,\n K.Vishal Venkat--VU21CSEN0100142")

