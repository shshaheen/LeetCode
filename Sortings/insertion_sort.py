arr = [5, 2, 9, 1, 5, 6]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)

# Time Complexity: O(n^2)
# Space Complexity: O(1)