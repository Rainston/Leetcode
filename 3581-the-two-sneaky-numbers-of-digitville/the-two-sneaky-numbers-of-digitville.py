class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        do={}
        arr=[]
        for num in nums:
            if num in do:
                do[num]+=1
            if num not in do:
                do[num]=1
        for num in nums:
            if do[num]==2:
                arr.append(num)
        return set(arr) 