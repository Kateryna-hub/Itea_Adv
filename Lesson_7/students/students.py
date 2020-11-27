import sqlite3
import sys


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
            user = []
            user_get = (db.execute(* ('SELECT users.login, users.password, users.is_admin '
                                      'FROM users WHERE users.login = ?', (login,)))).fetchone()
            if user_get is None:
                sys.exit("no such user")
            else:
                user = user_get

            return user

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
                                sys.exit('password must contain 10 or more symbols')
                        else:
                            sys.exit('password must contain the special symbol')
                    else:
                        sys.exit('password must contain the letter')
                else:
                    sys.exit('password must contain the number')
            else:
                sys.exit('The passwords are not the same')
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
        sql_list_students = ('SELECT s.Surname, s.First_Name, s.ID_card, s.group_name, d.full_name '
                             'FROM students as s INNER JOIN departments as d '
                             'ON s.dep_short = d.short_name')
        if self.sign_on:
            with DB("students.db") as db:
                list_students = (db.execute(sql_list_students)).fetchall()
                print('%-12s %-10s %-10s %-8s %-30s' % ('Фамилия', 'Имя', 'Ст.билет', 'Группа', 'Факультет'))
                for stud in list_students:
                    print('%-12s %-10s %-8s %-8s %-30s' % (stud[0], stud[1], stud[2], stud[3], stud[4]))
        else:
            print('You haven`t signed on yet')

    def find_student(self, card):
        sql_find_student = ('SELECT s.Surname, s.First_Name, s.id_card, s.group_name, s.dep_short, d.full_name '
                            'FROM students as s INNER JOIN departments as d ON s.dep_short = d.short_name '
                            'WHERE s.ID_card = ?', (card,))
        if self.sign_on:
            with DB("students.db") as db:
                find_student = (db.execute(* sql_find_student)).fetchone()

                print('%-10s %-10s %-7s %-6s %-30s' % ('Фамилия', 'Имя', 'ID_Card', 'Группа', 'Факультет'))
                print('%-10s %-10s %-7s %-6s %-30s' % (find_student[0], find_student[1],
                                                       find_student[2], find_student[3], find_student[5]))
                return find_student
        else:
            print('You haven`t signed on yet')

    def get_subjects_department(self, dep_short):
        sql_get_subject = ('SELECT id, name, d_short_name FROM subjects '
                           'WHERE (d_short_name = "All") OR (d_short_name = ?)', (dep_short,))
        if self.sign_on:
            with DB("students.db") as db:
                get_subjects = (db.execute(* sql_get_subject)).fetchone()
                return get_subjects
        else:
            print('You haven`t signed on yet')

    def get_score_student(self, card):
        sql_get_scores = ('SELECT subjects.name, scores.score FROM scores '
                          'INNER JOIN subjects ON scores.id_subject = subjects.id '
                          'WHERE scores.id_card = ?', (card,))
        if self.sign_on:
            with DB("students.db") as db:
                get_scores = (db.execute(* sql_get_scores)).fetchall()

                for subject in get_scores:
                    print('%-35s %-3s' % (subject[0], subject[1]))
                return get_scores
        else:
            print('You haven`t signed on yet')

    def best_students(self):
        sql_best_students = ('SELECT s.Surname, s.First_Name, s.group_name, d.full_name '
                             'FROM students as s '
                             'INNER JOIN departments as d ON s.dep_short = d.short_name '
                             'INNER JOIN scores '
                             'ON scores.id_card = s.ID_card '
                             'GROUP by scores.id_card '
                             'HAVING sum (score)/count(*)=5')
        if self.sign_on:
            with DB("students.db") as db:
                best_students = (db.execute(sql_best_students)).fetchall()
                print("Список отличников")
                for stud in best_students:
                    print('%-12s %-10s %-6s %-30s' % (stud[0], stud[1], stud[2], stud[3]))

                return best_students
        else:
            print('You haven`t signed on yet')

    def add_student(self, surname, first_name, card, group_name, dep_short, score=0):
        sql_add_student = ('INSERT INTO students (Surname, First_Name, ID_card, group_name, departments_id) '
                           'VALUES (?, ?, ?, ?, ?)', (surname, first_name, card, group_name, dep_short,))
        list_subjects = self.get_subjects_department(dep_short)
        if self.sign_on:
            if self.is_admin:
                with DB("students.db") as db:
                    db.execute(* sql_add_student)
                    for subject in list_subjects:
                        db.execute(* ('INSERT INTO scores (id_card, score, id_subject)'
                                      'VALUES (?, ?, ? )', (card, score, subject)))
            else:
                print('You haven`t permission')
        else:
            print('You haven`t signed on yet')

    def set_score_to_stud(self, card, new_score, subject_id):
        sql_set_score = ('UPDATE scores SET score = ? '
                         'WHERE (id_card = ?) AND (subject_id = ?)', (new_score, card, subject_id))
        if self.sign_on:
            if self.is_admin:
                with DB("students.db") as db:
                    db.execute(* sql_set_score)
            else:
                print('You haven`t permission')
        else:
            print('You haven`t signed on yet')

    @staticmethod
    def show_departments(self):
        with DB("students.db") as db:
            dep = (db.execute("SELECT * FROM departments")).fetchall()
            for d in dep:
                print(d[1], d[2])

    def update_student_info(self, table, var1, var2, card_):
        sql = 'UPDATE ' + table + ' SET ' + var1 + ' = "' + var2 + '" WHERE ID_card = ' + card_
        if self.sign_on:
            if self.is_admin:
                with DB("students.db") as db:
                    db.execute(str(sql))
            else:
                print('You haven`t permission')
        else:
            print('You haven`t signed on yet')

    def get_full_info_stud(self, card):
        self.find_student(card)
        self.get_score_student(card)

if __name__ == '__main__':

    user1 = User()
    user1.authentication(login=input('введите логин "login": '), password=input('введите "password": '))
    user1.list_of_students()
    print('_' * 75)
    user1.get_full_info_stud(input('Введите номер студенческого: '))
    print('_' * 75)
    user1.best_students()
    print('_' * 75)
    user1.find_student(input('Введите номер студенческого: '))
    table = ''
    var1 = ''
    var2 = ''
    t1 = input('1 - surname, 2 - group, 3 department')
    if t1 == '1':
        table = 'students'
        var1 = 'Surname'
        var2 = input('Введите новую фамилию: ')
    if t1 == '2':
        table = 'students'
        var1 = 'group_name'
        var2 = input('Введите группу: ')
    if t1 == '3':
        user1.show_departments()
        table = 'students'
        var1 = 'd_short_name'
        var2 = input('Введите аббревиатуру факультета: ')
    user1.update_student_info(table=table, var1=var1, var2=var2, card_=input('Введите номер студенческого: '))
    user1.list_of_students()
    print('_' * 75)
    user2 = User()
    user2.registration(login=input('регистрация нового пользователя\n введите Login: '),
                       password=input('введите password: '), confirm_password=input('подтвердите password: '))
    user2.authentication(login=input('введите логин "login": '), password=input('введите логин "password": '))
    user2.list_of_students()
    print('_' * 75)
    user2.find_student(card=input('чтобы найти сдудента введите номер его студенческого билета\n: '))
    print('_' * 75)
    user1.add_student(surname=input("Для добавления студента в БД заполните данные\n Введите фамилию: "),
                      first_name=input("Введите имя: "),
                      card=input("Введите номер студенческого билета: "), group_name=input("Введите группу: "),
                      dep_short=input(f'Введите факультет'))
    print('_' * 75)








