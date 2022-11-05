import requests
from bs4 import BeautifulSoup

#adding url of the page of whom to scrap data
url = "https://www.flipkart.com/zuari-monaco-engineered-wood-tv-entertainment-unit/p/itmafe1f309955bd?pid=TVUFSCCE6H9MYSKP&lid=LSTTVUFSCCE6H9MYSKPASM7NF&marketplace=FLIPKART&q=Zuari+Furniture&store=wwe&srno=s_1_13&otracker=search&otracker1=search&fm=Search&iid=71e7bc1e-7a82-426d-b57e-095b91fc160e.TVUFSCCE6H9MYSKP.SEARCH&ppt=sp&ppn=sp&ssid=jfo8d04dao0000001649073572176&qH=4bf732defd0ee7b6"
#url = "https://www.flipkart.com/canon-eos-1500d-dslr-camera-body-18-55-mm-ii-lens/p/itm033175ceb4ddd?pid=DLLFAEWE22ZAERXG&lid=LSTDLLFAEWE22ZAERXGWBJCOR&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=hp_omu_Best%2Bof%2BElectronics_6_10.dealCard.OMU_RXN53TXGM0FD_5&otracker1=hp_omu_WHITELISTED_neon%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_6_NA_view-all_5&fm=neon%2Fmerchandising&iid=6adc2153-d9e4-4b46-b5ab-b1bd896d28c5.DLLFAEWE22ZAERXG.SEARCH&ppt=hp&ppn=homepage&ssid=9xylne3u800000001646928923281"
scrap = requests.get(url).text
soup = BeautifulSoup(scrap,"lxml")

# getting product name
product_name=soup.find("span",class_="B_NuCI")
print("======name of the product =======")
print(product_name.text,"\n")

#reivew and ratings 
product_rating_review=soup.find("span",class_="_2_R_DZ")
print("==========total number of rating and recviews of the product are ----->>>>")
print(product_rating_review .text,"\n")

#star ratings on the product
product_star=soup.find("div",class_="_3LWZlK")
print("======star rating of the product are ----->>>>")
print(product_star.text,"\n")

#prce of the product
product_price=soup.find("div",class_="_30jeq3 _16Jk6d")
print("=========price of the product are =====>>>>")
print(product_price.text,"\n")


#pdescription of the product
product_desc=soup.find("div",class_="_1mXcCf RmoJUa")
print("======description of the product are =====>>>>")
print(product_desc.text,"\n")


# #prce of the product
# product_img=soup.find("img",class_="_396cs4 _2amPTt _3qGmMb  _3exPp9")
# a=product_img.src
# print("dimage link  of the product here=====>>>>")
# print(a)

# image link
# https://rukminim2.flixcart.com/image/416/416/kk01pjk0/dslr-camera/f/v/o/eos-1500d-canon-original-imafzfugydh2mjgf.jpeg?q=70


#scrapping comments and customer review
customer_rating=soup.find("div",class_="_3LWZlK _1BLPMq")
print("======rating of the customer on the product=====>>>>")
print(customer_rating.text,"\n")

#comments of the customer
customer_comment=soup.find("div",class_="t-ZTKy")
print("=====comment on the customer on the product=====>>>>")
print(customer_comment.text,"\n")

#link of the image
product_image_link=soup.find("div",class_="CXW8mj _3nMexc")
print("=====link of the image of the product=====>>>>")
print(product_image_link.img["src"],"\n")

#multiple comments
customer_comment_m=soup.find_all("div",class_="t-ZTKy")
print("=====comment on the customer on the product=====>>>>")
for i in customer_comment_m:
    print(i.text,"\n")