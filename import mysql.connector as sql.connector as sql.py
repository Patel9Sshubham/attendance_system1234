import mysql.connector as sql
connection = sql.connect(
  host="localhost",
  user="root",
  password="12345",
  database="student"
)
print(connection)


cursor = connection.cursor()
cursor.execute("CREATE table employeeinfo (id int auto_increment
                                 primary key, name varchar(255),
                                      department varchar(255))")