import sqlite3
from utility.checkaddress import is_valid_address

def add_scholar(name,address,cut):
    conn = sqlite3.connect('scholars.db')
    c = conn.cursor()
    c.execute("INSERT INTO scholars VALUES(?,?,?)",(name,address,cut))
    conn.commit()
    conn.close()
    
def edit_scholar(name):
    pass 

def get_scholar_data(target):
    conn = sqlite3.connect('scholars.db')
    c = conn.cursor()
    if(is_valid_address(target)):
        c.execute(f"SELECT * FROM scholars WHERE address='{target}'")
    else:
        c.execute(f"SELECT * FROM scholars WHERE name='{target}'")
    data = c.fetchall()
    conn.close()
    return data

def get_all_scholar_data():
    conn = sqlite3.connect('scholars.db')
    c = conn.cursor()
    c.execute("SELECT * FROM scholars")
    data = c.fetchall()
    conn.close()
    return data

def delete_scholar(address):
    conn = sqlite3.connect('scholars.db')
    c = conn.cursor()
    c.execute("DELETE FROM scholars WHERE address= ?",(address))
    conn.commit()
    conn.close()

def edit_cut(target,change):
    conn = sqlite3.connect('scholars.db')
    c = conn.cursor()
    if(is_valid_address(target)):
        c.execute(f" UPDATE scholars SET cut = ? WHERE address = '{target}'", (change,))
    else:
        c.execute(f" UPDATE scholars SET cut = ? WHERE name = '{target}'", (change,))
    conn.commit()
    conn.close()
