import json

def get_ronin_address(name):
    with open('scholars.json',"r") as file:
        data=json.load(file)
        for key in data:
            if(str(name)==key):
                return data[key]
    return None