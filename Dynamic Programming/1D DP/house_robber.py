# 1. Recurrence relation:
nums = [2, 7, 9, 3, 1]

def house_robber_rec(ind):
    if ind < 0:
        return 0
    if(ind == 0):
        return nums[ind]
    pick = nums[ind] + house_robber_rec(ind - 2)
    not_pick = house_robber_rec(ind - 1)
    return max(pick, not_pick)
# Time Complexity: O(2^n) - Exponential
# Space Complexity: O(n) - due to recursion stack

# 2. Memoization (Top-Down DP)
def house_robber_memo(ind, memo):
    if ind < 0:
        return 0
    if ind == 0:
        return nums[ind]
    if memo[ind] != -1:
        return memo[ind]
    
    pick = nums[ind] + house_robber_memo(ind - 2, memo)
    not_pick = house_robber_memo(ind - 1, memo)
    memo[ind] = max(pick, not_pick)
    return memo[ind]
# Time Complexity: O(n) - Linear with respect to n
# Space Complexity: O(n + n) - due to memoization array and recursion stack

# 3. Tabulation (Bottom-Up DP)
def house_robber_tabulation():
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    
    for i in range(1, n):
        pick = nums[i]
        if i > 1:
            pick += dp[i - 2]
        not_pick = dp[i - 1]
        dp[i] = max(pick, not_pick)
    
    return dp[-1]
# Time Complexity: O(n) - Linear with respect to n
# Space Complexity: O(n) - due to dp array

# 4. Space Optimized DP
def house_robber_space_optimized():
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]    
    prev1 = nums[0]
    prev2 = 0
    for i in range(1, n):
        pick = nums[i] + (prev2 if i > 1 else 0)
        not_pick = prev1
        current = max(pick, not_pick)        
        prev2 = prev1
        prev1 = current
    
    return prev1
# Time Complexity: O(n) - Linear with respect to n
# Space Complexity: O(1) - Constant space used for prev1 and prev2