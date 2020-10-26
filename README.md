# ShareMarket-Crypto-Currency-Bot-
Messenger Quick Replies with Wit.ai Integration 

![AddAudioToVideo1600666759393-001 (1)-min](https://user-images.githubusercontent.com/63660013/97191281-bb6a3880-17cc-11eb-95a1-d27f7cc82456.gif)

# ShareMarket & CryptoCurrency Bot
>## **Messenger Quick Replies & Wit.ai Integration**
>This is Written Tutorial on how you can create the same chatbot with perfect explaination
---
### Facebook app allows us to retrieve and post request as well as post data on facebook via Facebook API.
### Facebook API provides the interface and methods to interact with the Facebook App.
### The Facebook API acts as the interface between the user and the Facebook.
1. Create A Facebook Page thats a Simple Process 
2. Go To https://developers.facebook.com/
3. You will see a Awesome interface where you can login to your facebook account. Login button at the top right besides the search icon . Login Through Your Credentials .
4. Click on My Apps which will navigate you to the **Create App** page .
5. So Click on **Create App** . You will be prompted with 4 options select the one which interests you here we will be using the first one `Manage Business Integration` option, then continue . Enter your app name EG:- test-app. Now select the app purpose. Then Create App . Now complete the security check recaptcha and submit. 
6. Then you will be navigated to a page were you will be prompted to add products to your App in our case it is messenger . Click on **Messenger Setup** Button.
&. Navigated to the next page were you can add and make changes to the settings . Now scroll down towardds the access token . Create a New Page if you don't have else add a page
7. Once you login with the credentials you give the test-app the authority yo manage & message to the page . Once completed you will be given your page access token keep it safe . Select the fb page and continue . Click on Generate Token to get your access token .
---
# Time To Set Up Your Project

>## So This Is A Pure Python Based Tutorial
**Requirements**
- Python3 Installed 
- pip install virtualenv
- create a virtual env and activate it
- pip intall flask, requests, pymessenger, bs4, wit
### So webscrapping will be playing an important role in this
---
## Webhook
--- 
So we have to set up a webhook for our application were we will be adding a callback url through which we can handle all kinds of requests . When we setup a webhook we need to verify our callback url .

So in the docs provided at the https://developers.facebook.com/ is in the java format we will be doing it using python 

1. Create a file app.py
2. Now import all the dependencies and packages and initilaize your flask app
3. Now check the Veriify function in the app.py file through which we will be verifying our callback url. So the word `'hello'` is our callback url token. so when you run the file its runs on the local host for live web interaction we need to take it online for that purpose we need to install ngrok through which you can tunnel up your localhost network .
4. Visit https://ngrok.com/ and install it once done open the terminal in the file were ngrok is extracted and run the command `ngrok.exe http 80`
5. Now you can run your app.py and then then url in ngrok provided enter it at developers.facebook.com for webhook callback url and enter the verifcation token i.e `hello` and select the webhook services.


![bandicam 2020-10-26 09-52-38-374](https://user-images.githubusercontent.com/63660013/97157888-ba221700-179e-11eb-8f73-a0644b727a74.jpg)

---
## Event Handling
---
Now we will handle messaging events. So as you see in the app.py we have setup a app route 

![bandicam 2020-10-26 10-02-03-374](https://user-images.githubusercontent.com/63660013/97158699-ceb2df00-179f-11eb-9dc9-aede9eb9820a.jpg)

The Function `def webhook():` will be handling all kinds of requests If you want you can event print out the whole request to see how the actually the request is been received

We are actually handling and extracting the data from the json format request and extracting the relevant data

![bandicam 2020-10-26 09-14-02-542](https://user-images.githubusercontent.com/63660013/97159837-71b82880-17a1-11eb-937a-e7b0c5984a73.jpg)


---
## Webscrapping
---

So Now we have to create some other files from were will firstly do some webscrapping and extract the relevant data .

Now you can open the other python files to check what exactly is happening and in which format is exactly the data been stored

For the sharemarket database we will be scrapping data from https://www.moneycontrol.com/ & for crypto-currency https://coinmarketcap.com/ we will be extracting the required data and storing it is a certain format as required and specified in messenger quick replies docs 

Open utils.py to get the basic idea how exactly the data is scrapped and filtered out and is stored in the json format
![bandicam 2020-10-26 09-06-10-557](https://user-images.githubusercontent.com/63660013/97164819-b8f5e780-17a8-11eb-90c0-774d7086fc6a.jpg)

This What the database looks like

![bandicam 2020-10-26 09-56-38-225](https://user-images.githubusercontent.com/63660013/97163906-5c45fd00-17a7-11eb-9755-d69ffd8e3111.jpg)

> Similarly You can check the other python files to see what and how data is filtered out and stored 

---
## Wit.ai Integration in python 
---
Now we will be creating and training the bot to analysize the messages firstly open https://wit.ai/ login and create a app and start training it with some local commands and then create entities, entity EG:- price of tcs 

Here the entity will be share_market

So go on training to increase the accuracy of your bot 

Now open `user_response.py` now take the access token and see how the response is been handled

![bandicam 2020-10-26 09-18-34-138](https://user-images.githubusercontent.com/63660013/97165945-746b4b80-17aa-11eb-8be8-b8f48d6f44be.jpg)

---
## App.py Now Open This File To Check How All The Responses are handled
---
![bandicam 2020-10-26 09-25-27-468](https://user-images.githubusercontent.com/63660013/97166509-60741980-17ab-11eb-9003-64eae4b2fe7e.jpg)
