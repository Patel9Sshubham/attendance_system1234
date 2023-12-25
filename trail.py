# Python program to connect
# to mysql database
import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='SHpatel@9893',database='face_recognizer')
my_cursor=conn.cursor()

conn.commit()
conn.close()
print("connect successfully")
