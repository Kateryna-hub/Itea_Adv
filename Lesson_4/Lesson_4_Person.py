from abc import ABC, abstractmethod
from datetime import date

class Person(ABC):

    def __init__(self, surname, birthday, faculty):
        self.surname = surname
        self.birthday = birthday
        self.faculty = faculty


    @abstractmethod
    def show(self):
        pass

    def age(self):
        today = date.today()
        return today.year - self.birthday


class Applicant(Person):

    def show(self):
        print('{}, {}, {}'.format(self.surname, self.birthday, self.faculty))

    def add_to_list(self, list_):
        list_.append([self.surname, self.birthday, self.faculty])




class Student(Person):

    def __init__(self, surname, birthday, faculty, course):
        super(Student, self).__init__(surname, birthday, faculty)
        self.course = course

    def show(self):
        print('{}, {}, {}, {}'.format(self.surname, self.birthday, self.faculty, self.course))


class Teacher(Person):

    def __init__(self, surname, birthday, faculty, position, experience):
        super(Teacher, self).__init__(surname, birthday, faculty)
        self.position = position
        self.experience = experience

    def show(self):
        print('{}, {}, {}, {}, {}'.format(self.surname, self.birthday, self.faculty, self.position, self.experience))



applicant1 = Applicant('Ivanov', 1977, 'tyui')
print(applicant1.age())
applicant1.show()
list = []
applicant1.add_to_list(list)
print(list)