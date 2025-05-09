from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n=len(differences)
        prefix=[0]
        for diff in differences:
            prefix.append(prefix[-1]+diff)
        return max(0, upper-max(prefix) - (lower-min(prefix))+1)
        