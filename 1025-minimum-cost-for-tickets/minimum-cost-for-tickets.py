class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        td=set(days)
        dp=[0]*366
        for i in range(1,366):
            if i not in td:
                dp[i]=dp[i-1]
            else:
                c1=dp[i-1]+costs[0]
                c2=dp[max(0,i-7)]+costs[1]
                c3=dp[max(0,i-30)]+costs[2]
                dp[i]=min(c1,c2,c3)
        return dp[365]