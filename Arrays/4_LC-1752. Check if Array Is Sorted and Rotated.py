from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        flag=0
        n=len(nums)
        idx=-1
        for i in range(1,n):
            if(nums[i]<nums[i-1]):
                idx = i
        if(idx==-1):
            return True
        for j in range(idx+1,idx+n):
            if(nums[j%n]< nums[(j-1)%n]):
                return False
        return True