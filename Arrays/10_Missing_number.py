arr = [1,2,4,5]
n=len(arr)

# Brute Force
def missing_number(arr,n):
    for i in range(1,n+1):
        if i not in arr:
            return i
    return -1
print(missing_number(arr,n))
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Better Approach
def missing_number(arr,n):
    hassh = [0]*(n+1)
    for i in range(n):
        hassh[arr[i]] = 1
    for i in range(1,n+1):
        if hassh[i] == 0:
            return i
    return -1
print(missing_number(arr,n))
# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimal Approach
def missing_number(arr,n):
    sum1 = 0
    for i in range(n):
        sum1 += arr[i]
    sum2 = (n*(n+1))//2
    return sum2 - sum1
print(missing_number(arr,n))
# Time Complexity: O(n)
# Space Complexity: O(1)

#Super Optimal Approach
def missing_number(arr,n):
    xor1 = 0
    xor2 = 0
    for i in range(n):
        xor1 ^= arr[i]
    for i in range(1,n+1):
        xor2 ^= i
    return xor1 ^ xor2
print(missing_number(arr,n))
# Time Complexity: O(n)
# Space Complexity: O(1)
