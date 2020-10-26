import json
from pymessenger import Element, Button

BANK = ["hdfc bank", "axis bank", "kotak mahindra bank", "raymond", "adani power", "infosys", 
        "hindustan unilever", "bajaj finance", "tata consultancy services", "bharat petroleum corporation",
        "indian oil corporation", "future retail", "vip industries", "indiabulls housing finance"]

BANK_DICT = {"hdfcbank":"hdfc bank", "axisbank":"axis bank", "kotakbank":"kotak mahindra bank","raymond":"raymond", "adanipower":"adani power",
            "infy":"infosys","hinunilvr":"hindustan unilever", "bajfinance":"bajaj finance", "tcs":"tata consultancy services","bpcl":"bharat petroleum corporation",
            "oil":"indian oil corporation","fretail":"future retail","vipind":"vip industries","ibulhsgfin":"indiabulls housing finance"}

BANK_LIST = ["hdfc bank", "axis bank", "kotak mahindra bank", "raymond", "adani power", "infosys", 
        "hindustan unilever", "bajaj finance", "tata Consultancy services", "bharat petroleum corporation",
        "indian oil corporation", "future retail", "vip industries", "indiabulls housing finance", "hdfcbank", "axisbank","kotakbank", 
        "adanipower","infy","hinunilvr", "bajfinance", "tcs","bpcl","oil","fretail","vipind","ibulhsgfin"]

def stock(entry):
    elements = []
    with open('data.json', "r") as outline:
        data = json.load(outline)
        for phrase in BANK_LIST:
            if phrase in entry.lower():
                try:
                    if bool(BANK_DICT[phrase]):
                        phrase = BANK_DICT[phrase]
                except Exception:
                    pass
                print(phrase)
                title = data[phrase]['Company_Name']   
                subtitle = data[phrase]['Current_Stock'] + "\n" +  data[phrase]['Highest_Stock'] + "\n" + data[phrase]['Change']
                if "-" not in data[phrase]['Change']:
                    state = True
                else:
                    state = False
                url = data[phrase]['url']
                image_url = data[phrase]['image_url']
                element = {
                                    "title":title,
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
    return elements, state
def news():
    elements = []
    with open('news.json', 'r') as outline:
        data = json.load(outline)
        print(len(data))
        for i in range(10):
            title = (data[i]['title'])
            subtitle = (data[i]['sub-title'])
            image_url = (data[i]['image_url'])
            url = (data[i]['image_url'])
            element = {
                                "title":title,
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
            # print(element)
        return elements
# print(stock("what is the stock of hdfc bank "))
# news()
# phrase = 'axisbank'
# if  BANK_DICT[phrase]:
    # print(phrase)
    # print(bool(BANK_DICT[phrase]))