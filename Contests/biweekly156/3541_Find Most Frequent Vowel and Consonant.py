from collections import defaultdict

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a','e','i','o','u'}
        h1 = defaultdict(int)
        h2 = defaultdict(int)
        for ch in s:
            if(ch in vowels):
                h1[ch]+=1
            else:
                h2[ch]+=1
        v1,v2=0,0
        if(h1):
            v1 = max(h1.values())
        if(h2):
            v2 = max(h2.values())
        return v1+v2