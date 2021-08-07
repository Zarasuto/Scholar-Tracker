import re

def slice_mention(mention):
    pattern = "<@&(\d{17,19})>"
    regexp=re.compile(pattern)
    if regexp.search(mention):
        raise ValueError("argument is not a mention")
    else:
        var = str(mention)[3:len(str(mention))-1]
        return var