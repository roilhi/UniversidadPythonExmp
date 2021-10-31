# In this script, we read a query for a bunch of part numbers. 
import pandas as pd
import pyodbc  

#Connecting with Database
try:
    conn = pyodbc.connect('DRIVER={MySQL ODBC 5.1 Driver};SERVER=dataserver;DATABASE=as400;UID=root;PWD=dataserver;')
    print("Succesfully Connected! AS400\n")
except pyodbc.Error as ex:
    sqlstate = ex.args[1]
    print(sqlstate)

print('Please write a CSV file where the desired serial numbers to search are located in the first column. \n')
myPath = input('Then, please type the path where the CSV is located:\n ')

myDatabase = input('Please type the database name:\n ')

myTable = input('Please type table name:\n ')


dfGeneral = pd.read_csv(myPath)



#cursor = conn.cursor()
#cursor.execute("SELECT * FROM as400.items WHERE ITNBR='AJASFG'")