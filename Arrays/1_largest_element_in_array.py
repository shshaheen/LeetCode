arr = [1, 2, 3, 4, 5]

# ----------> Brute Force 
# Sort the array in ascending order.
arr.sort()
# Print the (size of the array -1)th index.
print(arr[len(arr) - 1])

# TIME COMPLEXITY: O(nlogn)
# SPACE COMPLEXITY: O(1)

# ----------> Optimal Approach
largest = arr[0]
# Traverse the array.
for i in range(1, len(arr)):
    # Update the largest element if the current element is greater.
    if arr[i] > largest:
        largest = arr[i]
# Print the largest element found.
print(largest)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
