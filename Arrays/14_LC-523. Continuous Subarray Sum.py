nums = [23, 2, 4, 6, 7]
k = 6

n=len(nums)
if(n<2):
    print(False)
presum=0
d = {0:-1}
for i in range(n):
    presum += nums[i]
    rem = presum%k
    if(rem in d):
        if(i-d[rem]>=2):
            print(True)
    else:
        d[rem] = i
print(False)
