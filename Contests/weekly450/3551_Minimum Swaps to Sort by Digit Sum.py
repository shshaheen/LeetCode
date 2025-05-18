from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        def sum_of_digits(num):
            summ=0
            while(num):
                summ+=num%10
                num//=10
            return summ
        new=[]
        for idx,num in enumerate(nums):
            new.append((num,sum_of_digits(num)))
            
        s = [x[0] for x in sorted(new, key=lambda x: (x[1], x[0]))]
        val_idx = {num:i for i,num in enumerate(nums)}
        # i=0
        swaps=0
        visited = [False]*n
        for i in range(n):
            if(visited[i] or nums[i] == s[i]):
                continue
            cycle=0
            j=i
            while(not visited[j]):
                visited[j] = True
                actual_num = s[j]
                j=val_idx[actual_num]
                cycle+=1
            if(cycle>1):
                swaps+=cycle-1
            # i+=1
        return swaps