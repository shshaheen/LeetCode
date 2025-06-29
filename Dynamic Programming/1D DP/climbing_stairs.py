
# 1. Recursive (Brute Force)
def climb_recursive(n):
    if n <= 1:
        return 1
    return climb_recursive(n - 1) + climb_recursive(n - 2)
# Time Complexity: O(2^n)
# Space Complexity: O(n)

# 2. Memoization (Top-Down DP)
def climb_memoization(n, dp):
    if n <= 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = climb_memoization(n - 1, dp) + climb_memoization(n - 2, dp)
    return dp[n]
# Time Complexity: O(n)
# Space Complexity: O(2n)

# 3. Tabulation (Bottom-Up DP)
def climb_tabulation(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = dp[0] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
# Time Complexity: O(n)
# Space Complexity: O(n)

# 4. Space Optimization (Only storing last two results)
def climb_space_optimized(n):
    if n <= 1:
        return 1
    prev2 = 1
    prev1 = 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1
# Time Complexity: O(n)
# Space Complexity: O(1)