#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    jogo = "#"
    spaces = ""
    cont = 0
    while cont < n-1:
        spaces += " "
        cont += 1
    for i in range(n):
        print(spaces+jogo)
        spaces = spaces[1:]
        jogo += "#"

if __name__ == '__main__':
    n = int(input())

    staircase(n)
