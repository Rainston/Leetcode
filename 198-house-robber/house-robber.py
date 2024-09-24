class Solution:
    def rob(self, nums: List[int]) -> int:
        s=0
        d=0
        
        for i in nums:
            t=max(i+s,d)
            s=d
            d=t
        return d