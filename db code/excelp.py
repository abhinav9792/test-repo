# # from openpyxl import Workbook

# # workbook = Workbook()
# # sheet = workbook.active

# # sheet["A1"] = "hello"
# # sheet["B1"] = "world!"

# # workbook.save(filename="hello_world.xlsx")


# from openpyxl import load_workbook
# workbook = load_workbook(filename="merge 8.xlsx")
# workbook.sheetnames
# ['Sheet 1']

# sheet = workbook.active
# print(sheet)

# # # print(sheet.title)
# # # for i in range(1,20):
# # #     i = str(i)
# # #     print(sheet["C"+i].value)
# # print(sheet["A":"b"])

# for value in sheet.iter_rows(min_row=1,max_row=1,min_col=1,max_col=10,values_only=True):
#         print(value)

import pandas as pd

pd_xl_file = pd.ExcelFile("merge 8.xlsx")
df = pd_xl_file.parse("Sheet1")
# print(df)
# print(df["phone_number"])
# print(df["company_name"])
# print(df["address"])
# print(df["latitude"])
# print(df["longitude"])
# print(df["acity"])
# print(df["mncity"])
# print(df["related_keyword_key"])
# print(df["category"])

print(df.at[1,'phone_number'])
print(df.iloc[2]['phone_number'])


# dimensions = df.shape
# print(dimensions)
for i in range(len(df.index)):
    phone_number =df.at[i,'phone_number']
    company_name=df.at[i,'company_name']
    company_rating=df.at[i,'company_rating']
    ddress=df.at[i,'address']
    latitude=df.at[i,'latitude']
    longitude=df.at[i,'longitude']
    acity=df.at[i,'acity']
    mncity=df.at[i,'mncity']
    related_keyword_key=df.at[i,'related_keyword_key']
    category=df.at[i,'category']
    