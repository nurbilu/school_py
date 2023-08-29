from enum import Enum 
import json
import numpy as np

class Actions(Enum):
    ADD_STUDENT = 0
    ADD_TEST = 1
    PRINT_STUDENT_AVRAGE = 2
    AVRAGE_SORTED = 3
    AVRAGE_SORTED_REVERSE =4
    HIGHEST_SCORE = 5
    LOWEST_SCORE = 6
    PRINT_STUDENTS = 7
    EXIT = 8


class Commands(Enum):
    LOAD_DATA = 0
    SAVE_DATA = 1



class Human:
    def __init__(self, first_name, last_name ,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"First name: {self.first_name},Last name:{self.last_name}, Age: {self.age}"


class Student(Human):
    students = []
    def test(self):
        print(self.first_name , 'is doing a test')

    def __init__(self, first_name, last_name,age, student_id, field_of_study):
        super().__init__(first_name,last_name, age)
        self.student_id = student_id
        self.field_of_study = field_of_study
        self.test_lst=[]
    
    def add_test(self ,type,grade):
        self.test_lst.append(Test(type , grade))

    @staticmethod
    def print_all():
        print("\n".join(str(student) for student in Student.students))
    
    @staticmethod
    def highest():
        if Student.students:
            return max(Student.students, key=lambda student: student.avg_score())

    @staticmethod  
    def lowest():
        if Student.students:  
            return min(Student.students, key=lambda student: student.avg_score())

    @staticmethod
    def stop():
        print("Exiting program...")
        exit()

    def avg_score(self):
        if self.test_lst:
            return np.mean([test.grade for test in self.test_lst])
        else:
            return 0

    def __str__(self):
        return f"Student ID: {self.student_id}, Field of Study: {self.field_of_study}, {super().__str__()}"



class Test(Student):
    def __init__(self, type, grade):
      self.type=""
      self.grade =0 
    
    # def avg_test_grd():
    #     pass
def load_data():
  try:
    with open('students.json') as f:
      data = json.load(f)
      for item in data:
        student = Student(**item)
        Student.students.append(student)
  except FileNotFoundError:
    print("Could not load student data.")

def save_data():
  data = [student.__dict__ for student in Student.students]
  with open('students.json', 'w') as f:
    json.dump(data, f, indent=2)
  print("Student data saved.")

if __name__ == '__main__':
    load_data()
    
    while True:
        action = int(input("Select an action: "))
        if action == Actions.ADD_STUDENT.value:
            Human
        elif action == Actions.ADD_TEST.value: 
            Student.add_test()
        elif action == Actions.PRINT_STUDENT_AVRAGE.value:
            Student.print_all()
        elif action == Commands.LOAD_DATA.value:
            load_data()
        elif action == Commands.SAVE_DATA.value:
            save_data()
        elif action == Actions.EXIT.value:
            Student.stop()
      
    save_data()