import pandas as pd
import mysql.connector


pd_xl_file = pd.ExcelFile("interior design.xlsx")
# i had changed the sheet name in the next line 
# by default it is sheet 1 but since i had renamed my sheet to interior design that why i had to change it
df = pd_xl_file.parse("Interior Designers")
df.head(4)

print(df.head(4))
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
#    database="pg1"
)

print(mydb)


mycursor = mydb.cursor()		
		 
mycursor.execute("USE Pg1")
print(" now using pg1 db")
#uncomment the next line to create a table automatically
mycursor.execute("CREATE TABLE interior_design(Types_of_Products Varchar(50),Sub_Product varchar(50))")
# items in the sheet
# Types of Products	
# Sub Product																								

for i in range(len(df.index)):
    Types_of_Products=str(df.at[i,'Types of Products'])
    Sub_Product	=str(df.at[i,'Sub Product'])
    
    sql = "INSERT INTO interior_design(Types_of_Products,Sub_Product)VALUES (%s,%s)"

    val =(Types_of_Products,Sub_Product)
   
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")



