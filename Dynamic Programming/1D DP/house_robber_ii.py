# House Robber II
# This is a variation of the House Robber problem where the houses are arranged in a circle.
# We need to consider two cases:
# 1. Include the first house and exclude the last house.
# 2. Exclude the first house and include the last house.
# We take the maximum of these two cases.
from .house_robber import house_robber_space_optimized

# Example input
nums = [2, 3, 7, 8, 1]  
def house_robber_ii():
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    return max(house_robber_space_optimized(nums[:-1]), house_robber_space_optimized(nums[1:]))
