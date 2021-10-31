import pyodbc 
try:
    conn = pyodbc.connect('DRIVER={MySQL ODBC 5.1 Driver};SERVER=dataserver;DATABASE=as400;UID=root;PWD=dataserver;')
except pyodbc.Error as ex:
    sqlstate = ex.args[1]
    print(sqlstate) 
cursor = conn.cursor()
cursor.execute("SELECT * FROM as400.items WHERE ITNBR='AJASFG'")

columns = [column[0] for column in cursor.description]

print(columns)
results =[]
for row in cursor.fetchall():
    results.append(dict(zip(columns,row)))

print(results)
#rows = cursor.fetchall()
#for row in rows:
#    print(row.ITNBR, row.ITDSC, row.DRWING)
#for row in cursor:
#    print(row)
