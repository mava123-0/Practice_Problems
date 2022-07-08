#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    # Write your code here
    # flag=arr[1]
    for i in range(1,n):
        flag=arr[i]
        j=i
        while(flag<arr[j-1] and j>0):
            arr[j]=arr[j-1]
            j-=1
            for i in range(n):
                print(arr[i],end=" ")
            print()
        arr[j]=flag
    for i in range(n):
        print(arr[i],end=" ")
    print()

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
