def reverse_and_add(num):
    iterations = 0

    while True:
        num += int(str(num)[::-1])  #reverse the num and add it to the original
        iterations += 1

        if str(num) == str(num)[::-1]:   #to check if palindrome 
            return iterations, num
  
r = int(input())      # Read the number of test cases

# Process each test case
for i in range(r):
    num = int(input())
    iterations, palindrome = reverse_and_add(num)
    print(iterations, palindrome)
