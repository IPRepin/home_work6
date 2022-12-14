all_courses = ['JavaScript', 'PHP', 'Python', 'HTML']
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.courses_grades:
                lecturer.courses_grades[course] += grade
            else:
                lecturer.courses_grades[course] = grade

    def average_grades_student(self):
        rate_lst_student = self.grades.values()
        grades = []
        for grade in rate_lst_student:
            grades.append(grade)
        if len(grades) == 0:
            self.avg_student = 0
        else:
            self.avg_student = sum(grades) / len(grades)
        return self.avg_student

    def all_students_rate(self):
        all_students = []
        for student in Student:
            all_students.append(student)
        for cours in all_courses:
            if cours in self.finished_courses:
                rate_student = self.grades.values()
                all_grades = []
                for grade in rate_student:
                    all_grades.append(grade)
                    avg_all_students_rate = sum(all_grades) / len(all_grades)

            print(f'Средний бал курса {cours}: {avg_all_students_rate}')




    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
        else:
            return self.avg_student < other.avg_student


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
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_grades = {}



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
            return self.avg < other.avg

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
                student.grades[course] += grade
            else:
                student.grades[course] = grade
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
reviewer_1.courses_attached.append('JavaScript')


reviewer_2 = Reviewer('Vitalii', 'Volgin')
reviewer_2.courses_attached.append('Python')

reviewer_1.rate_hw(student_2, 'JavaScript', 7)
reviewer_2.rate_hw(student_1, 'Python', 8)
student_1.rate_lecture(lecturer_2, 'Python', 10)
student_2.rate_lecture(lecturer_1, 'JavaScript', 8)

print(student_1)
print(student_2)
print(lecturer_2)
print(lecturer_1)
print(reviewer_2)
print(reviewer_1)


students_list = [student_1, student_2]
students_grades_list = []
def student_midgrades(student_list, course):
    for student in student_list:
        if course in student.grades.keys():
            students_grades_list.extend(student.grades.values())
    avg_sudent_grade = sum(students_grades_list) / len(students_grades_list)
    print(f'Средний бал по всем студентам курса {course}: {avg_sudent_grade}')



lecturer_list = [lecturer_1, lecturer_2]

def lecturer_midgrades(lecturer_list, course):
    lecturer_grades_list = []
    for lecturer in lecturer_list:
        if course in lecturer.courses_grades.keys():
                lecturer_grades_list.extend(lecturer.courses_grades.values())
    avg_lecturer_grade = sum(lecturer_grades_list) / len(lecturer_grades_list)
    print(f'Средний бал по всем лекторам курса {course}: {avg_lecturer_grade}')




student_midgrades(students_list, 'Python')
lecturer_midgrades(lecturer_list, 'JavaScript')
