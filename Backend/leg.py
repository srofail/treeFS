import requests
import json
import re

class Leg:

    def __init__(self, json):
        self.mode = json["transportation"]["product"]["class"]
        if self.mode in [99,100,107]:
            self.id = 0
            self.live_data = None
            self.duration = int(json["duration"])
            self.distance = 1
            self.model = ""
            self.departureTime = json["origin"]["departureTimeEstimated"]
            self.stops = 20
            self.origin = ""
            self.destination = ""
            self.occupancy_status = ""
            self.name = ""
            return
        
        try:
            self.id = json["transportation"]["properties"]["RealtimeTripId"]
        except KeyError:
            self.id = 0
        self.live_data = self.get_live_data()
        self.duration = int(json["duration"])
        self.distance = 1 # TODO: figure out
        self.model = self.find_model_name()
        self.departureTime = json["origin"]["departureTimeEstimated"]
        self.stops = 20 # TODO: figure out
        self.origin = json["origin"]["name"]
        self.destination = json["destination"]["name"]
        self.occupancy_status = self.find_occupancy()
        self.name = json["transportation"]["disassembledName"]

    def find_model_name(self):
        if self.live_data == None or self.id == 0:
            return "Unknown"
        
        return self.live_data["vehicle"]["vehicle"]["[transit_realtime.tfnsw_vehicle_descriptor]"]["vehicle_model"] 

    def find_occupancy(self):
        if self.live_data == None or self.id == 0:
            return 1
        
        print(self.live_data["vehicle"]["occupancy_status"])
        
        return self.live_data["vehicle"]["occupancy_status"]

    def get_live_data(self):
        if self.id == 0:
            return
        if self.mode != 5:
            return
        
        fobj = open("API_KEY", "r")
        api_key = fobj.readline()
        fobj.close()
        buses_url = 'https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/buses'

        headers = {
            "Authorization": api_key,

            "Accept": "application/json"
        }

        params = {
            'debug': 'true',
        }

        buses_response = requests.get(buses_url, params=params, headers=headers)

        final = None

        text = buses_response.text
        try:
            data = buses_response.json()
        except Exception:
            enum_value_after_colon = re.compile(r'(?<=:\s)([A-Z][A-Z0-9_]*)(?=\s*[\],}])')
            fixed = enum_value_after_colon.sub(r'"\1"', text)
            try:
                data = json.loads(fixed)
            except Exception:
                items = []
                for ln in text.splitlines():
                    s = enum_value_after_colon.sub(r'"\1"', ln)
                    s = s.strip()
                    if not s:
                        continue
                    try:
                        items.append(json.loads(s))
                    except Exception:
                        pass
                data = items

        if isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list):
            data = []

        for bus in data:
            if bus["vehicle"]["trip"]["trip_id"] == self.id:
                final = bus
        
        return final

