arr = [1,2,3,1,1,1,1,4,2,3]
n = len(arr)
k = 5
# Brute Force -> Generate all subarrays and check if their sum is equal to k
count = 0
for i in range(n):
    for j in range(i, n):
        if(sum(arr[i:j+1]) == k):
            count += 1
print(count)
# Time Complexity: O(n^3)
# Space Complexity: O(1)

# Better Approach -> Use a hashmap to store the sum of all subarrays
d={0:1}
presum = 0
count = 0
for i in range(n):
    presum += arr[i]
    if(presum - k in d):
        count += d[presum - k]
    if(presum not in d):
        d[presum] = 1
    else:
        d[presum] += 1
print(count)
# Time Complexity: O(n)
# Space Complexity: O(n)

# Optimal Approach -> Two Pointers(Only for Positives)
left, right = 0, 0
presum = 0
count = 0
while(right < n):
    presum += arr[right]
    while(left <= right and presum > k):
        presum -= arr[left]
        left += 1
    if(presum == k):
        count += 1
    right += 1
print(count)
# Time Complexity: O(n)
# Space Complexity: O(1)