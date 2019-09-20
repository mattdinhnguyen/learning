from resources.utils import run_tests
import random

def split2chunks(l, n):      
    # looping till length l 
    for i in range(0, len(l)):
        if i+n <= len(l):
            yield l[i:i+n]

def largestRec(hist):
    bins = []
    bin = []
    for h in hist:
        if h:
            bin.append(h)
        else:
            bins.append(bin)
            bin = []
    else:
        bins.append(bin)
    maxRec = 0
    for bin in bins:
        for n in range(1,len(bin)+1):
            for c in split2chunks(bin, n):
                area = min(c)*n
                if area > maxRec:
                    maxRec, maxChunk = area, c
    print("hist: {}, maxChunk: {}, maxRec: {}".format(hist, maxChunk, maxRec))
    return maxRec

tests_largest_rec = [
    ({'hist': [2, 1, 5, 6, 2, 3]}, 10),
    ({'hist': [2, 1, 0, 6, 2, 3]}, 6),
    ({'hist': [2, 1, 0, 8, 2, 3]}, 8),
    ({'hist': [2, 1, 0, 6, 2, 2, 2, 2, 2, 2]}, 14)
]
# hist = tests_largest_rec[0][0]['hist']
# for n in range(1,len(hist)+1):
#     print([c for c in split2chunks(hist, n)])
random.seed(0)
n = 10
random_list = [random.randint(1, n*10) for _ in range(n)]
largestRec(random_list)
# run_tests(tests_largest_rec, largestRec)

