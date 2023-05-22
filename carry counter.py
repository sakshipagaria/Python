num1, num2 = map(int, input().split())

mod1 = num1
mod2 = num2

carryCounter = 0    #for number of carryoperations
carry = 0       #for storing carry value during addtion

while mod1 > 0 or mod2 > 0:
    mod1 = num1 % 10 + carry
    mod2 = num2 % 10

    num1 = num1 // 10   #dividing by 10 so that we can remove the last digit of both the numbers
    num2 = num2 // 10

    carry = 0     #reset the carry to 0 for fresh start for each digit

    if (mod1 + mod2) > 9:
        carry = 10 - (mod1 + mod2)
        carryCounter += 1

if carryCounter > 0:
    print(str(carryCounter) + " carry operation.")
else:
    print("No carry operation.")
