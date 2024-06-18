class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.name},{self.floors}\n")
        print(f"Building '{self.name}' saved to file '{filename}'.")

    @staticmethod
    def load_from_file(filename):
        buildings = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, floors = line.strip().split(',')
                    building = Building(name, int(floors))
                    buildings.append(building)
                    
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

        return buildings


    def __repr__(self):
        return f"Building(name='{self.name}', floors={self.floors})"


building1 = Building(name='Empire State Building', floors=250)
building2 = Building(name='Burj Khalfa', floors=100)
building3 = Building(name='Eiffel Tower', floors=25)


filename = 'buildings.txt'


building1.save_to_file(filename)
building2.save_to_file(filename)
building3.save_to_file(filename)


loaded_buildings = Building.load_from_file(filename)


print("\nLoaded buildings from file:")
for building in loaded_buildings:
    print(building)
