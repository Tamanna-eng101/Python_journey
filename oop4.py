#create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average
class Student:
    def __init__(self,name,marks):
        self.name = name#thats my attribute
        self.marks = marks
    def get_avg(self):
        sum = self.marks
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg score is:",sum/3)
        
s1 = Student("Tamanna",[99,98,97])# this is object attribute
s1.get_avg()

s1.name ="Israt"
s1.get_avg()