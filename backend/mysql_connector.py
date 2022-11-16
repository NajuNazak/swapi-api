from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='mysql',
                                 host='localhost',
                                 database='db')
cursor = cnx.cursor()
