class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        fre={}
        sor=sorted(list(set(arr)))
        for i in range(len(sor)):
            fre[sor[i]]=i+1
        for i in range(len(arr)):
            arr[i]=fre[arr[i]]
        return arr