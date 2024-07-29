class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count=0
        n=len(rating)
        for m in range(1,n-1):
            ls=rl=0
            for i in range(m):
                if rating[i]<rating[m]:
                    ls+=1
            for j in range(m+1,n):
                if rating[j]>rating[m]:
                    rl+=1
            count+=ls*rl
            ll=m-ls
            rs=n-1-m-rl
            count+=ll*rs
        return count
                    