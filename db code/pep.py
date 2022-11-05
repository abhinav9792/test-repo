import requests
from bs4 import BeautifulSoup

# page ="https://www.pepperfry.com/elle-3-seater-sofa-in-printed-fabric-casacraft-by-pepperfry-1931177.html?type=microsite&pos=1:1&total_result=17&micrositeid=742"
# url = requests.get(page).text
# soup = BeautifulSoup(url,"lxml")
# print(soup.title)
url2 ="https://www.flipkart.com/techobucks-eating-stainless-steel-chinese-chopstick/p/itm1a7266eed61fe?pid=COPGBJCWBYXZDGTQ&lid=LSTCOPGBJCWBYXZDGTQ8ZM5YI&marketplace=FLIPKART&q=chopsticks&store=upp%2Fi7t%2Fbel&srno=s_1_10&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&fm=Search&iid=3b0cc0be-dc21-4b23-8afc-e485f7723a77.COPGBJCWBYXZDGTQ.SEARCH&ppt=sp&ppn=sp&qH=1c55726d7354d244"
#adding url of the page of whom to scrap data
url ="https://www.pepperfry.com/elle-3-seater-sofa-in-printed-fabric-casacraft-by-pepperfry-1931177.html?type=microsite&pos=1:1&total_result=17&micrositeid=742"
#url = "https://www.flipkart.com/canon-eos-1500d-dslr-camera-body-18-55-mm-ii-lens/p/itm033175ceb4ddd?pid=DLLFAEWE22ZAERXG&lid=LSTDLLFAEWE22ZAERXGWBJCOR&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=hp_omu_Best%2Bof%2BElectronics_6_10.dealCard.OMU_RXN53TXGM0FD_5&otracker1=hp_omu_WHITELISTED_neon%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_6_NA_view-all_5&fm=neon%2Fmerchandising&iid=6adc2153-d9e4-4b46-b5ab-b1bd896d28c5.DLLFAEWE22ZAERXG.SEARCH&ppt=hp&ppn=homepage&ssid=9xylne3u800000001646928923281"
scrap = requests.get(url)
# soup = BeautifulSoup(scrap,"lxml")
print(scrap.raise_for_status())
