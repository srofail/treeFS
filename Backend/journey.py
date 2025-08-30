from leg import Leg
from emissions import Emissions

class Journey:

    def __init__(self, data: dict):
        self.data = data
        self.legs = []
        self.parse_journey(data)

    def parse_journey(self, data):
        for leg_json in data["legs"]:
            self.legs.append(Leg(leg_json))

        co2 = 0
        for leg in self.legs:
            emissions = Emissions(leg)
            co2 += emissions.get_emissions()
        print(f"\n\n\n\n\nThis trip emits {co2*1000} grams of CO\u2082\n\n\n\n\n\n")
        return