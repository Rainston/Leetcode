class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r,c=len(matrix),len(matrix[0])
        re=[]
        rm=set()
        for i in range(r):
            rm.add(min(matrix[i]))
        cm=set()
        for j in range(c):
            ck=matrix[0][j]
            for k in range(r):
                ck=max(ck,matrix[k][j])
            if ck in rm:
                re.append(ck)
        return re