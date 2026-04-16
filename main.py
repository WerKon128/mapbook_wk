users: list = [
    {'username': 'Oliwia', 'location': 'Łódź', 'posts': 1,
     'usermessage': ['życzenia1', 'kocham legie1', 'sprzedam opla1', 'kiwi1']},
    {'username': 'Paweł', 'location': 'Ostróda', 'posts': 1,
     'usermessage': ['życzenia2', 'kocham legie2', 'sprzedam opla2']},
    {'username': 'Elizka', 'location': 'Łódź', 'posts': 1, 'usermessage': ['życzenia3', 'kocham legie3']},
    {'username': 'Filip', 'location': 'Dęblin', 'posts': 1,
     'usermessage': ['życzenia4', 'kocham legie4', 'sprzedam opla4', 'kiwi4']},
]


def read_data(users_data: list)-> None:

    for user in users_data:
         print(
             f'twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')


read_data(users[1:])
