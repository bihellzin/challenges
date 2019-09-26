#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    tres = (n-1)//3
    cinco = (n-1)//5
    quinze = (n-1)//15

    total = ((3+(tres*3))*tres)//2 + ((5+(cinco*5))*cinco)//2 - ((15+(quinze*15))*quinze)//2
    print(total)