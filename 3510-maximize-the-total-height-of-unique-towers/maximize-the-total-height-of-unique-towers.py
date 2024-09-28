class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        minh=maximumHeight[0]
        arr=[maximumHeight[0]]
        for i in range(1,len(maximumHeight)):
            cur=maximumHeight[i]
            if cur>=minh:
                minh-=1
                cur=minh
            arr.append(cur)
            minh=min(cur,minh)
            if minh==0:
                return -1
        return sum(arr)
