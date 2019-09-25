#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[8] == 'P' and s[0:2] != '12':
        a = int(s[0:2])
        s = s[2:8]
        a += 12
        s = str(a) + s
    
    elif s[8] == 'P' and s[0:2] == '12':
        s = s[0:8]
    
    elif s[8] == 'A' and s[0:2] != '12':
        s = s[0:8]
    
    elif s[8] == 'A' and s[0:2] == '12':
        a = '00'
        s = s[2:8]
        s = a+s
    
    return s

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
