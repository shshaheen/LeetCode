from typing import List


arr = [1,1,2,2,3,3,4,4,5]

# -------------> Brute Force <-------------
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = []
        for i in nums:
            if(i not in s):
                s.append(i)
        for i in range(len(s)):
            nums[i]= s[i]
        return len(s)
    
# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(n)

# -------------> Optimal Approach <-------------
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if(nums[i]!=nums[j]):
                nums[i+1] = nums[j]
                i+=1
        return i+1
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)