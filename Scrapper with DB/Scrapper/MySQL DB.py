import mysql.connector
import mysql

try:
    connection = mysql.connector.connect(user='root',
                                         database='Ozone_Product_Data',
                                         host= 'localhost',
                                         password='')

    cursor = connection.cursor()
    print('Connection Successful')

except mysql.connector.Error as error:
    print('Failure')





