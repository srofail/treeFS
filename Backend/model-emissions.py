from leg import Leg

class Emissions:
    def __init__(self, leg: "Leg"):

        modeMap = {
            1: "Train",
            2: "Metro",
            4: "Light Rail",
            5: "Bus",
            7: "Coach",
            9: "Ferry",
            11: "School Bus",
            99: "Walk",
            100: "Walk",
            107: "Cycle"
        }

        self.distance = leg.distance # in km
        self.mode = modeMap[leg.mode] # mode of transport
        self.model = leg.model # to check for zero emissions
        self.stops = leg.stops
        self.people = self.get_people(leg)
        self.zero = self.isZeroEmissions()

    def isZeroEmissions(self):
        # check through zero emissions list

        zero_emissions_list = [
            "BYD",
            "Yutong",
            "Custom Denning"
        ]

        # Sydney Metro uses zero-emission electricity for 100 per cent of Metro North West Line
        # Sydney Metro | Sustainability Report 2023 pg. 16

        if self.Mode in ["Walk", "Cycle", "Metro", "Train", "Light Rail"]:
            return True
        if self.Mode == "Bus":
            for make in zero_emissions_list:
                if self.model.startswith(make):
                    return True
        return False
        
    def get_emissions(self) -> float:
        # returns mass of co2 (kg) per person and greenhouse gases
        # Based on Australian Design Rule 80/04 – Emission Control for Heavy Vehicles
        # and Climate Active Report on Transdev Sydney Ferries
        
        if self.zero:
            return 0
        if self.mode == "Ferry":
            return 0.371 * self.distance
        else:
            stop_frequency = self.stops / self.distance
            co2_kg_per_km = (0.161 + 0.0584 * stop_frequency) * 2.68
            co2_kg = co2_kg_per_km * self.distance
            return co2_kg / self.people
        
    def get_tree_days(self):
        # Based on estimates from EcoTree Group
        TREE_YEAR = 25
        co2_kg = self.get_emissions()
        return 365 * co2_kg / TREE_YEAR

    def get_people(leg: "Leg"):
        return leg.occupancy_status * 15;

'''
enum OccupancyStatus {
	EMPTY = 0;
	MANY_SEATS_AVAILABLE = 1;
	FEW_SEATS_AVAILABLE = 2;
	STANDING_ROOM_ONLY = 3;
	CRUSHED_STANDING_ROOM_ONLY = 4;
	FULL = 5;
  }

  mode / class:
  1: train
  2: metro
  4: Light Rail
  5: Bus
  7: Coach
  9: Ferry
  11: School Bus
  99: Walk
  100: walk
  107: Cycle
'''