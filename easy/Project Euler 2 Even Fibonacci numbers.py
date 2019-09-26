#!/bin/python3

import sys

def fibonacci(n):
    n1 = 1
    n2 = 2
    soma = 0
    while n2 < n:
        if n2%2 == 0:
            soma += n2
        temp = n2
        n2 += n1
        n1 = temp
    
    
    return soma

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fibonacci(n))
