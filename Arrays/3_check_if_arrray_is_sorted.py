arr = [4, 5, 1, 2, 3, 6, 7, 8, 9]
for i in range(1, len(arr)):
    # Check if the current element is less than the previous element.
    if arr[i] < arr[i - 1]:
        # If it is, print "NO" and break the loop.
        print("NO")
        break
else:
    # If the loop completes without finding any unsorted elements, print "YES".
    print("YES")
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
