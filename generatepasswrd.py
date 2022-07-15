import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="1234567890"
character="!@#$%^&*{}[](),./?><\_-;"

all=lower+upper+number+character
length=8
password="".join(random.sample(all,length))
print(password)