class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        dk=0
        arr=[]
        for i in range(len(nums)):
            if not arr or nums[arr[-1]]> nums[i]:
                arr.append(i)
        for j in range(len(nums)-1,-1,-1):
            while arr and nums[arr[-1]]<=nums[j]:
                dk=max(dk,j-arr.pop())
        return dk