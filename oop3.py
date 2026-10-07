class Student:
  #this is our constructor (def__init__)
  college_name = "BN College"

  def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")



s1 = Student ("Tamanna",88)
print(s1.name,s1.marks)

s2 = Student("Israt",99)
print(s2.name,s2.marks)

print(s2.college_name)