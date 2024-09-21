class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums)):
            if nums.count(nums[i])>1:
                arr.append(nums[i])
        return set(arr)