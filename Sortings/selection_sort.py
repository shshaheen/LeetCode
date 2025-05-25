arr = [5, 2, 9, 1, 5, 6]
# Selection Sort Implementation

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if arr[mini] > arr[j]:
                mini = j
        if i != mini:
            arr[i], arr[mini] = arr[mini], arr[i]
    return arr

sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)

# Time Complexity: O(n^2)
# Space Complexity: O(1)