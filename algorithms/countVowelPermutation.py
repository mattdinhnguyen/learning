#!/usr/local/bin/python3
from typing import List
from collections import OrderedDict

class Solution:
    vowels = ('a', 'e', 'o', 'u', 'i')
    g = OrderedDict([('a',('e',)),('e',tuple('ai')),('o',tuple('iu')),('u',('a',)),('i',tuple('aeou'))])
    print(g)
    perm = OrderedDict([(1,{j:1}) for j in range(5)])
    for j in range(5):
        perm[1][j] = 1
    def countVowelPermutation(self, n: int) -> int:
        for i in range(2,n+1):
            self.perm[i] = dict()
            for j in range(5):
                self.perm[i][j] = self.perm[i-1][j] * len(self.g[self.vowels[j]])
        return(sum(self.perm[n].values()))

for n in range(1,6):
    print(Solution().countVowelPermutation(n))
#"ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua"
#"aea","aei", "iea", "iei"
