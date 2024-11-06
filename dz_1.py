class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'ф.и.о {self.full_name}, {self.age} лет, и {self.is_married}')

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = dict(marks)

    def average_rating(self):
        print('средняя оценка: ')
        print(sum(self.marks.values()) / len(self.marks))

class Teacher(Person):
    base_salary = 30000
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def count_salary(self):
        print(f'опыт работы {self.experience}')
        bonus = self.base_salary
        if self.experience > 3:
            for i in range(4, self.experience + 1):
                bonus += 0.05 * bonus
        return f'зарплата: {bonus}'

teacher = Teacher('Albert Lux',27,'не женат',6)
teacher.introduce_myself()
print(teacher.count_salary())


