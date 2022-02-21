import random
import datetime
bday=[]
i=0
while(i<50):
    year=random.randint(1900,2022)
#122yrs is the oldest a person lived ,till the date
    if(year%4==0 and year%100!=0 or year%400==0):
        leap=1
    else:
        leap=0
    month=random.randint(1, 12)
    if(month==2 and leap==1):
        day=random.randint(1,29)
    elif(month==2 and leap==0):
        day=random.randint(1,28)
    elif(month==7 or month==8):
        day=random.randint(1,31)
    elif(month%2!=0 and month<7):
        day=random.randint(1,31)
    elif(month%2==0 and month<7 and month<12):
        day=random.randint(1,31)
    else:
        day=random.randint(1,30)
    dd=datetime.date(year,month,day)
    day_of_year=dd.timetuple().tm_yday     #this funciton gives the day of year
    i=i+1
    bday.append(day_of_year)
    
bday.sort()
i=0
while(i<50):
    print(bday[i])
    i=i+1
