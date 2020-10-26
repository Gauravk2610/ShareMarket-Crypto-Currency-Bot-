import os, sys
from flask import Flask, request
from pymessenger import Bot
from utils import stock_read
from detail import stock, news
from pymessenger import Element, Button
from market_financial import load_financial, financial_data
from market_news import market_newss
from crypto import load_crypto, crypto_load
from user_response import wit_response
from load_gif import updating, complete, news_complete, stock_show, nope, crypto_show, sad, happy
import json
# from utils import wit_response

app = Flask(__name__)
PAGE_ACCES_TOKEN = 'EAAEniWjZCNuMBALkw98OvbGTBkFIBrpOwDIzNNTlt9gZBseHIJN4yMZCV0ZCveoXpK51GftfoayOoqJr9cLuVJKECQ2kP5Vw7rzDigJ7cqpBOeW8tnfDWHz8pcDFjv3yfPX5WWuZAeA3vpibwfs8d8JlZBABtUYBCNF3p0F90CpkuZCYTnEjzuX'
bot = Bot(PAGE_ACCES_TOKEN)
crypto_name = ['bitcoin', 'ethereum', 'tether', 'xrp', 'polkadot', 'bitcoin cash', 'binance coin', 'chainlink', 'crypto.com coin', 'litecoin', 'bitcoin sv', 'cardano', 'eos', 'usd coin', 'tron', 'tezos', 'stellar', 'monero', 'neo', 'unus sed leo', 'huobi token', 'cosmos', 'nem', 'yearn.finance', 'vechain', 'uma', 'iota', 'aave', 'dash', 'wrapped bitcoin', 'dai', 'ethereum classic', 'zcash', 'ontology', 'trueusd', 'maker', 'omg network', 'synthetix network token', 'theta', 'binance usd', 'compound', 'kusama', 'algorand', 'basic attention token', 'okb', 'hedgetrade', 'ftx token', 'dogecoin', 'digibyte', 'bittorrent', '0x', 'celo', 'energy web token', 'nxm', 'icon', 'hyperion', 'loopring', 'waves', 'paxos standard', 'qtum', 'kyber network', 'ren', 'flexacoin', 'hedera hashgraph', 'zilliqa', 'augur', 'lisk', 'dfi.money', 'decred', 'elrond', 'sushiswap', 'bitcoin gold', 'siacoin', 'balancer', 'aragon', 'band protocol', 'celsius', 'zb token', 'husd', 'ampleforth', 'enjin coin', 'reserve rights', 'abbc coin', 'terra', 'revain', 'quant', 'blockstack', 'ravencoin', 'cybervein', 'decentraland', 'ocean protocol', 'arweave', 'bytom', 'nano', 'bitcoin diamond', 'nervos network', 'swipe', 'golem', 'dxchain token', 'numeraire']
@app.route('/', methods=['GET'])
def verify():
    #webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello": 
            return "Verification token mismatch", 403
        return request.args['hub.challenge'], 200
    return "hello world", 200

def gif(recipient_id, image_url):

    result = bot.send_image_url(recipient_id, image_url)
last_message = None

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)
    print(data)
    if data['object'] =='page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']
                global last_message
                if messaging_event.get('message'):
                    if 'is_echo' not in messaging_event['message']:
                        if 'text' in messaging_event['message']:
                            messaging_text = messaging_event['message']['text']
                            if messaging_text != last_message:
                                last_message = messaging_text
                                print("last_message:"+last_message)
                                entity = None
                                # print(messaging_text)
                                response = None
                                try:
                                    entity = wit_response(messaging_text)
                                    print(entity)
                                except Exception:
                                    pass
                                
                                if entity == "price_crypto":
                                    for phrase in crypto_name :
                                        if phrase in messaging_text.lower():
                                            element = load_crypto(phrase)
                                            bot.send_generic_message(sender_id, element)
                                            image_url = stock_show()
                                            gif(sender_id, image_url)
                                        else:
                                            pass
                                        # image_url = 'https://media.giphy.com/media/rl0FOxdz7CcxO/giphy.gif'
                                        
                                    # continue
                                
                                elif entity == 'welcome_greets':
                                    print("welcome")
                                    image_url = news_complete()
                                    print("Done")
                                    response = 'Hello I am your Share Market & Crypto-Currency Bot \n\nHow can i help You? \n\n'\
                                        + "Here are a Command Before we get Started \n\nupdate=>updates the database always do this before you get started\n\n"\
                                            + "then just feel free to ask me anything 😄 "
                                    bot.send_text_message(sender_id, response)
                                    gif(sender_id, image_url)


                                elif entity == 'stock_update':
                                    image_url = news_complete()
                                    # print(image_url)
                                    print("Done")
                                    buttons = []
                                    button = Button(title='Stocks', type='postback', payload='stocks')
                                    buttons.append(button)
                                    button = Button(title='Crypto-Currency', type='postback', payload='crypto-currency')
                                    buttons.append(button)
                                    text = 'Select One To Update '
                                    result = bot.send_button_message(sender_id, text, buttons) 
                                    gif(sender_id, image_url)
                                
                                elif entity == "stock_price" :
                                    state = None
                                    print("Done")
                                    element,state = stock(messaging_text)
                                    # if bool(element) != False:
                                    bot.send_generic_message(sender_id, element)
                                    print(state)
                                    if state is True:
                                        image_url = happy()
                                        print(image_url)
                                        gif(sender_id, image_url)
                                    else:
                                        image_url  = sad()
                                        gif(sender_id, image_url)
                                    print(image_url)
                                    
                                            
                                    # else:
                                    #     image_url = nope()
                                    #     gif(sender_id, image_url)
                                    #     continue
                                    gif(sender_id, image_url)
                                    # image_url = 'https://media.giphy.com/media/rl0FOxdz7CcxO/giphy.gif'
                                    
                                    
                                elif entity == "stock_news":
                                    print("Done")
                                    element = news()
                                    if bool(element) != False:
                                        bot.send_generic_message(sender_id, element)
                                    else:
                                        image_url = nope()
                                        gif(sender_id, image_url)
                                        continue
                                    # image_url = 'https://media.giphy.com/media/rl0FOxdz7CcxO/giphy.gif'
                                    image_url = news_complete()
                                    gif(sender_id, image_url)
                                elif entity == "stock_financial":
                                    element = load_financial(messaging_text)
                                    bot.send_generic_message(sender_id, element)
                                    # else:
                                    #     image_url = nope()
                                    #     gif(sender_id, image_url)
                                    #     continue
                                    image_url = stock_show()
                                    gif(sender_id, image_url)
                        else:
                            # pass
                            messaging_text = 'no text' 
                elif messaging_event.get('postback'):
                    if 'title' in messaging_event['postback']:
                        messaging_text = messaging_event['postback']['title']
                        print(messaging_text)
                        if messaging_text != last_message:
                            last_message = messaging_text
                            if 'Stocks' in messaging_text:
                                print(messaging_text)
                                image_url = updating()
                                gif(sender_id, image_url)
                                bot.send_text_message(sender_id, "Starting")
                                stock_read()

                                bot.send_text_message(sender_id, "Completetd =====>20%")
                                market_newss()
                                bot.send_text_message(sender_id, "Completetd =====>60%")
                                financial_data()
                                bot.send_text_message(sender_id, "Completetd =====>100%")

                            elif 'Crypto-Currency' in messaging_text:
                                image_url = complete()
                                print(image_url)
                                crypto_load()
                                print("Done")
                                gif(sender_id, image_url)
                                response = "Done"
                                bot.send_text_message(sender_id, response)
                    # messaging_text = messaging_text.lower()
                    # response = None
                    # entity, value = wit_response(messaging_text)
                    # print(entity, value)
                    # if entity == "newstype:newstype":
                    #     response = "Ok. I will send you {} news".format(str(value))
                    # elif entity == "location:location":
                    #     response = "ok so you live in {0}. I will send you top headlines from {0}".format(str(value))
                    # elif response == None:
                    #     response = "sorry i didnt get you"
                    
                        # response = stock(messaging_text)

                    # buttons = []
                    # button = Button(title='Arsenal', type='web_url', url='http://arsenal.com')
                    # buttons.append(button)
                    # button = Button(title='Other', type='postback', payload='other')
                    # buttons.append(button)
                    # text = 'Select One To Update '
                    # buttons = []
                    # button = Button(title='Stocks', type='postback', payload='stocks')
                    # buttons.append(button)
                    # button = Button(title='Crypto-Currency', type='postback', payload='crypto-currency')
                    # buttons.append(button)
                    # text = 'Select One To Update '
                    # result = bot.send_button_message(sender_id, text, buttons) 
                    # # image_url = 'https://lh4.googleusercontent.com/-dZ2LhrpNpxs/AAAAAAAAAAI/AAAAAAAA1os/qrf-VeTVJrg/s0-c-k-no-ns/photo.jpg'
                    # # elements = []
                    # '''element = Element(title=title, image_url="https://images.moneycontrol.com/images/common/header/logo.png?v=0.2&impolicy=mchigh", subtitle=subtitle,
                    #                 item_url="https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/hdfcbank/HDF01"   )
                    
                    # elements.append(element)'''
                    # # element = Element(title=title, subtitle=subtitle, webview="tall")
                    
                    # elements.append(element)
                    # # result = bot.send_generic_message(sender_id, elements)
                    # buttons = []
                    # button = Button(title='Arsenal', type='web_url', url='http://arsenal.com')
                    # buttons.append(button)
                    # button = Button(title='Other', type='postback', payload='other')
                    # buttons.append(button)
                    # text = 'Select'           
                    # result = bot.send_button_message(sender_id, text, buttons)
                    
#                     print("DONE")
#                     bot.send_text_message(sender_id, elements)
#                     # response = {
#                     #             'attachment': {
#                     #                 'type': 'image',
#                     #                 'payload': {
#                     #                     'url': 'http://facebook.com/image.jpg'
#                     #                 }
#                     #             }
#                     #         }
#                     # image_url = 'https://lh4.googleusercontent.com/-dZ2LhrpNpxs/AAAAAAAAAAI/AAAAAAAA1os/qrf-VeTVJrg/s0-c-k-no-ns/photo.jpg'
#                     # result = bot.send_image_url(recipient_id, image_url)
#                     # user_profile = bot.get_user_info(recipient_id)
#                     image_url = 'https://media.giphy.com/media/rl0FOxdz7CcxO/giphy.gif'
#                     result = bot.send_image_url(recipient_id, image_url)
#                     image_url = 'https://media.giphy.com/media/1fgI4bZpCo9S57r4Vd/giphy.gif'
#                     bot.send_image_url(recipient_id, image_url)

    return "ok", 200

def log(message):
    # print(message)
    sys.stdout.flush()

if __name__ == '__main__':
    app.run(debug=True,  port=80)