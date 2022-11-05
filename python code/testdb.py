import pandas as pd
import mysql.connector


pd_xl_file = pd.ExcelFile("merge 8.xlsx")
df = pd_xl_file.parse("Sheet1")
# data = pd.read_csv (r'pg - Sheet4.csv')   
# df = pd.DataFrame(data)

# print(df.head(4))
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
#    database="pg1"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("USE Pg1")
print(" now using pg1 db");

# # mycursor.execute("SHOW DATABASES")

# # for x in mycursor:
# #   print(x) 


# mycursor.execute("CREATE TABLE list2 (phone_number INT, company_name VARCHAR(20), company_rating INT, ddress VARCHAR(30), latitude INT, longitude INT, acity VARCHAR(20), mncity VARCHAR(20), related_keyword_key VARCHAR(20), category VARCHAR(20))")

for i in range(len(df.index)):
    phone_number =str(df.at[i,'phone_number'])
    company_name=str(df.at[i,'company_name'])
    company_rating=str(df.at[i,'company_rating'])
    ddress=str(df.at[i,'address'])
    latitude=str(df.at[i,'latitude'])
    longitude=str(df.at[i,'longitude'])
    acity=str(df.at[i,'acity'])
    mncity=str(df.at[i,'mncity'])
    related_keyword_key=str(df.at[i,'related_keyword_key'])
    category=str(df.at[i,'category'])
    
    sql = "INSERT INTO list2 (phone_number, company_name, company_rating, ddress, latitude, longitude,acity, mncity, related_keyword_key,category)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val =  (phone_number, company_name, company_rating, ddress, latitude, longitude,acity, mncity, related_keyword_key,category)
    mycursor.execute(sql,val)
    mydb.commit()


# for value in sheet.iter_rows(min_row=1,max_row=1,min_col=1,max_col=1,values_only=True):    
#   print("----------")
#   print(value)

#   val = print(value)
#   mycursor.execute(sql, val)
#   mydb.commit()

print(mycursor.rowcount, "record inserted.")

# to stop APACHE SERVER and star the the xampp
# sudo /opt/lampp/manager-linux-x64.run
# sudo service apache2 stop