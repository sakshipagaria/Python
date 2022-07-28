----capitalize the 1st letter of the every word in the string----
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for i in s[:].split():
        s=s.replace(i,i.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
--------output---------
hey sakshi hello 
=Hey Sakshi Hello
