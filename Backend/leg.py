import requests

class Leg:

    def __init__(self, json):
        self.mode = json["transportation"]["product"]["class"]
        if self.mode in [99,100,107]:
            self.id = 0
            self.live_data = None
            self.duration = 0
            self.distance = 1
            self.model = ""
            self.departureTime = ""
            self.stops = 20
            self.origin = ""
            self.destination = ""
            self.occupancy_status = ""
            self.name = ""
            return
        
        self.id = json["transportation"]["properties"]["RealtimeTripId"]
        self.live_data = self.get_live_data()
        self.duration = json["duration"]
        self.distance = 1 # TODO: figure out
        self.model = "" # TODO: figure out
        self.departureTime = json["origin"]["departureTimeEstimated"]
        self.stops = 20 # TODO: figure out
        self.origin = json["origin"]["name"]
        self.destination = json["destination"]["name"]
        self.occupancy_status = "" # TODO: figure out
        self.name = json["transportation"]["name"]

    def find_model_name(self):
        pass

    def find_occupancy(self):
        pass

    def get_live_data(self):
        if self.mode != 5:
            return
        
        fobj = open("API_KEY", "r")
        api_key = fobj.readline()
        buses_url = 'https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/buses'

        headers = {
            "Authorization": api_key
        }
        
        params = {
            'debug': 'true',
        }

        buses_response = requests.get(buses_url, params=params, headers=headers)
        
        return buses_response

