import random
import mongoengine as me


first_name = ('Иван', 'Федор', 'Петр', 'Владимир', 'Александр', 'Алексей', 'Сергей', 'Максим', 'Игорь', 'Павел', 'Егор',
              'Екатерина', 'Татьяна', 'Светлана', 'Маргарита', 'Людмила', 'Анна', 'Алла', 'Валентина', 'Ольга')
last_name = ('Шевченко', 'Бондаренко', 'Петров', 'Сидоров', 'Котов', 'Поляков', 'Зайцев', 'Никитюк', 'Леонов',
             'Крамаренко', 'Игнатенко', 'Петренко', 'Волков', 'Медведев', 'Поляшенко', 'Бобров', 'Иванов', 'Сеничкин',
             'Леонтьев', 'Пугачев', 'Галкин', 'Макаров', 'Игнотов', 'Сеницын', 'Фролов', 'Бондарев', 'Макаренко',
             'Крамаров', 'Сидоренко', 'Котенко')
heads = ['Марченко В.И.', 'Шубин С.Ф.', 'Михеев О.А.', 'Сергеев А.С.', 'Юрченко В.В.', 'Захаров М.Ю.']
groups = ['Группа 1', 'Группа 2']
departments = ['Компьютерные сети', 'Программирование', 'Информационная безопасность']


me.connect('STUDENTS')


class Student(me.Document):
    full_name = me.StringField(min_length=5, max_length=65, required=True)
    group_name = me.StringField(required=True)
    group_head = me.StringField(min_length=2, max_length=30, required=True)
    department = me.StringField(min_length=2, max_length=65, required=True)

    def __str__(self):
        return f'{self.full_name} {self.department}'


class StudentMarks(me.Document):
    math = me.IntField(min_value=0, max_value=120)
    systems = me.IntField(min_value=0, max_value=120)
    architecture = me.IntField(min_value=0, max_value=120)
    technology = me.IntField(min_value=0, max_value=120)
    networks = me.IntField(min_value=0, max_value=120)
    english = me.IntField(min_value=0, max_value=120)
    logic = me.IntField(min_value=0, max_value=120)
    algorithms = me.IntField(min_value=0, max_value=120)
    student = me.ReferenceField(Student)


def students_of_head(head):
    studs_ = Student.objects(group_head=head)
    return studs_


def best_student():
    list_ = []
    for dep in departments:
        stud_departments = Student.objects(department=dep)
        for std in stud_departments:
            marks_of_stud = StudentMarks.objects(student=std.id)
            for m in marks_of_stud:
                marks_average = (m.math + m.systems + m.architecture + m.technology +
                                 m.networks + m.english + m.logic + m.algorithms)/8
                if marks_average > 100:
                    list_.append([std.department, std.full_name, std.group_name, marks_average])
    return list_


if __name__ == '__main__':

    # for i in range(120):
    #     name_ = random.choice(first_name)
    #     surname_ = random.choice(last_name)
    #     if (name_[-1] == "а") and (surname_[-1] == "в" or surname_[-1] == "н"):
    #         surname = surname_ + 'a'
    #     else:
    #         surname = surname_
    #     student_name = surname + ' ' + name_
    #     department_ = random.choice(departments)
    #     group = random.choice(groups)
    #     head = ''
    #     if department_ == departments[0] and group == groups[0]:
    #         head = heads[0]
    #     if department_ == departments[0] and group == groups[1]:
    #         head = heads[1]
    #     if department_ == departments[1] and group == groups[0]:
    #         head = heads[2]
    #     if department_ == departments[1] and group == groups[1]:
    #         head = heads[3]
    #     if department_ == departments[2] and group == groups[0]:
    #         head = heads[4]
    #     if department_ == departments[2] and group == groups[1]:
    #         head = heads[5]
    #     student = Student(full_name=student_name, group_name=group, group_head=head, department=department_).save()
    #     student_marks = StudentMarks(math=random.randint(50, 120), systems=random.randint(60, 120),
    #                                  architecture=random.randint(50, 120), technology=random.randint(60, 120),
    #                                  networks=random.randint(50, 120), english=random.randint(60, 120),
    #                                  logic=random.randint(50, 120), algorithms=random.randint(60, 120), student=student)
    #     student_marks.save()

    students_ = students_of_head('Марченко В.И.')
    for u in students_:
        print('%-20s %-10s %-10s %-30s' % (u.full_name, u.group_name, u.group_head, u.department))
    print('_' * 75)
    print('%-30s | %-20s | %-10s | %-8s' % ('Факультет', 'студент', 'группа', 'балл'))
    print('_' * 75)
    bests_of_students = best_student()
    for st in bests_of_students:
        print('%-30s | %-20s | %-10s | %-8d' % (st[0], st[1], st[2], st[3]))
