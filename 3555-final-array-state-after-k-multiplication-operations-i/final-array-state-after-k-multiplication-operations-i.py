class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k!=0:
            mini=nums[0]
            idx=0
            for i in range(len(nums)):
                if nums[i]<mini:
                   mini=nums[i]
                   idx=i
            nums[idx]*=multiplier
            k-=1
        return nums

                
