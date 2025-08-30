import requests
import time
from datetime import datetime
from journey import Journey

class Backend:

    def __init__(self):
        return
    
    def valid_journey(self):
        return True
    
    def get_journeys(self, origin_lat, origin_long, dest_lat, dest_long):
        API_ENDPOINT = "https://api.transport.nsw.gov.au/v1/tp/"
        API_CALL = "trip"

        when = int(time.time())

        origin_coord = f"{origin_long:.6f}:{origin_lat:.6f}:EPSG:4326"
        dest_coord = f"{dest_long:.6f}:{dest_lat:.6f}:EPSG:4326"

        params = {
            "outputFormat": "rapidJSON",
            "coordOutputFormat": "EPSG:4326",
            "depArrMacro": "dep",
            "itdDate": datetime.fromtimestamp(when).strftime("%Y%m%d"),
            "itdTime": datetime.fromtimestamp(when).strftime("%H%M"),
            "type_origin": "coord",
            "name_origin": origin_coord,
            "type_destination": "coord",
            "name_destination": dest_coord,
            "TfNSWTR": "true"
        }

        fobj = open("API_KEY", "r")
        api_key = fobj.readline()
        headers = {
            "Authorization": api_key
        }

        response = requests.get(API_ENDPOINT + API_CALL, params=params, headers=headers)

        journeys = []

        for json in response.json["journeys"]:
            journeys.append(Journey(json))

        return
