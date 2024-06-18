class Bus:
    city = "New York City"
    base_fare = 5.00

    def __init__(self, route_number, passenger_capacity):
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity

    def get_route_info(self):
        return f"Route {self.route_number} - City: {Bus.city}, Base Fare: ${Bus.base_fare}, Capacity: {self.passenger_capacity}"


bus1 = Bus(route_number='101', passenger_capacity=50)
bus2 = Bus(route_number='102', passenger_capacity=25)

print('City:', Bus.city, 'Base Fare:', Bus.base_fare)

print("\nBus 1:")
print(bus1.get_route_info())

print("\nBus 2:")
print(bus2.get_route_info())
