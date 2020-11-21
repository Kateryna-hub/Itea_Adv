from datetime import datetime
import shelve

FILE_USERS = 'Users'
FILE_POSTS = 'Posts'


def shelve_choose_file(file_name):

    def shelve_required(func):

        def wrapper(*args, **kwargs):
            with shelve.open(file_name) as db:
                result = func(*args, **kwargs)
                return result

        return wrapper
    return shelve_required()


def add_obj_to_file(file_name, key_name, value):

    with shelve.open(file_name) as db:
        db[key_name] = value


def set_key_name(file_name, name):

    with shelve.open(file_name) as db:
        key_name = name + str(len(db)+1)
        return key_name


def get_key_file(file_name, key_name):

    with shelve.open(file_name) as db:
        return db.get(key_name, 'There is no such user in the database')


class AuthorizationMixin:

    def __init__(self, sign_on=False, login='', is_admin=False):
        self.sign_on = sign_on
        self.login = login
        self.is_admin = is_admin

    @staticmethod
    def check_login(login):
        key_name = None
        with shelve.open(FILE_USERS) as db:
            for key in db:
                login_ = (db.get(key)).get('login')
                if login_ == login:
                    key_name = key
        return key_name

    @staticmethod
    def password_valid(_password, _confirm_password):
        flag_password = False
        while not flag_password:
            if _password == _confirm_password:
                if any(map(str.isdigit, _password)):
                    if any(map(str.isalpha, _password)):
                        if not _password.isalnum():
                            if len(_password) >= 10:
                                flag_password = True
                            else:
                                print('password must contain 10 or more symbols')
                        else:
                            print('password must contain the special symbol')
                    else:
                        print('password must contain the letter')
                else:
                    print('password must contain the number')
            else:
                print('The passwords are not the same')
        return flag_password

    def registration(self, surname, login, password, confirm_password, key_name=set_key_name(FILE_USERS, 'user')):
        today = datetime.now().strftime('%d.%m.%Y %H:%m')
        check = self.check_login(login)
        if check is None:
            check_password = self.password_valid(password, confirm_password)
            if check_password:
                dict_ = {'Surname': surname, 'login': login, 'password': password, 'date': today, 'is_admin': False}
                add_obj_to_file(FILE_USERS, key_name, dict_)
                result = True
            else:
                result = False
        else:
            print('login already exist')
            result = False
        return result

    def authentication(self, login, password):
        key_name = self.check_login(login)
        dict_ = get_key_file(FILE_USERS, key_name)
        if dict_.get('login') == login and dict_.get('password') == password:
            self.sign_on = True
            self.login = login
            self.is_admin = dict_.get('is_admin')
            print('Welcome\n')
        else:
            print('password is wrong')
            self.sign_on = False
        return self.sign_on, self.login, self.is_admin

    def log_out(self):
        self.sign_on = False
        return self.sign_on


class User(AuthorizationMixin):

    def __init__(self):
        super().__init__()

    def view_user(self):
        if self.sign_on:
            if self.is_admin:
                print('{} {} {}'.format('Surname', 'login', 'date_created'))
                with shelve.open(FILE_USERS) as db:
                    for key in db:
                        dict_ = db.get(key)
                        print('{} {} {} {} {}'.format(dict_.get('Surname'), dict_.get('login'), dict_.get('password'),
                                                      dict_.get('date'), dict_.get('is_admin')))
            else:
                print('You haven`t permission')
        else:
            print('You haven`t signed on yet')

    def view_posts(self):
        if self.sign_on:
            if self.is_admin:
                with shelve.open(FILE_POSTS) as db:
                    for key in db:
                        dict_ = db.get(key)
                        print('{} {} {} {}'.format(dict_.get('user'), dict_.get('title'),
                                                   dict_.get('content'), dict_.get('date_created')))
            else:
                print('You haven`t permission')
        else:
            print('You haven`t signed on yet')

    def save_post(self, post_, key_name=set_key_name(FILE_POSTS, 'post')):
        if self.sign_on:
            title = post_['title']
            content = post_['content']
            today = datetime.now().strftime('%d.%m.%Y %H:%m')
            dict_post = {'user': self.login, 'title': title, 'content': content, 'date_created': today}
            add_obj_to_file(FILE_POSTS, key_name, dict_post)

        else:
            print('You haven`t signed on yet')

    def set_admin_permission(self, user_login, access=True):
        if self.sign_on:
            if self.is_admin:
                with shelve.open(FILE_USERS, writeback=True) as db:
                    for key in db:
                        dict_ = db.get(key)
                        if dict_.get('login') == user_login:
                            dict_['is_admin'] = access
            else:
                print('You haven`t permission')
        else:
            print('You haven`t signed on yet')


class Post:

    def __init__(self, title='', content='', date_created=''):
        self.title = title
        self.content = content
        self.date_created = date_created

    def create_post(self, title='', content=''):
        dict_ = {'title': title, 'content': content}
        return dict_


user1 = User()
user2 = User()
user2.registration(surname=input('Enter Surname: '), login=input('Enter Login: '),
                   password=input('Enter password: '), confirm_password=input('Enter password: '))
user1.authentication(login=input('Enter Login: '), password=input('Enter password: '))
user1.set_admin_permission(user_login=input('Enter user: '), access=True)
user1.view_user()
user2.view_user()
user2.authentication(login=input('Enter Login: '), password=input('Enter password: '))
user2.view_user()
post = Post()
post1 = post.create_post(title=input('Enter title: '), content=input('Enter text: '))
user2.save_post(post1)
user1.view_posts()



