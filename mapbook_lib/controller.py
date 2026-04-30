
def read_data(users_data: list)-> None:
    for user in users_data:
         print(
             f'twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')


def add_user(users_data: list) -> None:
    name = input('Podaj imię: ')
    location = input('Podaj lokalizację: ')
    posts = int(input('Podaj liczbę postów: '))
    usermessage = ['']
    users_data.append({'username': name, 'location': location, 'posts': posts,
                       'usermessage': usermessage}, )