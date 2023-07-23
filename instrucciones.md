Definir 3 clases: User, Post, Article

Definir en cada clase un método (save) que permita guardar los datos de la instancia en el archivo respectivo (users.json, posts.json, articles.json)

users.json -> Contiene una lista de usuarios
posts.json -> Contiene una lista de posts
articles.json -> Contiene una lista de artículos

Resultado esperado:
user = User("Alfredo", "Altamirano")

user.save() -> Guarde los datos del usuario en users.json

Como referencia:
User
    first_name
    last_name
    username
    password
    email
    
Article
    title
    content
    status
    image
    created_by
    
Comments
    content
    created_by
    article