#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    menor = 99999999999999999999999999999999999
    maior = -99999999999999999999999999999999999
    cont = 0
    for i in range(len(arr)):
        soma = 0

        for j in range(len(arr)):
            if i == j:
                soma = soma

            else:
                soma += arr[j]

        if soma > maior:
            maior = soma
        if soma < menor:
            menor = soma
        cont += 1
    
    print(menor, maior)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
