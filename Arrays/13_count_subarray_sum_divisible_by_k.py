arr = [4, 5, 0, -2, -3, 1]

#Brute Force
count = 0
n = len(arr)
k = 5
for i in range(n):
    for j in range(i, n):
        if(sum(arr[i:j+1]) % k == 0):
            count += 1
print(count)
# Time Complexity: O(n^3)
# Space Complexity: O(1)

# Optimal Approach
d={0:1}
presum = 0
count = 0
for i in range(n):    
    presum += arr[i]
    rem = presum % k
    if(rem in d):
        count += d[rem]
    if(rem not in d):
        d[rem] = 1
    else:
        d[rem] += 1
print(count)
# Time Complexity: O(n)
# Space Complexity: O(n)