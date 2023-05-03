#multilevel inheritance

class college:
    def college_name(self):
        print("SVKM IOT")

class student(college):
    def student_info(self):
        print("Name: Sakshi Pagariya")
        print("Branch: Computer")

class exam(student):
    def exam_details(self):
        print("Subject1: Compiler Design")
        print("Subject2: Computer Networks")
        print("Subject3: IoT")

obj= exam()
obj.college_name()
obj.student_info()
obj.exam_details() 
