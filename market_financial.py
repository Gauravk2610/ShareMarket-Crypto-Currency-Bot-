import requests
from bs4 import BeautifulSoup
import json
URL = ["https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/hdfcbank/HDF01", "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/axisbank/AB16", "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/kotakmahindrabank/KMB", "https://www.moneycontrol.com/india/stockpricequote/textiles-woollenworsted/raymond/R",
        "https://www.moneycontrol.com/india/stockpricequote/power-generationdistribution/adanipower/AP11", "https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT", "https://www.moneycontrol.com/india/stockpricequote/personal-care/hindustanunilever/HU", "https://www.moneycontrol.com/india/stockpricequote/finance-leasinghire-purchase/bajajfinance/BAF",
        "https://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS", "https://www.moneycontrol.com/india/stockpricequote/refineries/bharatpetroleumcorporation/BPC", "https://www.moneycontrol.com/india/stockpricequote/refineries/indianoilcorporation/IOC", "https://www.moneycontrol.com/india/stockpricequote/retail/futureretail/FR",
        "https://www.moneycontrol.com/india/stockpricequote/plastics/vipindustries/VIP", "https://www.moneycontrol.com/india/stockpricequote/finance-housing/indiabullshousingfinance/IHF01"]
BANK = ["HDFC Bank", "Axis Bank", "Kotak Mahindra Bank", "Raymond", "Adani Power", "Infosys", 
        "Hindustan Unilever", "Bajaj Finance", "Tata Consultancy Services", "Bharat Petroleum Corporation",
        "Indian Oil Corporation", "Future Retail", "VIP Industries", "Indiabulls Housing Finance"]

BANK_SMALL = ["hdfc bank", "axis bank", "kotak mahindra bank", "raymond", "adani power", "infosys", 
        "hindustan unilever", "bajaj finance", "tata Consultancy services", "bharat petroleum corporation",
        "indian oil corporation", "future retail", "vip industries", "indiabulls housing finance", "hdfcbank", "axisbank","kotakbank", 
        "adanipower","infy","hinunilvr", "bajfinance", "tcs","bpcl","oil","fretail","vipind","ibulhsgfin"]

BANK_IMG = ['https://dc-cdn.s3-ap-southeast-1.amazonaws.com/dc-Cover-9iqgefts0481k7f57986e7ab20-20160627012717.Medi.jpeg', 'https://www.searchpng.com/wp-content/uploads/2019/01/Axis-Bank-PNG-Logo-.png', 'https://www.kotak.com/content/dam/Kotak/kotak-bank-logo.jpg', 'https://cdn.freelogovectors.net/wp-content/uploads/2019/10/raymond-logo.png', 'https://i.vimeocdn.com/video/255973172.webp?mw=1400&mh=787&q=70',
            'https://professionallyspeaking.net/wp-content/uploads/2017/04/infosys-logo-1.jpg', 'https://www.hul.co.in/Images/hul-hindustan-u-limited-990x557_tcm1255-551759_w700.jpg', 'https://images.financialexpress.com/2019/09/bajaj-finserv.jpg?w=1200&h=800&imflag=true', 'https://allvectorlogo.com/img/2017/02/tata-consultancy-services-tcs-logo.png', 'https://cdn.telanganatoday.com/wp-content/uploads/2020/06/BPCL.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTzIdv7ad0jclqbDnO79YAILP38Vs3k16Cx5g&usqp=CAU', 'https://img.etimg.com/thumb/msid-77056110,width-1200,height-900,imgsize-88949,overlay-economictimes/photo.jpg', 'https://seeklogo.com/images/V/vip-logo-684049CC20-seeklogo.com.png', 'https://www.forbesindia.com/media/image_uploads/SM_Indiabulls_housing_finance.jpg']

BANK_DICT = {"hdfcbank":"hdfc bank", "axisbank":"axis bank", "kotakbank":"kotak mahindra bank","raymond":"raymond", "adanipower":"adani power",
            "infy":"infosys","hinunilvr":"hindustan unilever", "bajfinance":"bajaj finance", "tcs":"tata consultancy services","bpcl":"bharat petroleum corporation",
            "oil":"indian oil corporation","fretail":"future retail","vipind":"vip industries","ibulhsgfin":"indiabulls housing finance"}

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
def financial_data():
    data = {}
    for i in range(len(URL)):
        page = requests.get(URL[i], headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        total = soup.find('div', class_="tab-content min_ht300")
        total = total.table.tbody.getText()
        total_income = ("Revenue Profit : " + total.strip().split('Total Income')[-1].split()[0] )
        net_profit = ("Net Profit : " + total.strip().split('Net Profit')[-1].split()[0] )
        data[BANK[i].lower()] = []
        data[BANK[i].lower()] = {
            "company":BANK[i],
            "total_income":total_income,
            "net_profit":net_profit,
            "url":URL[i],
            "image_url":BANK_IMG[i]
        }
        print(BANK[i].lower())
        print(total_income) 
        print(net_profit)
    print(data)
    with open("financial.json", "w") as outfile: 
        json_object=json.dump(data, outfile, indent=4)

def load_financial(bank_name):
    elements = []
    with open("financial.json") as outfile:
        data = json.load(outfile)
        for phrase in BANK_SMALL :
            if phrase in bank_name.lower():
                try:
                    if bool(BANK_DICT[phrase]):
                        phrase = BANK_DICT[phrase]
                except Exception:
                    pass
                # print(phrase)
                bank_name = data[phrase]['company']
                total_income = data[phrase]['total_income']
                net_profit = data[phrase]['net_profit']
                url = data[phrase]['url']
                image_url = data[phrase]['image_url']
                subtitle = (total_income +  "\n" + net_profit)
                # print (total_income + "\n" + net_profit)
                element = {
                                "title":bank_name,
                                "image_url":image_url,
                                "subtitle":subtitle,
                                "default_action": {
                                "type": "web_url",
                                "url": url,
                                "webview_height_ratio": "tall",
                                },
                                "buttons":[
                                {
                                    "type":"web_url",
                                    "url":url,
                                    "title":"View Website"
                                }              
                                ]      
                            }
                elements.append(element)
    return elements
# load_financial("stock price of axis bank")
# financial_data()