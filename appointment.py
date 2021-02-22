import requests
import json

#find appointments for flu shot from 5 nearest walgreens

zipcode = "53149"
date = "02/22/2021"
age = 21

#get lat and long for zipcode
lat_long_endpoint = f"https://api.promaptools.com/service/us/zip-lat-lng/get/?zip={zipcode}&key=17o8dysaCDrgv1c"
response = requests.get(lat_long_endpoint,verify=False)

lat = response.json()["output"][0]["latitude"]
lng = response.json()["output"][0]["longitude"]

#search for 5 nearest stores with pharm
search_endpoint = "https://www.walgreens.com/locator/v1/stores/search"
search_payload = {"filterOptions": "[rx]",
           "p": "1",
           "q": zipcode,
           "r": "50",
           "requestType": "locator",
           "s": "5",
           "lat": lat,
           "lng": lng}
response = requests.post(search_endpoint, 
                         data = json.dumps(search_payload), 
                         headers={'Content-Type': 'application/json'})

stores = response.json()["results"]
for store in stores:
    address = store["store"]["address"]

    #search for timeslot
    search_endpoint = "https://www.walgreens.com/schedulerservice/timeslot/search"
    search_payload = {"startDate": date,
                      "endDate": date,
                      "apptType": "rx",
                      "patientAge": age,
                      "serviceID" : "1",
                      "serviceName": "Flu (Influenza)",
                      "stores": [store]}

    response = requests.post(search_endpoint, 
                            data = json.dumps(search_payload), 
                            headers={'Content-Type': 'application/json'})    

    slots = response.json()["availableSlots"][0]["slots"]
    print (f"{address['city']}, {address['street']}")
    print(json.dumps(slots, indent=2))



# Sample output

# MUKWONAGO, 212 N ROCHESTER ST
# [
#   {
#     "date": "02/22/2021",
#     "day": "Monday",
#     "Before 8 AM": [],
#     "8 AM - 12 PM": [],
#     "12 PM - 3 PM": [],
#     "3 PM - 6 PM": [
#       "03:20 PM",
#       "03:30 PM",
#       "03:40 PM",
#       "03:50 PM",
#       "04:00 PM",
#       "04:10 PM",
#       "04:20 PM",
#       "04:30 PM",
#       "04:40 PM",
#       "04:50 PM",
#       "05:00 PM",
#       "05:10 PM",
#       "05:20 PM",
#       "05:30 PM",
#       "05:40 PM",
#       "05:50 PM"
#     ],
#     "6 PM - 9 PM": [
#       "06:00 PM",
#       "06:10 PM",
#       "06:20 PM",
#       "06:30 PM",
#       "06:40 PM",
#       "06:50 PM",
#       "07:00 PM",
#       "07:10 PM",
#       "07:20 PM",
#       "07:30 PM",
#       "07:40 PM",
#       "07:50 PM",
#       "08:00 PM",
#       "08:10 PM",
#       "08:20 PM",
#       "08:30 PM",
#       "08:40 PM",
#       "08:50 PM"
#     ],
#     "After 9 PM": []
#   }
# ]
# WALES, 320 W SUMMIT AVE
# [
#   {
#     "date": "02/22/2021",
#     "day": "Monday",
#     "Before 8 AM": [],
#     "8 AM - 12 PM": [],
#     "12 PM - 3 PM": [],
#     "3 PM - 6 PM": [
#       "03:20 PM",
#       "03:30 PM",
#       "03:40 PM",
#       "03:50 PM",
#       "04:00 PM",
#       "04:10 PM",
#       "04:20 PM",
#       "04:30 PM",
#       "04:40 PM",
#       "04:50 PM",
#       "05:00 PM",
#       "05:10 PM",
#       "05:20 PM",
#       "05:30 PM",
#       "05:40 PM",
#       "05:50 PM"
#     ],
#     "6 PM - 9 PM": [
#       "06:00 PM",
#       "06:10 PM",
#       "06:20 PM",
#       "06:30 PM",
#       "06:40 PM",
#       "06:50 PM",
#       "07:00 PM",
#       "07:10 PM",
#       "07:20 PM",
#       "07:30 PM",
#       "07:40 PM",
#       "07:50 PM"
#     ],
#     "After 9 PM": []
#   }
# ]
# WAUKESHA, 221 E SUNSET DR
# [
#   {
#     "date": "02/22/2021",
#     "day": "Monday",
#     "Before 8 AM": [],
#     "8 AM - 12 PM": [],
#     "12 PM - 3 PM": [],
#     "3 PM - 6 PM": [
#       "03:20 PM",
#       "03:30 PM",
#       "03:40 PM",
#       "03:50 PM",
#       "04:00 PM",
#       "04:10 PM",
#       "04:20 PM",
#       "04:30 PM",
#       "04:40 PM",
#       "04:50 PM",
#       "05:00 PM",
#       "05:10 PM",
#       "05:20 PM",
#       "05:30 PM",
#       "05:40 PM",
#       "05:50 PM"
#     ],
#     "6 PM - 9 PM": [
#       "06:00 PM",
#       "06:10 PM",
#       "06:20 PM",
#       "06:30 PM",
#       "06:40 PM",
#       "06:50 PM",
#       "07:00 PM",
#       "07:10 PM",
#       "07:20 PM",
#       "07:30 PM",
#       "07:40 PM",
#       "07:50 PM",
#       "08:00 PM",
#       "08:10 PM",
#       "08:20 PM",
#       "08:30 PM",
#       "08:40 PM",
#       "08:50 PM"
#     ],
#     "After 9 PM": [
#       "09:00 PM",
#       "09:10 PM",
#       "09:20 PM",
#       "09:30 PM",
#       "09:40 PM",
#       "09:50 PM",
#       "10:00 PM",
#       "10:10 PM",
#       "10:20 PM",
#       "10:30 PM",
#       "10:40 PM",
#       "10:50 PM"
#     ]
#   }
# ]
# WAUKESHA, 601 MEADOWBROOK RD
# [
#   {
#     "date": "02/22/2021",
#     "day": "Monday",
#     "Before 8 AM": [],
#     "8 AM - 12 PM": [],
#     "12 PM - 3 PM": [],
#     "3 PM - 6 PM": [
#       "03:20 PM",
#       "03:30 PM",
#       "03:40 PM",
#       "03:50 PM",
#       "04:00 PM",
#       "04:10 PM",
#       "04:20 PM",
#       "04:30 PM",
#       "04:40 PM",
#       "04:50 PM",
#       "05:00 PM",
#       "05:10 PM",
#       "05:20 PM",
#       "05:30 PM",
#       "05:40 PM",
#       "05:50 PM"
#     ],
#     "6 PM - 9 PM": [
#       "06:00 PM",
#       "06:10 PM",
#       "06:20 PM",
#       "06:30 PM",
#       "06:40 PM",
#       "06:50 PM",
#       "07:00 PM",
#       "07:10 PM",
#       "07:20 PM",
#       "07:30 PM",
#       "07:40 PM",
#       "07:50 PM",
#       "08:00 PM",
#       "08:10 PM",
#       "08:20 PM",
#       "08:30 PM"
#     ],
#     "After 9 PM": []
#   }
# ]
# MUSKEGO, S79W18885 JANESVILLE RD
# [
#   {
#     "date": "02/22/2021",
#     "day": "Monday",
#     "Before 8 AM": [],
#     "8 AM - 12 PM": [],
#     "12 PM - 3 PM": [],
#     "3 PM - 6 PM": [
#       "03:20 PM",
#       "03:30 PM",
#       "03:40 PM",
#       "03:50 PM",
#       "04:00 PM",
#       "04:10 PM",
#       "04:20 PM",
#       "04:30 PM",
#       "04:40 PM",
#       "04:50 PM",
#       "05:00 PM",
#       "05:10 PM",
#       "05:20 PM",
#       "05:30 PM",
#       "05:40 PM",
#       "05:50 PM"
#     ],
#     "6 PM - 9 PM": [
#       "06:00 PM",
#       "06:10 PM",
#       "06:20 PM",
#       "06:30 PM",
#       "06:40 PM",
#       "06:50 PM",
#       "07:00 PM",
#       "07:10 PM",
#       "07:20 PM",
#       "07:30 PM",
#       "07:40 PM",
#       "07:50 PM"
#     ],
#     "After 9 PM": []
#   }
# ]