arr = [5, 2, 9, 1, 5, 6]

def merge_sort(arr,lb, ub):
    mid = (lb+ub)//2
    if lb < ub:
        merge_sort(arr, lb, mid)
        merge_sort(arr, mid + 1, ub)
        merge(arr, lb, mid, ub)
def merge(arr, lb, mid, ub):
    left = arr[lb:mid + 1]
    right = arr[mid + 1:ub + 1]
    
    i = j = 0
    k = lb
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr
sorted_arr = merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", sorted_arr)

# Time Complexity: O(n log n)
# Space Complexity: O(n)