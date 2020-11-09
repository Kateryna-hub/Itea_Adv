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

    def person_age_matching(self, from_, to_):
        today = date.today()
        person_age = today.year - self.birthday
        if from_ <= person_age <= to_:
            return self.show()


class Applicant(Person):

    def show(self):
        print('{}, {}, {}'.format(self.surname, self.birthday, self.faculty))


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


applicant1 = Applicant('Ivanov', 1998, 'CS')
applicant2 = Applicant('Popov', 1999, 'CEC')
applicant3 = Applicant('Popov', 1998, 'ITM')
student1 = Student('Petrov', 1993, 'CEC', 3)
student2 = Student('Volkov', 1995, 'CS', 1)
teacher1 = Teacher('Smirnov', 1972, 'CS', 'assistant professor ', 17)
teacher2 = Teacher('Lebedev', 1965, 'ITM', 'professor', 35)

list_of_person = [applicant1, applicant2, applicant3, student1, student2, teacher1, teacher2]

for item in list_of_person:
    item.show()
print('-' * 18)
[item.person_age_matching(18, 25) for item in list_of_person]
