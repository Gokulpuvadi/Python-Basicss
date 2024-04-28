class school:
 def _init_(self,identity,proof):
     self.identity=identity
     self.proof=proof
 def student(self):
     print("hii")
     print("iam student")
 def teacher(self):
     print("good morning")
     print("iam teacher")
 def principal(self):
     print("one and all")
     print("iam principal")

obj1=school(12,13)
obj1.student()

obj2=school(15,56)
obj2.teacher()

obj3=school(32,76)
obj3.principal()
