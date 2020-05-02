#!/bin/python3

import math
import os
import random
import re
import sys


def binary_conversion(m):
    lst = []
    while m / 2 > 0:
        lst.append(m % 2)
        m = m // 2
    lst.reverse()
    return lst


if __name__ == '__main__':
    n = int(input())
    bi = binary_conversion(n)
    print(bi)
    print(bin(n))
    count = []
    count.extend(bi)

    print(count)

    for j in range(len(bi)):
        for k in range(j, len(bi) - 1):
            if (bi[k] == 1) and (bi[k + 1] == 1):
                count[j] += 1
            else:
                break
        print(count)
    print(count)
    print(max(count))
