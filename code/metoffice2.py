# From the file find the site id for Glasgow (310009)
# Now get the weather for Glasgow

URL = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/310009?res=3hourly&key=0214dd6a-9ad5-4f34-8015-c0442079f40f"
response  = requests.get(URL)
print response.text


###### Get the types

#print type(response)
#print type(response.text)

##### The first output is not very readable, so we will do it again and format the output to make it more readable.

#data = json.loads(response.text)
#print type(data)
#print json.dumps(data, indent=2)

