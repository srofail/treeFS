from leg import Leg

class Journey:

    def __init__(self, data: dict):
        self.data = data
        self.legs = []
        self.parse_journey(data)

    def parse_journey(self, data):
        for leg_json in data["legs"]:
            self.legs.append(Leg(leg_json))
        return