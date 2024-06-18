class Vehicle:
    def __init__(self, reg_number, vehicle_type, owner):
        self.registration_number = reg_number
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        print('Ownership will be transferred from', self.owner, 'to', new_owner)
        self.owner = new_owner

    def get_info(self):
        print(self.owner, 'now owns a', self.type, 'and its registration number is', self.registration_number)

car1 = Vehicle(reg_number='777-007', vehicle_type='Tesla Roadster', owner='Elon Musk')
car2 = Vehicle(reg_number='123-ABC', vehicle_type='Ford Mustang', owner='John Doe')

car1.get_info()
car2.get_info()

car1.update_owner('Michael Scott')
car2.update_owner('Jane Doe')

car1.get_info()
car2.get_info()


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
        print('Adding participants. Total Participants:', self.participant_count)

    def get_participant_count(self):
        print(f"Current participant count: {self.participant_count}")
        return self.participant_count


event1 = Event(name='Tech Conference', date='2024-06-20')
event2 = Event(name='Music Festival', date='2024-07-10')

print('Event:', event1.name, 'on', event1.date)
event1.add_participant()
event1.add_participant()
event1.add_participant()

event1.get_participant_count()

print('Event:', event2.name, 'on', event2.date)
event2.add_participant()

event2.get_participant_count()
