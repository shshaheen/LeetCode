from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        i=1
        total=1
        while(i<n):
            if(i<n and ratings[i]==ratings[i-1]):
                total+=1
                i+=1
                continue
            peak =1
            while(i<n and ratings[i]> ratings[i-1]):                
                
                peak+=1
                total+=peak
                i+=1
            down=1
            while(i<n and ratings[i]< ratings[i-1]):                
                total+=down
                down+=1                
                i+=1
            if(down>peak):
                total+=down-peak
        return total