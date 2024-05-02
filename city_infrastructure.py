#   Task 1:

#   Create a Python class Vehicle with attributes: registration_number, type, and owner.
#   Implement a method update_owner to change the vehicle's owner.
#   Then create a few instances of Vehicle and demonstrate changing the owner.

# class Vehicle:
#   def __init__(self, reg_num, type, owner):
#       self.registration_number = reg_num
#       self.type = type
#       self.owner = owner




#   Create a Python class Vehicle with attributes: registration_number, type, and owner.
class Vehicle():
    def __init__(self, reg_number, type, owner):
        self.registration_number = reg_number
        self.type = type
        self.owner = owner 


#   Implement a method update_owner to change the vehicle's owner.
    def update_owner(self, new_owner):
        print(f'Ownership will be transferred from {self.owner} to {new_owner}')
        self.owner = new_owner


#   Then create a few instances of Vehicle and demonstrate changing the owner.
    def get_info(self):
        print(f'{self.owner} now owns a {self.type}, and its registration number is {self.registration_number}')
    

Owner = Vehicle(reg_number='777-007', type='Tesla Roadster', owner='Elon Musk')

Owner.get_info()




#   Task 2:


#   Extend an existing Event class by adding an attribute to keep track of the number of participants.
#   Implement a method add_participant that increases the count,
#   and a method get_participant_count to retrieve the current count.


#   Extend an existing Event class by adding an attribute to keep track of the number of participants.
class Event():
    def __init__(self, name, date, participants, count):
        self.name = name
        self.date = date
        self.participants = participants
        self.count = count

#   Implement a method add_participant that increases the count,
    def add_participant(self):
        print(f'pass')

   #   and a method get_participant_count to retrieve the current count.
    def get_participant_count(self):
        print()
        
   #    Summary
    def new_participant(self, name, date):
        print(f'{self.participants} increases by {self.count} from adding {self.name} to the list')


new_participant1 = Event(name='Han Solo', date='May 4th', participant= '1', count='+1')
new_participant2 = Event(name='', date='', participant= '2', count='+1')
new_participant3 = Event(name='', date='', participant= '3', count='+1')

new_participant1.add_participant()
new_participant2.add_participant()
new_participant3.add_participant()