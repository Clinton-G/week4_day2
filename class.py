

#   email, username, password

class User():
    #class_attribute = pass

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
    
#   Methods:
    def user_contact(self):
        print(f'{self.username} can be contacted at {self.email}')



WforWumbo = User(email='wumbo@email.com', username='wumbology', password='wstandsforwumbology')

WforWumbo.get_info()