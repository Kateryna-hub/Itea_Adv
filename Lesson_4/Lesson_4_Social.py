from datetime import date


class Authorization:
    list_of_users = [{'Surname': 'Petrov', 'login': 'ivan123', 'password': '1Qaz@wsx', 'data': '', 'access': 'admin'},
                     {'Surname': 'Popov', 'login': 'Peta1', 'password': '1Qaz@wsx', 'data': '', 'access': 'user'},
                     {'Surname': 'Ivanov', 'login': '123Ivanov_I', 'password': '1Qaz@wsx', 'data': '', 'access': 'user'}
                     ]
    posts = []
    log_on = ['OFF', '']

    def __init__(self, surname, login, password, access, today=date.today()):
        self.today = today
        self.surname = surname
        self.login = login
        self.password = password
        self.access = access

    def registration(self):
        login = self.check_login(self.list_of_users)
        password = self.check_password()
        self.list_of_users.append({'name': self.surname, 'login': login[0], 'password': password[0],
                                   'date': self.today, 'access': 'user'})
        print('Successful')

    def authentication(self):
        self.login = input('Enter LOGIN: ')
        self.password = input('Enter password: ')
        for dict_ in self.list_of_users:
            if dict_.get('login') == self.login and dict_.get('password') == self.password:
                print('Welcome')
                self.log_on = ['ON', dict_.get('login')]
                print(self.log_on)
        return self.log_on

    @staticmethod
    def check_password():
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
                        if len(_password)-1 >= 10:
                            flag_password = '1'
                        else:
                            print('password must contain 10 or more sybbols')
                    else:
                        print('password must contain the special symbol')
                else:
                    print('password must contain the letter')
            else:
                print('password must contain the number')
        return _password

    @staticmethod
    def check_login(list_of_users):
        login = input('Enter LOGIN: ')
        for dict_ in list_of_users:
            while dict_.get('login') == login:
                print('This login already exists.')
                login = input('Enter LOGIN: ')
        return login

 #   @property


class User(Authorization):

    def __init__(self, surname = '', login = '', password = '', today = date.today(), access = 'User'):
        super(User, self).__init__(surname, login, password, today)
        #self.name = name
        self.access = access


class Post(Authorization):
    key_status = 0
    key_login = 1

    def __init__(self, surname = '', login = '', password = '', today = '', post_title = '', content = '', access = ''):
        super(Post, self).__init__(surname, login, password, today)
        self.post_title = post_title
        self.content = content
        self.access = access

    def create_post(self):
        print(self.log_on)
        if self.log_on[self.key_status] == 'ON':
            self.login = self.log_on[self.key_login]
            self.post_title = input('Enter title og POST: ')
            self.content = input('Enter content: ')
            self.today = date.today()
            self.posts.append({'user': self.login, 'title': self.post_title, 'content': self.content,
                               'data created': self.today})
        else:
            print('You are not logged ON')

    def view_posts(self):
        if self.log_on[self.key_status] == 'ON':
            for dict_ in self.list_of_users:
                if dict_.get('login') == self.key_login and dict_.get('access') == 'admin':
                    for post in self.posts:
                        print('{] {} {} {}'.format(dict_.get('user'), dict_.get('title'),
                                                   dict_.get('content'), dict_.get('data created')))
                elif dict_.get('login') == self.key_login and dict_.get('access') == 'user':
                    for post in self.posts:
                        if post.get('user') == self.key_login:
                            print('{] {} {} {}'.format(dict_.get('user'), dict_.get('title'),
                                                       dict_.get('content'), dict_.get('data created')))
                else:
                    print('You haven`t published a post yet')


user = User()
#user.registration()
user.authentication()
print(Post.posts)
post = Post()
post.create_post()


# Post.view_posts()
#print(Authorization.list_of_users)





