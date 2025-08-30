class Leg:

    def __init__(self, id, duration, distance, mode, model, departureTime, stops, origin, destination, occupancy_status):
        self.id = id
        self.duration = duration
        self.distance = distance
        self.mode = mode
        self.model = model
        self.departureTime = departureTime
        self.stops = stops
        self.origin = origin
        self.destination = destination
        self.occupancy_status = occupancy_status

