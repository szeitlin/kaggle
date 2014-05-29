["artist"][0]["@attr"]["rank"] == 1 import json
import requests
from pprint import pprint
def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    url = "JSON: /2.0/?method=geo.gettopartists&country=spain&api_key=0628ffd27796eb8d7720e5baef0731c7"
    
    data = requests.get(url).text
    data = json.loads(data) #convert to a python dict
    
    print type(data)
    
    pprint(data)
    
    print data["topartists"]["artist"][0]["@attr"]["rank"]  #should return 1  
#the 0 is there because artist is a list    
    
    #return artist # return the top artist in Spain 

    return data["topartists"]["artist"][0]["name"] 
