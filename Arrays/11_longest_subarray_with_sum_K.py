# Subarray -> A subarray is a contiguous part of an array.
# Sub sequence -> A subsequence is a sequence you get by removing some elements from another sequence, without changing the order of the rest.


arr = [1,2,3,1,1,1,1,4,2,3]
n = len(arr)
k = 5
# Brute Force -> Generate all subarrays and check if their sum is equal to k
maxi = 0
for i in range(n):
    for j in range(i, n):
        if(sum(arr[i:j+1]) == k):
            maxi = max(maxi, j-i+1)
print(maxi)
# Time Complexity: O(n^3)
# Space Complexity: O(1)

# Better Approach -> Use a hashmap to store the sum of all subarrays
prefix_sum = {}
curr_sum = 0
maxlen = 0
for i in range(n):
    curr_sum += arr[i]
    if(curr_sum == k):
        maxlen = max(maxlen, i+1)
    if(curr_sum - k in prefix_sum):
        maxlen = max(maxlen, i - prefix_sum[curr_sum - k])
    if(curr_sum not in prefix_sum):
        prefix_sum[curr_sum] = i
# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimal Approach -> Two Pointers
left, right = 0, 0
summ = arr[0]
maxlen = 0
while(right < n):
    while(left <= right and summ > k):
        summ -= arr[left]
        left += 1
    if(summ == k):
        maxlen = max(maxlen, right - left + 1)
    right += 1
    if(right < n):
        summ += arr[right]
print(maxlen)

# Time Complexity: O(n)
# Space Complexity: O(1)

