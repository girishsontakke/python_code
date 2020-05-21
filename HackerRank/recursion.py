#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the factorial function below.
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


m = int(input())

print(factorial(m))
