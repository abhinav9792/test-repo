from bs4 import BeautifulSoup
import requests



end_url = "Delhi/Brick-Dealers/nct-10057401"
base_url = "https://www.justdial.com/"

main_url = base_url + end_url
web= requests.get(main_url ,headers={'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}).text
soup = BeautifulSoup(web,"lxml")

# a = soup.find("span",class_ ="jcn")
# name extraction
a = soup.find("span",class_ ="lng_cont_name")
print(a.text) 

#address
b = soup.find("span",class_ ="comp-text")
print(b) 