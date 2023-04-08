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

#------example------------------
import csv 
e=open("example.csv","a",newline="")
a=csv.writer(e)
a.writerow(["stud_id","name","rollno","email","address","mobileno","p1","p2","p3","p4","p5","total","percentage","result"])

stud_id=int(input("Enter your student id : "))
name=input("Enter your name : ")
rollno=int(input("Enter your roll number : "))
email=input("Enter your email address : ")
address=input("Enter your address : ")
mobileno=int(input("Enter your mobile number : "))
p1=int(input("English marks= "))
p2=int(input("Maths marks= "))
p3=int(input("Science marks= "))
p4=int(input("Social Science marks="))
p5=int(input("Geography= "))
total=p1+p2+p3+p4+p5
percentage=(total/500)*100
if p1>40 and p2>40 and p3>40 and p4>40 and p5>40:
    result="Pass"
else:
    result="Fail"
    
print("Total marks obtained out of 500= ",total)
print("Percentage obtained= ",percentage)
print("Result: ",result)
