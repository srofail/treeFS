from leg import Leg
from emissions import Emissions

class Journey:

    def __init__(self, data: dict):
        self.data = data
        self.legs = []
        self.co2 = 0
        self.duration = 0
        self.trees = 0
        self.departure_time = "XX:XX"
        self.parse_journey(data)

    def small_present_format(self):
        result = []
        result.append(self.duration // 60)
        result.append(10)
        result.append(self.departure_time)
        result.append(int(self.co2 * 1000))
        result.append(int(self.trees))
        
        routes = []
        for leg in self.legs:
            route = []
            route.append(leg.mode)
            route.append(leg.name)
            routes.append(route)

        result.append(routes)
        
        return result
        

    def parse_journey(self, data):
        for leg_json in data["legs"]:
            self.legs.append(Leg(leg_json))

        self.duration = 0
        for leg in self.legs:
            self.duration += leg.duration
            print(f"This leg has duration {leg.duration}")

        self.co2 = 0
        self.trees = 0
        for leg in self.legs:
            emissions = Emissions(leg)
            self.co2 += emissions.get_emissions()
            self.trees += emissions.get_tree_days()
        print(f"This trip emits {self.co2*1000} grams of CO\u2082")

        self.departure_time = self.legs[0].departureTime[11:16]
        print("FHDJISOIUYFGDHSK", self.departure_time)
        self.departure_time = Journey.gmt_to_aest(self.departure_time)
        print(self.legs[0])
        return
    
    def gmt_to_aest(time: str):
        hours = int(time[0:2])
        print("GFHJKSHGFHJKSDJ ", hours)
        hours = (hours + 10) % 24
        time_2 = str(hours) + time[2:]
        return time_2