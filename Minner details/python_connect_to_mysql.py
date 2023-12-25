import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='SHpatel@9893',database='minner')
my_cursor=conn.cursor()

conn.commit()
conn.close()

print("connection created!")