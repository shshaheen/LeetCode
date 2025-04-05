from functools import reduce
from itertools import combinations
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        sums = sum(nums)
        for i in range(2,len(nums)+1):
            new=list(combinations(nums,i))
            for j in new:
                val=reduce(lambda x,y: x ^ y,j)
                sums += val
        return sums