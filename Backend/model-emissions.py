from leg import Leg

class Emissions:
    def __init__(self, leg: "Leg"):
        self.distance = distance # in km
        self.model = model # to check for zero emissions
        self.stops = stops
        self.people = self.get_people()
        self.zero = self.isZeroEmissions()

    def isZeroEmissions(self):
        # look through zero emissions list
        return False
        
    def get_emissions(self) -> float:
        # returns mass of co2 (kg) per person and greenhouse gases
        # Based on Australian Design Rule 80/04 – Emission Control for Heavy Vehicles
        if self.zero:
            return 0
        stop_frequency = self.stops / self.distance
        co2_kg_per_km = (0.161 + 0.0584 * stop_frequency) * 2.68
        co2_kg = co2_kg_per_km * self.distance
        return co2_kg / self.people
        
    def get_tree_days(self):
        # Based on estimates from EcoTree Group
        TREE_YEAR = 25
        co2_kg = self.get_emissions()
        return 365 * co2_kg / TREE_YEAR