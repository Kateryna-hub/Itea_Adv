import sqlite3


class DB:

    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.commit()
        self.cursor.close()


class AuthorizationMixin:

    def __init__(self, sign_on=False, login='', is_admin=False):
        self.sign_on = sign_on
        self.login = login
        self.is_admin = is_admin

    @staticmethod
    def get_user(login):
        with DB("students.db") as db:
            user = db.execute(* ('SELECT users.login, users.password, users.is_admin '
                                 'FROM users WHERE users.login = ?', (login,)))
            return user.fetchone()

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

    def registration(self, login, password, confirm_password, is_admin='False'):
        check = self.get_user(login)
        if check is None:
            check_password = self.password_valid(password, confirm_password)
            if check_password:
                create_user = ('INSERT INTO users (login, password, is_admin) '
                               'VALUES (?, ?, ?)', (login, password, is_admin))
                with DB("students.db") as db:
                    db.execute(* create_user)
                result = True
            else:
                result = False
        else:
            print('login already exist')
            result = False
        return result

    def authentication(self, login, password):
        user = self.get_user(login)
        if user[0] == login and user[1] == password:
            self.sign_on = True
            self.login = login
            self.is_admin = user[2]
            print(f'{login} Welcome\n')
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

    def list_of_students(self):
        list_studs = ('SELECT s.Surname, s.First_Name, s.group_name, d.name '
                      'FROM students as s INNER JOIN departments as d '
                      'ON s.departments_id = d.id')
        if self.sign_on:
            with DB("students.db") as db:
                list_students = (db.execute(list_studs)).fetchall()
                print('%-12s %-10s %-8s %-30s' % ('Фамилия', 'Имя', 'Группа', 'Факультет'))
                for stud in list_students:
                    print('%-12s %-10s %-8s %-30s' % (stud[0], stud[1], stud[2], stud[3]))
        else:
            print('You haven`t signed on yet')

    def find_student(self, card):
        find_student = ('SELECT s.id, s.Surname, s.First_Name, s.id_card, s.group_name, d.name '
                        'FROM students as s INNER JOIN departments as d where s.ID_card = ?', (card,))
        if self.sign_on:
            with DB("students.db") as db:
                find_stud = (db.execute(* find_student)).fetchone()
                print('%-10s %-10s %-7s %-6s %-30s' % ('Фамилия', 'Имя', 'ID_Card', 'Группа', 'Факультет'))
                print('%-10s %-10s %-7s %-6s %-30s' % (find_stud[1], find_stud[2],
                                                       find_stud[3], find_stud[4], find_stud[5]))
                return find_stud
        else:
            print('You haven`t signed on yet')

    def add_student(self, surname, first_name, card, group_name, department):
        add_stud = ('INSERT INTO students (Surname, First_Name, ID_card, group_name, departments_id) '
                    'VALUES (?, ?, ?, ?, ?)',
                    (surname, first_name, card, group_name, department,))
        if self.sign_on:
            if self.is_admin:
                with DB("students.db") as db:
                    db.execute(* add_stud)
            else:
                print('You haven`t permission')
        else:
            print('You haven`t signed on yet')

    def add_score_to_stud(self, card, score, subject_id):
        stud = self.find_student(card)
        students_id = stud[0]

        add_score = ('INSERT INTO assessments (students_id, subject_id, score) '
                     'VALUES (?, ?, ?)', (students_id, subject_id, score,))
        if self.sign_on:
            if self.is_admin:
                with DB("students.db") as db:
                    db.execute(* add_score)
            else:
                print('You haven`t permission')
        else:
            print('You haven`t signed on yet')

    def add_subject(self, subject_name):
        add_subject = ('INSERT INTO subjects (subject_name) VALUES ?', (subject_name,))
        if self.sign_on:
            if self.is_admin:
                with DB("students.db") as db:
                    db.execute(* add_subject)
            else:
                print('You haven`t permission')
        else:
            print('You haven`t signed on yet')

    def best_students(self):
        best_studs = ('SELECT s.Surname, s.First_Name, s.group_name '
                      'FROM students as s INNER join assessments as a '
                      'ON a.students_id = s.id '
                      'GROUP by a.students_id '
                      'HAVING sum (score)/count(*)=5')
        if self.sign_on:
            with DB("students.db") as db:
                best_studs = (db.execute(best_studs)).fetchall()
                print(best_studs)
                print('%-10s %-10s %-7s' % ('Фамилия', 'Имя', 'Группа'))
                for stud in best_studs:
                    print('%-10s %-10s %-7s' % (stud[0], stud[1], stud[2]))
                return best_studs
        else:
            print('You haven`t signed on yet')

    def get_full_info_stud(self, card):
        self.find_student(card)
        get_score = ('SELECT sbj.name, a.score FROM assessments as a '
                     'INNER JOIN subjects as sbj ON a.subject_id = sbj.id '
                     'INNER JOIN students ON a.students_id = students.id '
                     'WHERE students.ID_card = ?', (card,))
        if self.sign_on:
            with DB("students.db") as db:
                get_scores = (db.execute(* get_score)).fetchall()
                for sc in get_scores:
                    print('%-12s %-7s' % (sc[0], sc[1]))
                return get_scores
        else:
            print('You haven`t signed on yet')


def get_departments():
    with DB("students.db") as db:
        departments = db.execute('SELECT * FROM departments')
        return departments.fetchall()


def get_subjects():
    with DB("students.db") as db:
        subjects = db.execute('SELECT * FROM subjects')
        return subjects.fetchall()


user1 = User()
user1.authentication(login=input('введите логин "login": '), password=input('введите логин "password": '))
user2 = User()
#user2.registration(login=input('регистрация нового пользователя\n введите Login: '), password=input('введите password: '),
#                  confirm_password=input('подтвердите password: '))
user2.authentication(login=input('введите логин "login": '), password=input('введите логин "password": '))
user2.list_of_students()
print('_' * 30)
user2.find_student(card=input('чтобы найти сдудента введите номер его студенческого билета\n: '))
print('_' * 30)
departs = get_departments()
#user1.add_student(surname=input("Для добавления студента в БД заполните данные\n Введите фамилию: "), first_name=input("Введите имя: "),
#                  card=input("Введите номер студенческого билета: "), group_name=input("Введите группу: "),
#                  department=input(f' Введите номер факультета {departs}'))
print('_' * 30)
user2.get_full_info_stud(card=input('чтобы посмотреть оценки студента введите номер его студенческого билета\n: '))
print('_' * 30)
card_ = input("для добавления оценок студента в БД введите номер его студенческого билета: ")
subj = get_subjects()
for i in subj:
    print(i)
while True:
    do_ = input('нажмите 1 для ввода оценок, 2 для добавления предмета или 0 для выхода: ')
    if do_ == '1':
        user1.add_score_to_stud(card=card_, subject_id=input('номер предмета: '), score=input('введите оценку: '))
    if do_ == '2':
        user1.add_subject(subject_name=input('введите название предмета: '))
    else:
        break
user2.best_students()







