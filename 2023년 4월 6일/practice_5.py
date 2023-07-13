class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student1 = Student(2020112084, "제보민")
student2 = Student(2020112087, "우신영")

print("첫번째 학생의 학번:", student1.student_id)
print("첫번째 학생의 이름:", student1.student_name)

print("두번째 학생의 학번:", student2.student_id)
print("두번째 학생의 이름:", student2.student_name)
#2020112084 제보민
