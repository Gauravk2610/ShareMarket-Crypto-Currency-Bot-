from wit import Wit

def wit_response(messaging_text):
    access_token = 'F6XCF3CXEVRQXDIHU7IKN5HJRD5YHHCG'
    client = Wit(access_token = access_token)

    resp = client.message(messaging_text)
    entity = resp['intents'][0]['name']
    return entity

# print(bool(resp['traits']['wit$thanks']))