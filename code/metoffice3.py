URL = "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/310009?res=daily&key=0214dd6a-9ad5-4f34-8015-c0442079f40f"
response  = requests.get(URL)

data = json.loads(response.text)


print data["SiteRep"]["DV"]["Location"]["name"] + ", " + \
      data["SiteRep"]["DV"]["Location"]["i"] + ", " + \
      data["SiteRep"]["DV"]["Location"]["Period"][0]["type"] + ", " + \
      data["SiteRep"]["DV"]["Location"]["Period"][0]["value"] + ", " + \
      data["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["Dm"] + ", " + \
      data["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][1]["Nm"]