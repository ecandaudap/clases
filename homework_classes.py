import os
import json

class User:
    def __init__(self, first_name, last_name, username, password = '123') -> None:
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
  
    def save(self):
       
       dict_user = {
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password
        }
            
       file = open('users.json', 'w')
       file.write(json.dumps(dict_user))
       file.close()

class Article:
    def __init__(self, title, content, status, image, created_by) -> None:
        self.title = title
        self.content = content
        self.status = status
        self.image = image
        self.created_by = created_by
 
    def save(self):
       
       dict_user = {
            'title': self.title,
            'content': self.content,
            'status': self.status,
            'image': self.image,
            'created_by' : self.created_by
        }
            
       file = open('articles.json', 'w')
       file.write(json.dumps(dict_user))
       file.close()

class Post:
    def __init__(self, comments, content, created_by, article) -> None:
        self.comments = comments
        self.content = content
        self.created_by = created_by
        self.article = article
  
    def save(self):
       
       dict_user = {
            'comments': self.comments,
            'content': self.content,
            'created_by': self.created_by,
            'article': self.article
        }
            
       file = open('posts.json', 'w')
       file.write(json.dumps(dict_user))
       file.close()
       
user1 = User('alfredoa','Alfredo', 'Altamirano', 'asdfghjkl')
user2 = User('ecandaudap', 'Eduardo', 'Candaudap')

article1 = Article('Hands-On Machine Learning', 'Data Science', 'Finished', 'None', 'Aurélien Géron')
article2 = Article('Economics today', 'Economics', 'In process', 'None', 'Various')

post1 = Post('Great article', 'Data Science', 'Aurélien Géron', 'Hands-On Machine Learning')
post2 = Post('It is not so good','Economics', 'Various', 'Economics today')


user1.save()
article1.save()
post2.save()


#print(alfredo.first_name, alfredo.race)
#print(francisco.first_name, francisco.race)
