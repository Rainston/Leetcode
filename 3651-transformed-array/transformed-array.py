class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        re=[0]*n
        for i in range(len(nums)):
            re[i]=nums[(i+nums[i])%n]
        return re