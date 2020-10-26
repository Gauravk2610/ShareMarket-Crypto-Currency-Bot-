import json 
from bs4 import BeautifulSoup
import requests

URL = "https://coinmarketcap.com/"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

data1 = []
def crypto_load():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    a = soup.find('div', class_="vmm4qx-0 dSjGWZ cmc-table-listing cmc-table-listing--is-tab-selected")
    var = 0
    data = {}
    for col in a.find_all('div', class_='cmc-table__table-wrapper-outer'):
        var +=1
        if var == 3:
            # print(col.getText())
            b = col.find('div')
            c = b.find('table')
            d = c.find('tbody')
            for row in d.find_all('tr'):
                # print(row.find_all('td').getText().split())
                count = 0
                for td in row.find_all('td')[1:]:
                    count += 1
                    crypto_data = td.getText().strip()
                    if bool(crypto_data) :
                        if count == 1:
                            coin_name = crypto_data
                            data1.append(coin_name.lower())
                            data[coin_name.lower()] = []
                            data[coin_name.lower()].append(crypto_data)
                            tn = td.find('div')
                            try:
                                img = tn.img['src']
                                data[coin_name.lower()].append(img)
                            except Exception :
                                img = None
                                data[coin_name.lower()].append(img)
                            continue
                        data[coin_name.lower()].append(crypto_data)
    print(data1)                   

    with open('crypto_data.json', 'w') as outline:
        json.dump(data, outline, indent=4)

def load_crypto(entry):

    with open('crypto_data.json') as outfile:
        data = json.load(outfile)
        title = data[entry][0]
        img_url = data[entry][1]
        market_cap = ("Market Cap : "+ data[entry][2] )
        current_price  = ("Price : " + data[entry][3])
        if "-" not in data[entry][6]: 
            change = ("Change : +" + data[entry][6])
            # print(change)
        else:
            change = ("Change : " + data[entry][6])
        subtitle = ( market_cap+ "\n" + current_price + "\n" + change)
        # print(subtitle)
        element = [{
                                    "title":title,
                                    "image_url":img_url,
                                    "subtitle":subtitle,
                                    "default_action": {
                                    "type": "web_url",
                                    "url": "https://coinmarketcap.com/",
                                    "webview_height_ratio": "tall",
                                    },
                                    "buttons":[
                                    {
                                        "type":"web_url",
                                        "url":"https://coinmarketcap.com/",
                                        "title":"View Website"
                                    }              
                                    ]      
                                }]
    return element
# print(load_crypto("monero"))
# crypto_load()