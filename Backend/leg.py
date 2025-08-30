import requests

class Leg:

    def __init__(self, json):
        self.id = json["transportation"]["properties"]["RealtimeTripID"]
        self.mode = json["transportation"]["product"]["id"]
        self.live_data = self.get_live_data()
        self.duration = json["duration"]
        self.distance = 1 # TODO: figure out
        self.model = self.find_model_name()
        self.departureTime = json["origin"]["departureTimeEstimated"]
        self.stops = "" # TODO: figure out
        self.origin = json["origin"]["name"]
        self.destination = json["destination"]["name"]
        self.occupancy_status = self.find_occupancy()
        self.name = json["transportation"]["name"]

    def find_model_name(self):
        if self.live_data == None:
            return "Unknown"
        
        return self.live_data["vehicle"]["vehicle"]["[transit_realtime.tfnsw_vehicle_descriptor]"]["vehicle_model"] 

    def find_occupancy(self):
        if self.live_data == None:
            return "Unknown"
        
        return self.live_data["vehicle"]["occupancy_status"]

    def get_live_data(self):
        if self.mode != 5:
            return
        
        fobj = open("API_KEY", "r")
        api_key = fobj.readline()
        fobj.close()
        buses_url = 'https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/buses'

        headers = {
            "Authorization": api_key
        }

        params = {
            'debug': 'true',
        }

        buses_response = requests.get(buses_url, params=params, headers=headers)

        final = None

        for bus in buses_response.json():
            if bus["vehicle"]["trip"]["trip_id"] == self.id:
                final = bus
        
        return final

