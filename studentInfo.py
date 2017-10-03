def main():
 students = [
   Student("Halsted", "Larsson", 37),
   Student("Hailey", "Greene", 14),
   Student("Caitlin", "Greene", 17),
   Student("Nadia", "Crockett-Current", 17),
   Student("Rosalie", "Bryson", 17),
   Student("Sofia", "MB", 17),
   Student("Zoe", "Silvia", 17),
   Student("Stella", "Lynch", 17),
 ]

 printHeader()
 selection = getUserSelection()
 if selection == "0":
   printStudentsByAge(students)
 elif selection == "1":
   printStudentsByLName(students)
 elif selection == "2":
   printStudentsByFName(students)
 else:
   print ("SELECTION NOT RECOGNIZED")


class Student:
 def __init__(self, firstName, lastName, age):
   self.lastName = lastName
   self.age = age
   self.firstName = firstName

 def assignRandomName(self):
   pass

 def assignRandomAge(self):
   self.age = random.randint(0,100)

 def assignRandomWeight(self, isMetric):
   pass

 def assignRandomHeight(self, isMetric):
   pass

inputQuestions = [
 "For STUDENTS BY AGE, type 0",
 "For STUDENTS BY LAST NAME, type 1",
 "For STUDENTS BY FIRST NAME, type 2",
 "For SUM of STUDENT AGES type 4",
 "For AVERAGE of STUDENT AGES type 5",
]

def getUserSelection():
 print (inputQuestions[0])
 print (inputQuestions[1])
 print (inputQuestions[2])
 return input("Type selection and press enter:")

def printHeader():
   print("HEADER TEXT HERE")


def printStudentsByAge(students):
 print ("--Students By Age--")
 sortStudents = sorted(students, key=lambda student: student.age)
 for student in sortStudents:
   print (str(student.age) + ", " +student.lastName + ", " + student.firstName)

def printStudentsByLName(students):
 print ("--Students By Last Name--")
 sortStudents = sorted(students, key=lambda student: student.lastName)
 for student in sortStudents:
   print (student.lastName + ", " + student.firstName + ", " + str(student.age))

def printStudentsByFName(students):
 print ("--Students By First Name--")
 sortStudents = sorted(students, key=lambda student: student.firstName)
 for student in sortStudents:
   print (student.firstName + " " + student.lastName + ", " + str(student.age))

def printSumAge(students):
 print ("Answer:")

def printAvgAge(students):
 print ("Answer:")

def ageRange(studentA, studentB):
 return math.abs(studentA.age - studentB.age)


main()
