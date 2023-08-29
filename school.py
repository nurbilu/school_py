from enum import Enum 
import numpy
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
    pass



class Human:
    def __init__(self, first_name, last_name ,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"First name: {self.first_name},Last name:{self.last_name}, Age: {self.age}"

# class Test(Student):
#     def __init__(self, type, grade):
#       self.type=""
#       self.grade =0 

class Student(Human):
    def test(self):
        print(self.first_name , 'is doing a test')

    def __init__(self, first_name, last_name,age, student_id, field_of_study):
        super().__init__(first_name,last_name, age)
        self.student_id = student_id
        self.field_of_study = field_of_study
        self.test_lst=[]
    
    def add_test(self ,type,grade):
        self.test_lst.append(Test(type , grade))

    def print_all():
        pass

    def highest():
        pass
    def lowest():
        pass
    
    def stop():
        pass

    def __str__(self):
        return f"Student ID: {self.student_id}, Field of Study: {self.field_of_study}, {super().__str__()}"

class Test(Student):
    def __init__(self, type, grade):
      self.type=""
      self.grade =0 
    
    def avg_test_grd():
        pass


if __name__ == '__main__':
    pass
    s1=Student('Matan' , 'Cohen' , 22 ,87653233,"History")
    print(s1)