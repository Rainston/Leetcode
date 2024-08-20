class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        c=True
        m=True
        for i in range(len(nums)-1):
             if nums[i]>nums[i+1]:
                c=False
        for i in range(len(nums)-1):         
             if nums[i]<nums[i+1]:
                m=False
        if c:
            return c
        elif m:
            return m
        else:
            return False