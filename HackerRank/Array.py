#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("input number of element in list : "))

    arr = list(map(int, input("elements :").rstrip().split()))[:n]

    try:
        for i in range(1, n + 1):
            print(arr[int(n - i)], end=" ")
    except:
        print("enter elements with space between them")
