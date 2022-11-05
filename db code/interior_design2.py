import pandas as pd
import mysql.connector


pd_xl_file = pd.ExcelFile("Interior Designing9.xlsx")
# i had changed the sheet name in the next line 
# by default it is sheet 1 but since i had renamed my sheet to interior design that why i had to change it
df = pd_xl_file.parse("Sheet2")
df.head(4)

print(df.head(4))
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
#    database="pg1"
)

print(mydb)

mycursor = mydb.cursor()		
		# S. No. 	Design Style	Main Materials	Colour Palette	Furniture Style	Distinguishing Features	Image 	Image 2	Image 3	Image 4	Image 5	Image 6
 
mycursor.execute("USE Pg1")
print(" now using pg1 db")
#uncomment the next line to create a table automatically
# mycursor.execute("CREATE TABLE interior_design2(SNo INT,Design_Style VARCHAR(50),Main_Materials VARCHAR(100),Colour_Palette VARCHAR(100),Furniture_Style VARCHAR(100),Distinguishing_Features VARCHAR(100),Image VARCHAR(300),Image_2 VARCHAR(300),Image_3 VARCHAR(300),Image_4 VARCHAR(300),Image_5 VARCHAR(300),	Image_6 VARCHAR(300))")
print("table created")


# items in the sheet
# Types of Products	
# Sub Product																								

for i in range(1,len(df.index)):
    SNo=str(df.at[i,'Sno'])
    Design_Style=str(df.at[i,'Design Style'])
    Main_Materials =str(df.at[i,'Main Materials'])
    Colour_Palette=str(df.at[i,'Colour Palette'])
    Furniture_Style=str(df.at[i,'Furniture Style'])
    Distinguishing_Features=str(df.at[i,'Distinguishing Features'])
    Image=str(df.at[i,'Image ']) 
    Image_2=str(df.at[i,'Image 2'])
    Image_3=str(df.at[i,'Image 3'])
    Image_4=str(df.at[i,'Image 4'])
    Image_5=str(df.at[i,'Image 5'])
    Image_6=str(df.at[i,'Image 6'])
    
    sql = "INSERT INTO interior_design2(SNo,Design_Style,Main_Materials,Colour_Palette ,Furniture_Style,Distinguishing_Features,Image,Image_2 ,Image_3,Image_4,Image_5,	Image_6)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    val =(SNo,Design_Style,Main_Materials,Colour_Palette,Furniture_Style,Distinguishing_Features,Image,Image_2,Image_3,Image_4,Image_5,Image_6)
   
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")



