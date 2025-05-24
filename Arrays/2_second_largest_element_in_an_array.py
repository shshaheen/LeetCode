arr = [4, 5, 1, 2, 3, 6, 7, 8, 9]

# -------------> Brute Force <-------------
# Sort the array 
arr.sort()
largest = arr[len(arr) - 1]
for i in range(len(arr) - 2, -1, -1):
    # Check if the current element is less than the largest element.
    if arr[i] < largest:
        # Print the second largest element and break the loop.
        print(arr[i])
        break

# TIME COMPLEXITY: O(nlogn+n)
# SPACE COMPLEXITY: O(1)

# -------------> Better Approach <-------------
large = arr[0]
for i in range(1, len(arr)):
    # Update the largest element if the current element is greater.
    if arr[i] > large:
        large = arr[i]
second_largest = -1
for i in range(len(arr)):
    # Check if the current element is less than the largest element.
    if arr[i] < large:
        # Update the second largest element if the current element is greater.
        if arr[i] > second_largest:
            second_largest = arr[i]

# Print the second largest element found.
print(second_largest)
# TIME COMPLEXITY: O(n+n)=O(2n)
# SPACE COMPLEXITY: O(1)


# -------------> Optimal Approach <-------------
largest = arr[0]
second_largest = -1
for i in range(1, len(arr)):
    # Update the largest and second largest elements based on the current element.
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

# Print the second largest element found.
print(second_largest)   
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)