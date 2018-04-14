class Student:
   def __init__(self, rollno, name):
      self.rollno = rollno
      self.name = name
   def displayStudent(self):
      self.rollno = input("rollno")
      self.name = input("name")
      print (self.rollno)
      print(self.name)
#emp1 = Student(121, "Ajeet")
#emp2 = Student(122, "Sonoo")
emp1 = Student("self.name", "self.rollno")
emp2 = Student("self.name", "self.rollno")
emp1.displayStudent()
emp2.displayStudent()






