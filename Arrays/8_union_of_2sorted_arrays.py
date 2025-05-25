arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5,6,7]

i,j = 0,0
union = [float('-inf')]  # Initialize union with a placeholder
while i < len(arr1) and j < len(arr2):
    if(union[-1]!=arr1[i] and union[-1]!=arr2[j]):
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        else:
            union.append(arr1[i])
            i += 1
        j += 1
    
while i < len(arr1):
    if union[-1] != arr1[i]:
        union.append(arr1[i])
    i += 1
while j < len(arr2):
    if union[-1] != arr2[j]:
        union.append(arr2[j])
    j += 1
print("Union of the two sorted arrays is:", union)
