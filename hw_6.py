class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.grades_lecturer:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades_student(self):
        rate_lst_student = list(self.grades.values())
        if len(rate_lst_student) == 0:
            self.avg_student = 0
        else:
            self.avg_student = sum(rate_lst_student) / len(rate_lst_student)
        return self.avg_student

    # def cool_student(self):
    #     if self.avg_student > self.avg_student:


    def __str__(self):
        some_student = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades_student()}\n" \
                        f"Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"
        return some_student




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def rate_lecturer(self):
        self.grades_lecturer = {}
        return self.grades_lecturer

    def average_grades(self):
        rate_lst = list(self.rate_lecturer().values())
        if len(rate_lst) == 0:
            self.avg = 0
        else:
            self.avg = sum(rate_lst) / len(rate_lst)
        return self.avg

    def __str__(self):
        some_lecturer = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades()}"
        return some_lecturer


class Reviewer(Mentor):
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
student_1.finished_courses.append('HTML')
student_1.grades.update({'python_hw1': 9, 'python_hw2': 8, 'python_hw3': 10, 'python_hw4': 9, 'python_hw5': 5})
print(student_1)

student_2 = Student('Irina', 'Petrova', 'female')
student_2.courses_in_progress.append('Python')
student_2.finished_courses.append('JavaScript')
student_2.finished_courses.append('PHP')
student_2.grades.update({'python_hw1': 7, 'python_hw2': 10, 'python_hw3': 8, 'python_hw4': 9, 'python_hw5': 6})
print(student_2)

lecturer_1 = Lecturer('Maxim', 'Sidorov')
lecturer_1.courses_attached.append('JavaScript')
lecturer_1.courses_attached.append('PHP')
# lecturer_1.grades_lecturer.update({'JavaScript': 7, 'PHP': 10})
print(lecturer_1)

lecturer_2 = Lecturer('Igor', 'Vasilev')
lecturer_2.courses_attached.append('Python')
lecturer_2.courses_attached.append('HTML')
# lecturer_2.grades_lecturer.update({'JavaScript': 7, 'PHP': 10})
print(lecturer_2)

reviewer_1 = Reviewer('Elena', 'Sidorenko')
print(reviewer_1)

reviewer_2 = Reviewer('Vitalii', 'Volgin')
print(reviewer_2)