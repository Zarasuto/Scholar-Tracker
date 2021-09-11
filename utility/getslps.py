import sqlscripts
import scholar_data

def get_scholar_slp():
    scholars = sqlscripts.get_all_scholar_data()
    data = [(item[0],item[1]) for item in scholars]
    scholar_list = [(name[0],scholar_data.get_slp_data(name[1])["earnings"]['slp_inventory']) for name in data]
    return scholar_list
