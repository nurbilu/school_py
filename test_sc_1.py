import xml.etree.ElementTree as ET

class Human:
    def __init__(self, first_name, last_name ,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Student(Human):
    def test(self):
        print(self.first_name , 'is doing a test')

    def __init__(self, first_name, last_name, age, student_id, field_of_study):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        self.field_of_study = field_of_study
        self.test_lst = []
        self.xml_filename = ""  # Initialize the filename attribute

    def add_test(self, type, grade):
        self.test_lst.append(Test(type, grade))

    def print_all(self):
        for test in self.test_lst:
            print(f"Type: {test.type}, Grade: {test.grade}")

    def highest(self):
        if not self.test_lst:
            return None
        return max(self.test_lst, key=lambda x: x.grade)

    def lowest(self):
        if not self.test_lst:
            return None
        return min(self.test_lst, key=lambda x: x.grade)

    def stop(self):
        # Create an XML element for the student and their tests
        student_element = ET.Element("Student")
        name_element = ET.SubElement(student_element, "Name")
        name_element.text = f"{self.first_name} {self.last_name}"
        age_element = ET.SubElement(student_element, "Age")
        age_element.text = str(self.age)
        id_element = ET.SubElement(student_element, "StudentID")
        id_element.text = self.student_id
        study_element = ET.SubElement(student_element, "FieldOfStudy")
        study_element.text = self.field_of_study

        tests_element = ET.SubElement(student_element, "Tests")
        for test in self.test_lst:
            test_element = ET.SubElement(tests_element, "Test")
            type_element = ET.SubElement(test_element, "Type")
            type_element.text = test.type
            grade_element = ET.SubElement(test_element, "Grade")
            grade_element.text = str(test.grade)

        # Create an XML tree with the student element
        student_tree = ET.ElementTree(student_element)

        # Write the XML tree to the file specified by xml_filename
        student_tree.write(self.xml_filename)

    def __str__(self):
        return f"Student ID: {self.student_id}, Field of Study: {self.field_of_study}, {super().__str__()}"

class Test:
    def __init__(self, type, grade):
        self.type = type
        self.grade = grade

    @staticmethod
    def avg_test_grd(tests):
        if not tests:
            return 0.0
        total = sum(test.grade for test in tests)
        return total / len(tests)

if __name__ == '__main__':
    student1 = Student("John", "Doe", 20, "12345", "Computer Science")
    student2 = Student("aiden", "allstar", 23, "09876", "math")
    student1.add_test("Midterm", 85)
    student1.add_test("Final", 92)
    student2.add_test("Midterm", 67)
    student2.add_test("Final", 97)
    # Set the XML filename before stopping
    student1.xml_filename = "student_data.xml"
    print("\n",student1)
    print("\n",student2)
    student1.print_all()
    student2.print_all()
    # Save the data to an XML file when stopping the program
    student1.stop()
