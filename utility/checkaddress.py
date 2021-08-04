import re
def check_ronin_address(address):
    pattern = re.compile("\Aronin:(.+)")
    if(bool(pattern.search(address)) and len(address[6:])==40):
        return True
    else:
        return False
