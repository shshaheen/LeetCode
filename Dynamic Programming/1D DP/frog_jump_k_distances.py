
# 1. Recursive (Brute Force)
def frog_jump_k_distances_recursive(i, heights, k):
    if i == 0:
        return 0
    min_cost = float('inf')
    for j in range(1, k + 1):
        if i - j >= 0:
            cost = frog_jump_k_distances_recursive(i - j, heights, k) + abs(heights[i] - heights[i - j])
            min_cost = min(min_cost, cost)
    return min_cost
# Time Complexity: O(k^n) - Exponential
# Space Complexity: O(n) - due to recursion stack

# 2. Memoization (Top-Down DP)
def frog_jump_k_distances_memoization(i, heights, k, memo):
    if i == 0:
        return 0
    if i in memo:
        return memo[i]
    min_cost = float('inf')
    for j in range(1, k + 1):
        if i - j >= 0:
            cost = frog_jump_k_distances_memoization(i - j, heights, k, memo) + abs(heights[i] - heights[i - j])
            min_cost = min(min_cost, cost)
    memo[i] = min_cost
    return min_cost
# Time Complexity: O(n * k) - Linear with respect to n and k
# Space Complexity: O(n + n) - due to memoization dictionary

# 3. Tabulation (Bottom-Up DP)
def frog_jump_k_distances_tabulation(heights, k):
    n = len(heights)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, k + 1):
            if i - j >= 0:
                cost = dp[i - j] + abs(heights[i] - heights[i - j])
                dp[i] = min(dp[i], cost)
    return dp[-1]
# Time Complexity: O(n * k) - Linear with respect to n and k
# Space Complexity: O(n) - due to dp array