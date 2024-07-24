class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pk=[]
        for i,n in enumerate(nums):
            n=str(n)
            mn=0
            for c in n:
                mn=mn*10+mapping[int(c)]
            pk.append((mn,i))
        pk.sort()
        return [nums[p[1]] for p in pk]