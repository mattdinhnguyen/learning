import sys
import random
from collections import defaultdict

random.seed(0)
from resources.utils import run_tests
from functools import reduce

class Bucket(object):
    def __init__(self, min, max):
        self.min = min
        self.max = max

def countingSort(arr):
    max = -sys.maxint-1
    min = sys.maxint
    for v in arr:
        if v < min:
            min = v
        if v > max:
            max = v
    print(min, max)
    n = len(arr)
    lowerBound = (max - min)/(n-1)
    buckets = defaultdict(Bucket)

    for v in arr:
        idx = (v - min)/lowerBound
        if idx in buckets:
            if buckets[idx].min > v:
                buckets[idx].min = v
            elif buckets[idx].max < v:
                buckets[idx].max = v
        else:
            buckets[idx] = Bucket(v,v)
    maxGap = 0
    prev = min
    for idx in range(n):
        if idx in buckets:
            curGap = buckets[idx].min - prev
            prev = buckets[idx].max
            if curGap > maxGap:
                maxGap = curGap
    print("countingSort: {}".format(maxGap))
    return maxGap

def maxGap(arr):
    max = 0
    for i,v in enumerate(arr[:-1]):
        gap = arr[i+1]-v
        if gap > max:
            max = gap
    print("maxGap {}".format(max))
    return max

# Driver code to test above 
arr = [3, 10, 7, 8, 9, 1, 5]
arr = sorted(arr)
print ("Sorted array is: {}, maxGap is: {}".format(arr, maxGap(arr)))
print(countingSort(arr))
random_list = [random.randint(1, 1000) for _ in range(100)]
tests_counting_sort = [
    ({'arr': [1, 2]}, maxGap([1, 2])),
    ({'arr': [2, 1]}, maxGap([1, 2])),
    ({'arr': [5, 1, 1]}, maxGap([1, 1, 5])),
    ({'arr': [9, 1, 10, 2]}, maxGap([1, 2, 9, 10])),
    ({'arr': list(range(10)[::-1])}, maxGap(list(range(10)))),
    ({'arr': random_list}, maxGap(sorted(random_list)))
]

run_tests(tests_counting_sort, countingSort)