
# 1. Recursive (Brute Force)
def frog_jump_recursive(i, heights):
    if i == 0:
        return 0
    jumpOne = frog_jump_recursive(i - 1, heights) + abs(heights[i] - heights[i-1])
    if(i>1):
        jumpTwo = frog_jump_recursive(i - 2, heights) + abs(heights[i] - heights[i - 2])
        return min(jumpOne, jumpTwo)
    return jumpOne
# Time Complexity: O(2^n) - Exponential
# Space Complexity: O(n) - due to recursion stack

# 2. Memoization (Top-Down DP)
def frog_jump_memoization(i, heights, dp):
    if i == 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    jumpOne = frog_jump_memoization(i - 1, heights, dp) + abs(heights[i] - heights[i-1])
    if(i>1):
        jumpTwo = frog_jump_memoization(i - 2, heights, dp) + abs(heights[i] - heights[i - 2])
        dp[i] = min(jumpOne, jumpTwo)
    else:
        dp[i] = jumpOne
    return dp[i]
# Time Complexity: O(n) - Linear
# Space Complexity: O(2n) - due to recursion stack and dp array

# 3. Tabulation (Bottom-Up DP)
def frog_jump_tabulation(n, heights):
    dp = [0] * (n + 1)
    dp[1] = abs(heights[1] - heights[0])
    for i in range(2, n + 1):
        jumpOne = dp[i - 1] + abs(heights[i] - heights[i - 1])
        jumpTwo = dp[i - 2] + abs(heights[i] - heights[i - 2])
        dp[i] = min(jumpOne, jumpTwo)
    return dp[n]
# Time Complexity: O(n) - Linear
# Space Complexity: O(n) - due to dp array

# 4. Space Optimization (Only storing last two results)

def frog_jump_space_optimized(n, heights):
    prev =abs(heights[1] - heights[0])
    prev2=0
    for i in range(2, n + 1):
        curr = min(prev + abs(heights[i] - heights[i - 1]), prev2 + abs(heights[i] - heights[i - 2]))
        prev2 = prev
        prev = curr
    return prev
# Time Complexity: O(n) - Linear
# Space Complexity: O(1) - Constant space