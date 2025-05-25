arr = [5, 2, 9, 1, 5, 6]

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

# Time Complexity: O(n log n)
# Space Complexity: O(log n)
# This version of partitioning is known as the Hoare partition scheme
# which is more efficient in practice than the Lomuto partition scheme.
# The choice of pivot and the partitioning method can significantly affect the performance of quicksort.
