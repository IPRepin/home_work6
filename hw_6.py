class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses:
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += [grade]
            else:
                lecturer.courses_grades[course] = [grade]

    def average_grades_student(self):
        rate_lst_student = list(self.grades.values())
        if len(rate_lst_student) == 0:
            self.avg_student = 0
        else:
            self.avg_student = sum(rate_lst_student) / len(rate_lst_student)
        return self.avg_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
        else:
            self.avg_student < other.avg_student


    def __str__(self):
        some_student = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades_student()}\n" \
                        f"Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"
        return some_student




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_grades = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)



    def average_grades(self):
        rate_lst = list(self.courses_grades.values())
        if len(rate_lst) == 0:
            self.avg = 0
        else:
            self.avg = sum(rate_lst) / len(rate_lst)
        return self.avg

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
        else:
            self.avg < other.avg

    def __str__(self):
        some_lecturer = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades()}"
        return some_lecturer


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f"Имя: {self.name}\nФамилия: {self.surname}"
        return some_reviewer





student_1 = Student('Ivan', 'Ivanov', 'male')
student_1.courses_in_progress.append('Python')
student_1.finished_courses.append('JavaScript')


student_2 = Student('Irina', 'Petrova', 'female')
student_2.courses_in_progress.append('JavaScript')
student_2.finished_courses.append('PHP')


lecturer_1 = Lecturer('Maxim', 'Sidorov')
lecturer_1.courses_attached.append('JavaScript')
lecturer_1.courses_attached.append('PHP')


lecturer_2 = Lecturer('Igor', 'Vasilev')
lecturer_2.courses_attached.append('Python')
lecturer_2.courses_attached.append('HTML')


reviewer_1 = Reviewer('Elena', 'Sidorenko')
reviewer_1.courses_attached.append('Python')


reviewer_2 = Reviewer('Vitalii', 'Volgin')
reviewer_2.courses_attached.append('Python')


student_1.rate_lecture(lecturer_2, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'JavaScript', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'JavaScript', 9)
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)