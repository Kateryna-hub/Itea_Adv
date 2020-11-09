class Authorization:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def registration(self):
        pass

    def authentication(self):
        pass

    def password_validation(self):
        pass

    def check_login(self):
        pass


class User(Authorization):

    def __init__(self, login, password, name, surname, date_registration, access):
        super(User, self).__init__(login, password)
        self.name = name
        self.surname = surname
        self.date_registration = date_registration
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



