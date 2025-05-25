arr = [5, 2, 9, 1, 5, 6]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_arr = bubble_sort(arr)

# Time Complexity: O(n^2)
# Space Complexity: O(1)
print("Sorted array:", sorted_arr)