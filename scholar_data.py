from bs4 import BeautifulSoup
import requests
import json

#accepts ronin address
#returns JSON variable named "data"
def getdata(address):
    url = f"https://game-api.skymavis.com/game-api/clients/0x{address}/items/1"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    data = json.loads(soup.find('p').text)
    return data