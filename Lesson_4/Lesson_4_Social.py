from datetime import datetime
import sys
from abc import ABC, abstractmethod


class AuthorizationMixin:

    _list_of_users = [{'Surname': 'Petrov', 'login': 'ivan123', 'password': '1Qaz@wsx', 'data': '2020-11-10 23:22:21'}]
    _posts = [{'user': 'Petro1', 'title': 'post1', 'content': 'some kind of text', 'data created': '2020-11-12 20:45:21'}]

    def registration(self):
        surname = input('Enter Surname: ')
        today = datetime.now()
        login = input('Enter login: ')
        for dict_ in self._list_of_users:
            if dict_.get('login') == login:
                print('LOGIN already exist')
                self.registration()
            else:
                password = self.password_valid()
                self._list_of_users.append({'Surname': surname, 'login': login, 'password': password[0],
                                            'date': today})
                print('Successful')
            return login

    def authentication(self):
        login = input('Enter LOGIN: ')
        password = input('Enter password: ')
        for dict_ in self._list_of_users:
            if dict_.get('login') == login and dict_.get('password') == password:
                self.sign_on = 1
                print('Welcome\n')
            if dict_.get('login') == login and dict_.get('password') != password:
                print('password is wrong')
                self.authentication()
            if dict_.get('login') != login and dict_.get('password') != password:
                print('There is not such user\n')
                next_step = input('to repeat LOG ON press "1"\n'
                                  'for REGISTRATION PRESS "2"\n'
                                  'or press "q" for EXIT: ')
                if next_step == '1':
                    self.authentication()
                if next_step == '2':
                    self.registration()
                    print('Now you can LOG ON ')
                    self.authentication()
                if next_step == 'q':
                    sys.exit(0)
        return self.sign_on

    def log_out(self):
        self.sign_on = 0
        return self.sign_on

    @staticmethod
    def password_valid():
        _password = ''
        flag_password = '2'
        while flag_password == '2':
            _password = input('Enter password: ')
            confirm_password = input('Confirm password: ')
            while _password != confirm_password:
                print('The passwords are not the same')
                _password = input('Enter new password: ')
                confirm_password = input('Confirm password: ')
            if any(map(str.isdigit, _password)):
                if any(map(str.isalpha, _password)):
                    if not _password.isalnum():
                        if len(_password) >= 10:
                            flag_password = '1'
                        else:
                            print('password must contain 10 or more symbols')
                    else:
                        print('password must contain the special symbol')
                else:
                    print('password must contain the letter')
            else:
                print('password must contain the number')
        return _password


class Post(ABC):

    @abstractmethod
    def create_post(self):
        pass


class User(AuthorizationMixin, Post):

    sign_on = 0
    is_admin = 0

    def __init__(self, surname='', login='', password='', today=datetime.now()):
        super().__init__()
        self.surname = surname
        self.login = login
        self.password = password
        self.today = today

    def view_user(self):
        if self.sign_on == 1:
            if self.is_admin == 1:
                for dict_ in self._list_of_users:
                    print('{} {} {}'.format(dict_.get('Surname'), dict_.get('login'), dict_.get('data')))
            else:
                print('You haven`t permission')
        else:
            print('You haven`t signed on yet')

    def view_posts(self):
        if self.sign_on == 1:
            if self.is_admin == 1:
                for post_ in self._posts:
                    print('{} {} {} {}'.format(post_.get('user'), post_.get('title'),
                                               post_.get('content'), post_.get('data created')))
            else:
                print('You haven`t permission')
        else:
            print('You haven`t signed on yet')

    # @property
    # def login(self):
    #     return self.login

    def set_admin_permission(self, value):
        self.is_admin = 1
        return self.is_admin

    def create_post(self):
        if self.sign_on == 1:
            login = self.login
            post_title = input('Enter title og POST: ')
            content = input('Enter content: ')
            today = datetime.now()
            self._posts.append({'user': login, 'title': post_title, 'content': content,
                                'data created': today})


user1 = User()
user1.authentication()
user1.set_admin_permission(1)
user1.create_post()
user1.view_posts()
user2 = User()
user2.registration()
user2.create_post()
user2.view_user()
user2.view_posts()
user1.view_posts()
user1.view_user()
user1.log_out()
user1.view_user()








