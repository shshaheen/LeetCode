from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        c=0
        while(len(set(nums))<len(nums)):
            if(len(nums)>3):
                nums=nums[3:]
            else:
                nums=[]
            c+=1
        return c