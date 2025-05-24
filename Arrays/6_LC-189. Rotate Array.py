from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        nums[:] = nums[-k:]+nums[:-k]
# Time complexity: O(n)
# Space complexity: O(n)



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
       
        k=k%n
        temp = nums[n-k:]
        # print(temp)
        j=1
        for i in range(len(nums)-k-1,-1,-1):
            nums[n-j] = nums[i]
            j+=1
        for i in range(len(temp)):
            nums[i]=temp[i]

# Time complexity: O(n)
# Space complexity: O(n)


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution.rotate(nums, k)
    print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]