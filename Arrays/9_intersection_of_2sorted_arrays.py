arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5,6,7]

#intersection of 2 sorted arrays

i,j = 0,0
intersection = [float('-inf')]  # Initialize union with a placeholder
while(i<len(arr1) and j<len(arr2)):
    if(arr1[i]==arr2[j]):
        intersection.append(arr1[i])
        i+=1
        j+=1
    elif(arr1[i]<arr2[j]):
        i+=1
    else:
        j+=1

print(intersection[1:])

#Time Complexity : O(n+m)
#Space Complexity : O(1)
