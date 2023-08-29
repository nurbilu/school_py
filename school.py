from enum import Enum 
import numpy as np
import json
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


# class Commands(Enum):
#     LOAD = 1
#     SAVE = 2



class Human:
    def __init__(self, first_name, last_name ,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"First name: {self.first_name},Last name:{self.last_name}, Age: {self.age}"



class Student(Human):
    students=[]
    test_lst=[]
    def test(self):
        print(self.first_name , 'is doing a test')

    def __init__(self, first_name, last_name,age, student_id, field_of_study):
        super().__init__(first_name,last_name, age)
        self.student_id = student_id
        self.field_of_study = field_of_study

    def add_student():
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = int(input("Enter age: "))
        student_id = input("Enter student ID: ")
        field_of_study = input("Enter field of study: ")
  
        new_student = Student(first_name, last_name, age, student_id, field_of_study)
        Student.students.append(new_student)

    
    
    def add_test():
        try:
            student_id = input("Enter student ID: ")
            student = next((s for s in Student.students if s.student_id == student_id), None)
            if not student:
                print("Student not found")
                return

            test_type = input("Enter test type: ")  
            test_grade = float(input("Enter grade: "))
    
            test = Test(test_type, test_grade)
            student.test_lst.append(test)

        except ValueError:
            print("Invalid grade. Please enter a number.")
  
        except Exception as e:
            print("Error adding test:", e)
        
    def print_student_averages():
        for student in Student.students:
            print(f"{student.first_name} {student.last_name}: {student.avg_score()}")

    def sort_student_averages():
        sorted_students = sorted(Student.students, key=lambda student: student.avg_score())
        for student in sorted_students:
            print(student)

    def reverse_sort_student_averages():
        sorted_students = sorted(Student.students, key=lambda student: student.avg_score(), reverse=True)
        for student in sorted_students:
            print(student)  

    @staticmethod
    def Print_studnets():
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
    


def menu():
    while True:
        print("SMTIM:\n""School Management Test Info Menu:\n")
        print(f"{Actions.ADD_STUDENT.value}. Add student")
        print(f"{Actions.ADD_TEST.value}. Add test")
        print(f"{Actions.PRINT_STUDENT_AVRAGE.value}. Print total students avrage")
        print(f"{Actions.AVRAGE_SORTED.value}. Sort avrage ")
        print(f"{Actions.AVRAGE_SORTED_REVERSE.value}. Revresed sort avrage ")
        print(f"{Actions.HIGHEST_SCORE.value}. Highest score student")
        print(f"{Actions.LOWEST_SCORE.value}. Lowest score student")
        print(f"{Actions.PRINT_STUDENTS.value}. Print all studnets")
        print(f"{Actions.EXIT.value}. Exit")
        

        choice = input("Enter your choice: ")

        if choice == str(Actions.ADD_STUDENT.value):
            Student.add_student()
            pass
        elif choice == str(Actions.ADD_TEST.value):
            Student.add_test()
        elif choice == str(Actions.PRINT_STUDENT_AVRAGE.value):
            Student.avg_score
            Student.print_student_averages()
        elif choice == str(Actions.AVRAGE_SORTED.value):
            Student.sort_student_averages()
            pass
        elif choice == str(Actions.AVRAGE_SORTED_REVERSE.value):
            Student.reverse_sort_student_averages()
            pass
        elif choice == str(Actions.HIGHEST_SCORE.value):
            Student.highest()
            pass
        elif choice == str(Actions.LOWEST_SCORE.value):
            Student.lowest()
            pass
        elif choice == str(Actions.PRINT_STUDENTS.value):
            Student.Print_studnets()
            pass
        elif choice == str(Actions.EXIT.value):
                break
        else:
            print("Invalid choice. Please enter a valid option.")


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
    menu()
    save_data()
