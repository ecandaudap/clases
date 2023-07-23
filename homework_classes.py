from datetime import date

class User:
    race = 'Human'


    # dunder: double underscore
    def __init__(self, first_name, last_name, username, password = '123', email) -> None:
        self.username = username
        self.girst_name = first_name
        self.last_name = last_name
        self.password = password

    def __str_(self) -> str:
        return f'{self.name} {self.last_name}'
    
    def save(self):
        user.json


    def as_dict(self):
        return {
            'username': self.username,
            'name': self.name,
            'last_name': self.last_name,
            'password': self.password
        }

user1 = User('alfredoa','Alfredo'.'Altamirano', 'asdfghjkl')
user2 = User('ecandaudap', 'Eduardo', 'Candaudap')


print(alfredo.first_name, alfredo.race)
print(francisco.first_name, francisco.race)
