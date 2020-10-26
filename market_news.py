import requests
from bs4 import BeautifulSoup
import json
URL = "https://www.moneycontrol.com/news/business/markets/"
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
def market_newss():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    # main_box = soup.find('ul', id="cagetory").getText()
    data = []
    table = soup.find('div', class_="fleft")
    col = table.find('ul', id="cagetory")
    # print(col.prettify())
    for col1 in col.find_all('li'):
        # col = soup.find_all('li', class_="clearfix")
        try:
            quote = {}
            quote['title'] = col1.a['title']
            quote['sub-title'] = col1.p.getText()
            quote['url'] = col1.a['href']
            quote['image_url'] = col1.img['data']
            # print(col.prettify())
            # print(quote)
            data.append(quote)
        except Exception as e:
            pass
    print(data)
    with open('news.json', "w") as outline:
        json.dump(data, outline, indent=4)