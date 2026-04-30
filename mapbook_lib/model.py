users: list = [
    {'username': 'Oliwia', 'location': 'Łódź', 'posts': 1,
     'usermessage': ['życzenia1', 'kocham legie1', 'sprzedam opla1', 'kiwi1']},
    {'username': 'Paweł', 'location': 'Ostróda', 'posts': 2,
     'usermessage': ['życzenia2', 'kocham legie2', 'sprzedam opla2']},
    {'username': 'Elizka', 'location': 'Łódź', 'posts': 3, 'usermessage': ['życzenia3', 'kocham legie3']},
    {'username': 'Filip', 'location': 'Dęblin', 'posts': 4,
     'usermessage': ['życzenia4', 'kocham legie4', 'sprzedam opla4', 'kiwi4']},
]
def add_user(users_data: list)->None:

    print(users)
    name=input('Podaj imię: ')
    location=input('Podaj lokalizację: ')
    posts=int(input('Podaj liczbę postów'))
    usermessage=[]
    users.append( {'username': name, 'location': location, 'posts': posts,
         'usermessage': usermessage} ,)
    print(users)
add_user(users)