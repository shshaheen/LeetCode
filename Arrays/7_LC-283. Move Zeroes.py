from typing import List

# ----------> Brute Force <----------
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=[]
        n = len(nums)
        for i in range(n):
            if(nums[i]!=0):
                temp.append(nums[i])
        nums[:] = temp[:]
        for i in range(n-len(temp)):
            nums.append(0)
# Time Complexity: O(n)
# Space Complexity: O(n)

# ---------->Better Approach<---------- (Two Pointers)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1