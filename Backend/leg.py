import requests

class Leg:

    def __init__(self, json):
        self.id = json["transportation"]["properties"]["RealtimeTripID"]
        self.mode = json["transportation"]["product"]["id"]
        self.live_data = self.get_live_data()
        self.duration = json["duration"]
        self.distance = 1 # TODO: figure out
        self.model = "" # TODO: figure out
        self.departureTime = json["origin"]["departureTimeEstimated"]
        self.stops = "" # TODO: figure out
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

        headers = {
            'accept': 'application/x-google-protobuf',
            'Authorization': 'apikey eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJFLUVFaEtfSkxGckdtcDdDUmlCcE03LWY3bldDakZxSVV3YXdEM1FCbS1ZIiwiaWF0IjoxNzU2NTI3OTQ4fQ.JSlweOlbpsW9fmVEZ3iqIMMlUFo76S_iGDrRVnX7HrY',
        }

        params = {
            'debug': 'true',
        }

        buses_response = requests.get(buses_url, params=params, headers=headers)
        
        return buses_response

