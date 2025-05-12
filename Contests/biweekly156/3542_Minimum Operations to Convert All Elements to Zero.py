# Approach -1:
# 1. Sort the array
# 2. Use a sorted list to store the indices of the elements
# 3. Iterate through the array
# 4. If the element is not 0, increment the operations
# 5. If the next element is the same as the current element, check if the next smaller element is greater than the next same element

from typing import List
from bisect import insort, bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        a= []
        for idx, val in enumerate(nums):
            a.append((val, idx))
        a.sort()
        i=0
        sorted_idx = []
        operations=0
        while(i<n):
            insort(sorted_idx, a[i][1])
            if(a[i][0] !=0):
                operations+=1

            while(i+1<n and a[i][0]==a[i+1][0]):
                idx = bisect_right(sorted_idx, a[i][1])
                next_smaller_idx = sorted_idx[idx] if idx<len(sorted_idx) else float('inf')
                next_same_idx = a[i+1][1]
                if(next_same_idx>next_smaller_idx):
                    break
                i+=1
                insort(sorted_idx, a[i][1])
            i+=1
        return operations



# Approach -2:
# Initialize an empty stack and a counter op = 0.
# Iterate through each number in nums:
# While the top of the stack is greater than the current number, pop and increment op.
# Skip pushing if the top of the stack is equal to the current number or the current number is 0.
# Push the number onto the stack if not skipped
#  finally, return op + len(stack).

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        stack = []
        op=0
        for i in range(n):
            while(stack and stack[-1]>nums[i]):
                op+=1
                stack.pop()
            if((stack and stack[-1] == nums[i]) or nums[i] ==0):
                continue
            else:
                stack.append(nums[i])
        return op+len(stack)
