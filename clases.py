from datetime import date

class User:
    race = 'Human'


    # dunder: double underscore
    def __init__(self, first_name, last_name, brth_date, username, password = '123', email) -> None:
        self.username = username
        self.name = name
        self.last_name = last_name
        self.password = password
    
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

# class: PascalCase
# vars: snake_case
# const: UPPER_SNAKE_CASE

# User
# Post
# Comments