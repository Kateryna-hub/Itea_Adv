from datetime import date
import sys
from abc import ABC, abstractmethod


class Authorization(ABC):

    _list_of_users = [{'Surname': 'Petrov', 'login': 'ivan123', 'password': '1Qaz@wsx', 'data': ''}]

    def registration(self):
        surname = input('Enter login: ')
        login = input('Enter login: ')
        for dict_ in self._list_of_users:
            if dict_.get('login') == login:
                print('LOGIN already exist')
                self.registration()
            else:
                password = self.password_valid()
                self._list_of_users.append({'name': self.surname, 'login': login[0], 'password': password[0],
                                           'date': self.today, 'access': 'user', 'status': 'OFF'})
                print('Successful')
        return login

    def authentication(self):
        self.login = input('Enter LOGIN: ')
        self.password = input('Enter password: ')
        for dict_ in self._list_of_users:
            if dict_.get('login') == self.login and dict_.get('password') == self.password:
                self.is_logon = True
                print('Welcome\n')
            if dict_.get('login') == self.login and dict_.get('password') != self.password:
                print('password is wrong')
                self.authentication()
            if dict_.get('login') != self.login and dict_.get('password') != self.password:
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
        return self.is_logonrjy

    def log_out(self):
        pass

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


class User(Authorization):


    def __init__(self, surname='', login='', password='', today=date.today(), is_admin=False):
        super().__init__()
        self.surname = surname
        self.login = login
        self.password = password
        self.today = today
        self.is_admin = is_admin


class Post(User):
    key_status = 0
    key_login = 1
    posts = [{'user': 'Petro1', 'title': 'post1', 'content': 'some kind of text', 'data created': '2020-11-11'}]

    def __init__(self, surname='', login='', password='', today='', post_title='', content=''):
        super(Post, self).__init__(surname, login, password, today)
        self.post_title = post_title
        self.content = content


    def create_post(self):
        for dict_ in self._list_of_users:
            if dict_.get('status') == 'ON':
                self.login = status_[self.key_login]
                self.post_title = input('Enter title og POST: ')
                self.content = input('Enter content: ')
                self.today = date.today()
                self.posts.append({'user': self.login, 'title': self.post_title, 'content': self.content,
                                   'data created': self.today})
            else:
                print('You are not logged ON')

    def view_posts(self, status_):
        if status_[self.key_status] == 'ON':
            for dict_ in self._list_of_users:
                if dict_.get('login') == status_[self.key_login]:
                    if dict_.get('access') == 'admin':
                        for post_ in self.posts:
                            print('{} {} {} {}'.format(post_.get('user'), post_.get('title'),
                                                       post_.get('content'), post_.get('data created')))
                    if dict_.get('access') == 'user':
                        for post_ in self.posts:
                            if post_.get('user') == self.key_login:
                                print('{} {} {} {}'.format(post_.get('user'), post_.get('title'),
                                                           post_.get('content'), post_.get('data created')))
                    else:
                        print('You haven`t published a post yet')


user1 = User()
print(dir(user1))
post = Post()
print(dir(post))
# user2 = User()
# #user1.registration()
# logon1 = user1.authentication()
# post = Post()
# post.create_post(logon1)
# post.view_posts(logon1)
# print('-' * 10)
# logon2 = user1.authentication()
# post.view_posts(logon2)
# user1.create_post
# #print(Authorization.list_of_users)





