from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_of_digits(num):
            summ=0
            while(num):
                summ+=num%10
                num//=10
            return summ
        for idx,num in enumerate(nums):
            if(idx == sum_of_digits(num)):
                return idx
        return -1