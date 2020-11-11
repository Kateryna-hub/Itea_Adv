from datetime import date


class Authorization:
    list_of_users = [{'Surname': 'Petrov', 'login': 'ivan123', 'password': '1Qaz@wsx', 'data': ''},
                     {'Surname': 'Popov', 'login': 'Petya1', 'password': '1Qaz@wsx', 'data': ''},
                     {'Surname': 'Ivanov', 'login': '123Ivanov_I', 'password': '1Qaz@wsx', 'data': ''}
                     ]

    def __init__(self, surname, today=date.today()):
        self.today = today
        self.surname = surname
        self.flag_login = False
        self.flag_password = False

    def registration(self):
        new_login = input('Enter LOGIN: ')
        login = self.check_login(new_login, self.list_of_users)
        new_password = input('Enter password: ')
        confirm_password = input('Confirm password: ')
        if new_password == confirm_password:
            password_ = self.check_password(new_password)
            print(password_)
        else:
            print('passwords are not the same')
            password_ = None
            self.flag_login = '2'
        if login[1] == '1' and password_[1] == '1':
            self.list_of_users.append({'name': self.surname, 'login': login[0], 'password': password_[0], 'date': self.today})
            print('Successful')
        else:
            print('sorry for inconvenience')

    def authentication(self):
        pass

    @staticmethod
    def check_password(password):
        numbers = str('0123456789')
        symbols_ = str('!@#$%^&*()_+-=<>,.?/{}[]')
        while True:
            if password != '1':
                for letter in password:
                    if letter not in '0123456789':
                        print('password must contain the number')
                    elif letter not in "!@#$%^&*()_-+=<>,.?/{}[]":
                        print('password must contain the special symbol')
                else:
                    flag_password = '1'
            else:
                break
            return password, flag_password

    @staticmethod
    def check_login(login, list_of_users):
        for dict_ in list_of_users:
            if dict_.get('login') == login:
                print('This login already exists.')
                flag_login = '2'
            else:
                flag_login = '1'
        return login, flag_login


class User(Authorization):

    def __init__(self, surname, today = date.today(), access = None ):
        super(User, self).__init__(surname, today)
        #self.name = name
        self.access = access


class Post:

    def __init__(self, post_name, content, user_name, date_publication):
        self.post_name = post_name
        self.content = content
        self.user_name = user_name
        self.date_publication = date_publication

    def create_post(self):
        pass

    def view_post(self):
        pass



user = User('John')
user.registration()
print(Authorization.list_of_users)





