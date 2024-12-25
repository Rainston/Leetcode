class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ik=0
        res=[]
        for i in range(len(nums)):
            if nums[i]<k:
                return -1
            if nums[i]>k and nums[i] not in res:
                ik+=1
                res.append(nums[i])
        return ik