import sqlite3


class DB:

    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()


def fetch_all(db_name, sql):

    with DB(db_name) as db:
        result = db.execute(sql)
        return result.fetchall()


def fetch_one(db_name, sql):

    with DB(db_name) as db:
        result = db.execute(* sql)
        return result.fetchone()


card = input("Введите для id_card поиска: ")
find_id_card = ('SELECT s.id_card, s.Surname, s.First_Name, s.group_name, d.name '
                'FROM students as s INNER JOIN departments as d where s.ID_card = ?', (card,))
print(find_id_card)


view_studs = ('SELECT s.Surname, s.First_Name, s.group_name, d.name '
              'FROM students as s INNER JOIN departments as d '
              'ON s.departments_id = d.id')

get_excellent_students = ('SELECT s.Surname, s.First_Name, s.group_name '
                          'FROM students as s INNER join assessments as a '
                          'ON a.students_id = s.id '
                          'GROUP by a.students_id '
                          'HAVING sum (score)/count(*)=5')

get_full_info = ('')


view_students = fetch_all("students.db", view_studs)
print('%-12s %-10s %-8s %-30s' % ('Фамилия', 'Имя', 'Группа', 'Факультет'))
for i in view_students:
    print('%-12s %-10s %-8s %-30s' % (i[0], i[1], i[2], i[3]))

find = fetch_one("students.db", find_id_card)
print(find)

excellents_ = fetch_all("students.db", get_excellent_students)
print(excellents_)
