URL = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/310009?res=daily&key=0214dd6a-9ad5-4f34-8015-c0442079f40f"
response  = requests.get(URL)

data = json.loads(response.text)

cline1 = data["SiteRep"]["DV"]["Location"]["name"] + ", " + \
         data["SiteRep"]["DV"]["Location"]["i"] + ", "
for x in  data["SiteRep"]["DV"]["Location"]["Period"]:
    cline2 = cline1 + x["type"] + ", " + x["value"] + ", " + x["Rep"][0]["Dm"] + ", " + x["Rep"][1]["Nm"]
    print cline2


#fw = codecs.open('glasgow_data.csv', 'w', 'utf-8')
#
#cline1 = data["SiteRep"]["DV"]["Location"]["name"] + "," + data["SiteRep"]["DV"]["Location"]["i"]
#for x in data["SiteRep"]["DV"]["Location"]["Period"]:
#    cline2 = cline1 + "," + x["type"]+ "," + x["value"]+ "," + x["Rep"][0]["Dm"] + "," + x["Rep"][1]["Nm"] + "\n"
#    fw.write(cline2)
#    
#fw.close()	
	