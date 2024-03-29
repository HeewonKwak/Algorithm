# Sorting / Running Time of Algorithms
# https://www.hackerrank.com/challenges/runningtime/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here
    ans = 0
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
            ans += 1
        arr[j+1] = key
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
