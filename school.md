# Student Test Data Management System

This Python program is designed to manage and store test data for students. It provides a simple class structure to create student profiles, add test scores, and save the data in an XML file.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Class Structure](#class-structure)
- [License](#license)

## Introduction

This program allows you to create and manage student profiles. For each student, you can add various test scores, calculate average grades, and save the student's data to an XML file.

## Features

- Create and manage student profiles.
- Add multiple test scores for each student.
- Calculate the average test grade for a set of tests.
- Save student data, including test scores, to an XML file.

## Requirements

- Python 3.x
- No external libraries or dependencies are required.

## Usage

1. **Creating Student Profiles**: To create a student profile, use the `Student` class. You can provide the student's first name, last name, age, student ID, and field of study when initializing a student object.

   ```python
   student1 = Student("John", "Doe", 20, "12345", "Computer Science")
   student2 = Student("Aiden", "Allstar", 23, "09876", "Math")
   ```

2. **Adding Test Scores**: To add test scores for a student, use the `add_test` method. This method allows you to specify the type of test (e.g., "Midterm," "Final") and the grade for that test.

   ```python
   student1.add_test("Midterm", 85)
   student1.add_test("Final", 92)
   student2.add_test("Midterm", 67)
   student2.add_test("Final", 97)
   ```

3. **Calculating Average Test Grade**: You can calculate the average test grade for a set of tests using the `avg_test_grd` method of the `Test` class.

   ```python
   avg_grade = Test.avg_test_grd(student1.test_lst)
   ```

4. **Printing Student Data**: Use the `print_all` method to print all test scores for a student.

   ```python
   student1.print_all()
   student2.print_all()
   ```

5. **Saving Student Data to XML**: Set the `xml_filename` attribute of a student object to specify the XML file where the student's data should be saved. Use the `stop` method to write the student data to the XML file.

   ```python
   student1.xml_filename = "student_data.xml"
   student1.stop()
   ```

## Class Structure

- `Human`: Base class for storing human-related attributes.
- `Student`: Derived class that extends `Human` and adds functionality for managing student data and test scores.
- `Test`: Class to represent a single test with attributes for test type and grade.

## License

This code is provided under the [MIT License](LICENSE). Feel free to use and modify it for your needs.