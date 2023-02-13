
#XML
#<person>
 # <name>Chuck</name>
  #<phone type="intl">
   # +1 734 303 4456
#</phone>
 # <email hide="yes" />
#</person>

import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data) #info dictionary
print(info[1]['name'])
#1 list 2 dictionaries

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("enter location: ")
    if len(address) < 1:break

    url = serviceurl + urllib.parse.urlencode({"address": address})

    print("retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("retrieved",  len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
         print("==== Failure To Retrieve ====")
         print(data)
    continue

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print("lat", lat, "lng", lng)
location = js["results"][0]["formatted_address"]
print(location)