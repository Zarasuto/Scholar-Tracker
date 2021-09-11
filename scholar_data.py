from bs4 import BeautifulSoup
import requests
import json

#accepts ronin address
#returns JSON variable named "data"
def get_slp_data(address):
    url = f"https://api.lunaciaproxy.cloud/_earnings/0x{address[6:]}"
    r = requests.get(url)
    data = r.json()
    return data

def get_mmr_data(address):
    url = f"https://api.lunaciaproxy.cloud/_stats/0x{address[6:]}"
    r = requests.get(url)
    data = r.json()
    return data

