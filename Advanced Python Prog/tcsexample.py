#wap to read the data from csv file and sort them as per bubble sort
# import csv
# #f=open("sorting.csv","a",newline="")
# file = csv.reader(open('test.csv', 'r'))
# a=csv.writer(f)     #here it will return csv writer obj
# a.writerow(["Age","Salary"])          #col names

# Age=int(input("Enter the age : "))
# Salary=int(input("Enter your Salary : "))
# a.writerow([Age ,  Salary])
# print("Student record has been saved")


import csv
# Read data from CSV file
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    data = [(int(row[0]), int(row[1])) for row in reader]

# Bubble sort algorithm
n = len(data)
for i in range(n):
    for j in range(0, n-i-1):
        if data[j][0] > data[j+1][0]:
            data[j], data[j+1] = data[j+1], data[j]

# Print sorted data
for age, salary in data:
    print(f"Age: {age}, Salary: {salary}")