# student_management_system.py

import json

def add_student(students):
  """Adds a new student to the student dictionary."""
  serial_number = len(students) + 1
  fname = input("Enter the first name: ")
  lname = input("Enter the last name: ")
  contact = input("Enter the contact number: ")
  while True:
    try:
      int(contact)
      break
    except ValueError:
      print("Invalid contact number. Please enter a valid number.")
      contact = input("Enter the contact number: ")
  subjects = {}
  while True:
    subject = input("Enter a subject (or type 'done' to finish): ")
    if subject.lower() == 'done':
      break
    marks = input("Enter the marks for {}: ".format(subject))
    while True:
      try:
        int(marks)
        break
      except ValueError:
        print("Invalid marks. Please enter a valid number.")
        marks = input("Enter the marks for {}: ".format(subject))
    fees = input("Enter the fees for {}: ".format(subject))
    while True:
      try:
        int(fees)
        break
      except ValueError:
        print("Invalid fees. Please enter a valid number.")
        fees = input("Enter the fees for {}: ".format(subject))
    subjects[subject] = {'marks': int(marks), 'fees': int(fees)}
  faculty = input("Enter the faculty name: ")
  students[serial_number] = {
      'fname': fname,
      'lname': lname,
      'contact': contact,
      'subject': subjects,
      'faculty': faculty,
  }
  print("Student added successfully.")

def remove_student(students):
  """Removes a student from the student dictionary."""
  student_id = input("Enter the ID of the student to remove: ")
  while True:
    try:
      int(student_id)
      break
    except ValueError:
      print("Invalid student ID. Please enter a valid number.")
      student_id = input("Enter the ID of the student to remove: ")
  if student_id in students:
    del students[student_id]
    print("Student removed successfully.")
  else:
    print("Student not found.")

def view_all_students(students):
  """Displays all students in the student dictionary."""
  if students:
    for student_id, student_data in students.items():
      print("\nStudent ID:", student_id)
      print("First Name:", student_data['fname'])
      print("Last Name:", student_data['lname'])
      print("Contact Number:", student_data['contact'])
      print("Subjects and Marks:")
      for subject, details in student_data['subject'].items():
        print(f"  {subject}: Marks - {details['marks']}, Fees - {details['fees']}")
      print("Faculty:", student_data['faculty'])
  else:
    print("No students found.")

def view_specific_student(students):
  """Displays a specific student from the student dictionary."""
  student_id = input("Enter the ID of the student to view: ")
  while True:
    try:
      int(student_id)
      break
    except ValueError:
      print("Invalid student ID. Please enter a valid number.")
      student_id = input("Enter the ID of the student to view: ")
  if student_id in students:
    student_data = students[student_id]
    print("\nStudent ID:", student_id)
    print("First Name:", student_data['fname'])
    print("Last Name:", student_data['lname'])
    print("Contact Number:", student_data['contact'])
    print("Subjects and Marks:")
    for subject, details in student_data['subject'].items():
      print(f"  {subject}: Marks - {details['marks']}, Fees - {details['fees']}")
    print("Faculty:", student_data['faculty'])
  else:
    print("Student not found.")

def add_marks(students, faculty_name):
  """Allows faculty to add marks for their students."""
  student_id = input("Enter the ID of the student to add marks: ")
  while True:
    try:
      int(student_id)
      break
    except ValueError:
      print("Invalid student ID. Please enter a valid number.")
      student_id = input("Enter the ID of the student to add marks: ")
  if student_id in students:
    student_data = students[student_id]
    if student_data['faculty'] == faculty_name:
      while True:
        subject = input("Enter the subject to add marks (or type 'done' to finish): ")
        if subject.lower() == 'done':
          break
        marks = input("Enter the new marks for {}: ".format(subject))
        while True:
          try:
            int(marks)
            break
          except ValueError:
            print("Invalid marks. Please enter a valid number.")
            marks = input("Enter the new marks for {}: ".format(subject))
        student_data['subject'][subject]['marks'] = int(marks)
        print("Marks updated successfully.")
    else:
      print("You are not authorized to add marks for this student.")
  else:
    print("Student not found.")

def load_students():
  """Loads students from a JSON file."""
  try:
    with open('students.json', 'r') as f:
      return json.load(f)
  except FileNotFoundError:
    return {}

def save_students(students):
  """Saves students to a JSON file."""
  with open('students.json', 'w') as f:
    json.dump(students, f)

def main():
  """Main function to run the student management system."""
  students = load_students()
  while True:
    print("\nStudent Management System")
    print("1. Counsellor")
    print("2. Faculty")
    print("3. Student")
    print("4. Exit")
    role_id = input("Enter a role ID: ")
    while True:
      try:
        int(role_id)
        break
      except ValueError:
        print("Invalid role ID. Please enter a valid number.")
        role_id = input("Enter a role ID: ")
    if role_id == 1:
      while True:
        print("\nCounsellor Menu")
        print("1. Add student")
        print("2. Remove student")
        print("3. View all students")
        print("4. View specific student")
        print("5. Back")
        choice = input("Enter a choice: ")
        while True:
          try:
            int(choice)
            break
          except ValueError:
            print("Invalid choice. Please enter a valid number.")
            choice = input("Enter a choice: ")
        if choice == 1:
          add_student(students)
        elif choice == 2:
          remove_student(students)
        elif choice == 3:
          view_all_students(students)
        elif choice == 4:
          view_specific_student(students)
        elif choice == 5:
          break
        else:
          print("Invalid choice.")
    elif role_id == 2:
      faculty_name = input("Enter your faculty name: ")
      while True:
        print("\nFaculty Menu")
        print("1. Add marks to student")
        print("2. View all students")
        print("3. Back")
        choice = input("Enter a choice: ")
        while True:
          try:
            int(choice)
            break
          except ValueError:
            print("Invalid choice. Please enter a valid number.")
            choice = input("Enter a choice: ")
        if choice == 1:
          add_marks(students, faculty_name)
        elif choice == 2:
          view_all_students(students)
        elif choice == 3:
          break
        else:
          print("Invalid choice.")
    elif role_id == 3:
      print("Student functionality is not implemented yet.")
    elif role_id == 4:
      save_students(students)
      break
    else:
      print("Invalid choice.")

if __name__ == '__main__':
  main()