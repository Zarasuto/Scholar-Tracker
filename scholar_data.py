from bs4 import BeautifulSoup
import requests
import json

#accepts ronin address
#returns JSON variable named "data"
def getdata(address):
    url = "https://api.lunaciarover.com/stats/0x"+address
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    data = json.loads(soup.find('p').text)
    return data