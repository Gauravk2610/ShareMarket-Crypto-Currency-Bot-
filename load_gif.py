import random

update_url = ['https://media.giphy.com/media/rl0FOxdz7CcxO/giphy.gif', 'https://media.giphy.com/media/1fgI4bZpCo9S57r4Vd/giphy.gif', 'https://media.giphy.com/media/3o7bu3XilJ5BOiSGic/giphy.gif',\
    'https://media.giphy.com/media/cnzP4cmBsiOrccg20V/giphy.gif', 'https://media.giphy.com/media/y1ZBcOGOOtlpC/giphy.gif', 'https://media.giphy.com/media/VX7yEoXAFf8as/giphy.gif']

complete_url = ['https://media.giphy.com/media/icPn4EwqNpAsZQmInZ/giphy.gif', 'https://media.giphy.com/media/26tP9F5MWTXOJL3DG/giphy.gif', 'https://media.giphy.com/media/5n9EYHtrnn2M4rdQMU/giphy.gif',\
    'https://media.giphy.com/media/l4EpblDY4msVtKAOk/giphy.gif', 'https://media.giphy.com/media/H4zC1A2FZ0ViA6GcxD/giphy.gif', 'https://media.giphy.com/media/L4ZZNbDpOCfiX8uYSd/giphy.gif']

news_url = ['https://media.giphy.com/media/l0Iy67eveh48xHQFa/giphy.gif', 'https://media.giphy.com/media/QP8f6jgNcsOyhNBDNb/giphy.gif', 'https://media.giphy.com/media/3bzW3b6ILbN1ZY5974/giphy.gif',\
    'https://media.giphy.com/media/TgJQI8wlEWBusPqDrF/giphy.gif', 'https://media.giphy.com/media/UVSsHRESNbRYevZJJ1/giphy.gif', 'https://media.giphy.com/media/TgJQI8wlEWBusPqDrF/giphy.gif']

stock_url = ['https://media.giphy.com/media/S4178TW2Rm1LW/giphy.gif', 'https://media.giphy.com/media/AgHBbekqDik0g/giphy.gif', 'https://media.giphy.com/media/JtBZm3Getg3dqxK0zP/giphy.gif', 'https://media.giphy.com/media/mgByAN6FfHTnq/giphy.gif', \
    'https://media.giphy.com/media/l0OXXpl20sY9G0uJy/giphy.gif', 'https://media.giphy.com/media/3o7WIsoNhSNAZ8U2GI/giphy.gif', 'https://media.giphy.com/media/KbfDRCD1GB9VTrzvtB/giphy.gif']

nope_url = ['https://giphy.com/gifs/new-girl-jake-johnson-nick-miller-VqPpOjb1rOBBS', 'https://giphy.com/gifs/mrw-front-rthedonald-wofftnAdDtx4s', 'https://giphy.com/gifs/404-14uQ3cOFteDaU', 'https://giphy.com/gifs/error-404-not-found-kF0ngyP7S1DfmzKqiN']

crypto_url = ['https://giphy.com/gifs/money-bitcoin-crypto-mCghKeLLkjgttG9lK9', 'https://giphy.com/gifs/bitcoin-visuals-network-MFabj1E9mgUsqwVWHu', 'https://giphy.com/gifs/crypto-ethereum-eth-MagSgolK3ScWvtHAB4', 'https://giphy.com/gifs/Cryply-jesus-cryply-cryptojesus-lpmv5pQNN332wF6Fue']

happy_url = ['https://giphy.com/gifs/happy-car-home-rdma0nDFZMR32', 'https://giphy.com/gifs/happy-excited-cartoons-F6PFPjc3K0CPe', 'https://giphy.com/gifs/jimgaffigan-jim-gaffigan-39onL3yTmFw8I8agYk', 'https://giphy.com/gifs/victoriajustice-victoria-justice-3og0ICmyySyzbmnxqE']

sad_url = ['https://giphy.com/gifs/mrw-song-myself-Ty9Sg8oHghPWg', 'https://giphy.com/gifs/filmeditor-christmas-movies-a-story-3o6wrebnKWmvx4ZBio', 'https://giphy.com/gifs/sad-a9xhxAxaqOfQs', 'https://giphy.com/gifs/sad-baby-wIhfELB4LvDhe']

def updating():
    image_url = random.choice(update_url)
    return image_url

def nope():
    image_url = random.choice(nope_url)
    return image_url

def complete():
    image_url = random.choice(complete_url)
    return image_url   

def news_complete():
    image_url = random.choice(news_url)
    print(type(image_url))
    return image_url  

def stock_show():
    image_url = random.choice(stock_url)
    return image_url  

def crypto_show():
    image_url = random.choice(crypto_url)
    return image_url 

def happy():
    image_url = random.choice(happy_url)
    return image_url

def sad():
    image_url = random.choice(sad_url)
    return image_url