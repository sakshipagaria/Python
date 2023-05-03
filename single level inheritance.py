class college:
    def college_name(self):
        print("SVKM IoT")

class student(college):
    def student_info(self):
        print("Name: Sakshi Pagariya")
        print("Branch: Computer")

obj = student()
obj.college_name()
obj.student_info()
