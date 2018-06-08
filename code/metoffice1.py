# Get a list of sites and write them to a file

import codecs
import requests
import json

URL = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=0214dd6a-9ad5-4f34-8015-c0442079f40f"
response  = requests.get(URL)
data = json.loads(response.text)

fw = codecs.open('sitelist.csv', 'w', 'utf-8')

for x in data["Locations"]["Location"]:
    cline = x["name"]+","+x["id"]+"\n"
    fw.write(cline)
    
fw.close()