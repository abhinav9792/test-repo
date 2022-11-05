import pandas as pd
import mysql.connector


pd_xl_file = pd.ExcelFile("Untitled spreadsheet.xlsx")
df = pd_xl_file.parse("Sheet1")
# data = pd.read_csv (r'pg - Sheet4.csv')   
df.head(4)

print(df.head(4))
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
#    database="pg1"
)

print(mydb)


mycursor = mydb.cursor()		
# Company Name	Work since	Holiday Name	Stay	No. of Person	Starting From (Trip)	Destination	By	 Hotel Name	Meal	Cab Facility	Price	Cancellation Charge	Cancellation Policy	image Link		 
mycursor.execute("USE Pg1")
print(" now using pg1 db")
# mycursor.execute("CREATE TABLE tour_travels (Company_Name VARCHAR(30),Work_since INT,Holiday_Name VARCHAR(30),Stay INT,No_of_Person INT,Starting_From_Trip VARCHAR(30),Destination VARCHAR(30),Bys VARCHAR(30),Hotel_Name VARCHAR(30),Meal VARCHAR(30),Cab_Facility VARCHAR(30), Price INT, Cancellation_Charge VARCHAR(30),Cancellation_Policy VARCHAR(30),image_Link VARCHAR(30))")


for i in range(len(df.index)):
    Company_Name =str(df.at[i,'Company Name'])
    Work_since=str(df.at[i,'Work since'])
    Holiday_Name=str(df.at[i,'Holiday Name'])
    Stay=str(df.at[i,'Stay'])
    No_of_Person=str(df.at[i,'No. of Person'])
    Starting_From_Trip=str(df.at[i,'Starting From (Trip)'])
    Destination=str(df.at[i,'Destination'])
    Bys=str(df.at[i,'By'])
    Hotel_Name=str(df.at[i,' Hotel Name'])
    Meal=str(df.at[i,'Meal'])
    Cab_Facility=str(df.at[i,'Cab Facility'])
    Price=str(df.at[i,'Price'])
    Cancellation_Charge=str(df.at[i,'Cancellation Charge'])
    Cancellation_Policy=str(df.at[i,'Cancellation Policy'])
    image_Link=str(df.at[i,'image Link'])
    
            
    
    sql = "INSERT INTO tour_travels (Company_Name,	Work_since,Holiday_Name,Stay,No_of_Person,Starting_From_Trip,Destination,Bys,Hotel_Name,Meal,Cab_Facility,Price,Cancellation_Charge,Cancellation_Policy,image_Link)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    val =(Company_Name,	Work_since,Holiday_Name	,Stay,No_of_Person,Starting_From_Trip,Destination,Bys,Hotel_Name,Meal,Cab_Facility,Price,Cancellation_Charge,Cancellation_Policy,image_Link)
   
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


# for value in sheet.iter_rows(min_row=1,max_row=1,min_col=1,max_col=1,values_only=True):    
#   print("----------")
#   print(value)

#   val = print(value)
#   mycursor.execute(sql, val)
#   mydb.commit()

