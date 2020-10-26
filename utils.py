import requests
from bs4 import BeautifulSoup
import smtplib
import json

URL = ["https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/hdfcbank/HDF01", "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/axisbank/AB16", "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/kotakmahindrabank/KMB", "https://www.moneycontrol.com/india/stockpricequote/textiles-woollenworsted/raymond/R",
        "https://www.moneycontrol.com/india/stockpricequote/power-generationdistribution/adanipower/AP11", "https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT", "https://www.moneycontrol.com/india/stockpricequote/personal-care/hindustanunilever/HU", "https://www.moneycontrol.com/india/stockpricequote/finance-leasinghire-purchase/bajajfinance/BAF",
        "https://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS", "https://www.moneycontrol.com/india/stockpricequote/refineries/bharatpetroleumcorporation/BPC", "https://www.moneycontrol.com/india/stockpricequote/refineries/indianoilcorporation/IOC", "https://www.moneycontrol.com/india/stockpricequote/retail/futureretail/FR",
        "https://www.moneycontrol.com/india/stockpricequote/plastics/vipindustries/VIP", "https://www.moneycontrol.com/india/stockpricequote/finance-housing/indiabullshousingfinance/IHF01"]

BANK = ["HDFC Bank", "Axis Bank", "Kotak Mahindra Bank", "Raymond", "Adani Power", "Infosys", 
        "Hindustan Unilever", "Bajaj Finance", "Tata Consultancy Services", "Bharat Petroleum Corporation",
        "Indian Oil Corporation", "Future Retail", "VIP Industries", "Indiabulls Housing Finance"]

BANK_IMG = ['https://dc-cdn.s3-ap-southeast-1.amazonaws.com/dc-Cover-9iqgefts0481k7f57986e7ab20-20160627012717.Medi.jpeg', 'https://www.searchpng.com/wp-content/uploads/2019/01/Axis-Bank-PNG-Logo-.png', 'https://www.kotak.com/content/dam/Kotak/kotak-bank-logo.jpg', 'https://cdn.freelogovectors.net/wp-content/uploads/2019/10/raymond-logo.png', 'https://i.vimeocdn.com/video/255973172.webp?mw=1400&mh=787&q=70',
            'https://professionallyspeaking.net/wp-content/uploads/2017/04/infosys-logo-1.jpg', 'https://www.hul.co.in/Images/hul-hindustan-u-limited-990x557_tcm1255-551759_w700.jpg', 'https://images.financialexpress.com/2019/09/bajaj-finserv.jpg?w=1200&h=800&imflag=true', 'https://allvectorlogo.com/img/2017/02/tata-consultancy-services-tcs-logo.png', 'https://cdn.telanganatoday.com/wp-content/uploads/2020/06/BPCL.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTzIdv7ad0jclqbDnO79YAILP38Vs3k16Cx5g&usqp=CAU', 'https://img.etimg.com/thumb/msid-77056110,width-1200,height-900,imgsize-88949,overlay-economictimes/photo.jpg', 'https://seeklogo.com/images/V/vip-logo-684049CC20-seeklogo.com.png', 'https://www.forbesindia.com/media/image_uploads/SM_Indiabulls_housing_finance.jpg']


headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
subscribers = ["gauravkonde26@gmail.com"]
message = []
def stock_read():
    print("         CODEGRAMMED" )
    print("       Stock_Alert_Bot")
    data = {}
    for i in range(len(URL)):
        
        page = requests.get(URL[i], headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        price = soup.find('div', class_="pcnsb div_live_price_wrap").get_text()
        change = price.strip().split("(")[-1].replace(")", "")
        if "-" not in change:
            change = "+" + change
            print(change) 
        price = int(price.strip().split(".")[0])
        price_high = soup.find('div', {"class":"clearfix lowhigh_band week52_lowhigh_wrap"}).get_text()
        price_high = int(price_high.strip().split()[4].split(".")[0])
        fall_down = (price_high*60)/100
        BANK_NAME = (BANK[i]).lower()
        
        # message.append(BANK_NAME)
        print(BANK_NAME)
        # print(URL[i])
        # print("Price Drop Detected")
        Current_price=("Current Price : ₹" + str(price))
        Highest_price=("Highest  Price : ₹" +  str(price_high))
        change=("Change : " + str(change))
        # print( "60 percent Fall Down Price " + str(fall_down) + "\n")
        data[BANK_NAME] = []
        data[BANK_NAME] ={ 
            
            "Company_Name":BANK[i],
            "Current_Stock":Current_price,
            "Highest_Stock":Highest_price,
            "Change":change,
            "url":URL[i],
            'image_url':BANK_IMG[i]
            
        }
    with open("data.json", "w") as outfile: 
        json_object=json.dump(data, outfile, indent=4)

# stock_read()

# with open('data.json', 'r') as outfile:
#     data = json.load(outfile)
#     print(data['Axis Bank'])