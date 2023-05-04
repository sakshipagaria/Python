#polymorphism
#functional overloading

class Principal:
    def role(self):
        print("Principal: I'm managing all the activites of college")

class Dean:
    def role(self):
        print("Dean: I'm decision taking person")

class HoD:
    def role(self):
        print("HoD: I have the responsibility of the department")

class Faculty:
    def role(self):
        print("Faculty: I have to complete the syllabus in time")

def func(obj):
    obj.role()

campus=[Principal(),Dean(),HoD(),Faculty()]
for obj in campus:
    func(obj)