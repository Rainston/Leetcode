class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ca=-1
        v=0
        for i in nums:
            if v==0:
                ca=i
            if i ==ca:
                v+=1
            else:
                v-=1
        return ca