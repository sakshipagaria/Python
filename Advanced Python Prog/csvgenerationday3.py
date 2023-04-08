import csv
f=open("student.csv","a",newline="")
a=csv.writer(f)     #here it will return csv writer obj
a.writerow(["Student_id","Roll_no","Name","Mobile_no"])          #col names

Student_id=int(input("Enter your student id : "))
Roll_no=int(input("Enter your roll number : "))
Name=input("Enter your name : ")
Mobile_no=int(input("Enter your mobile number : "))

a.writerow([Student_id,Roll_no,Name,Mobile_no])
print("Student record has been saved")

