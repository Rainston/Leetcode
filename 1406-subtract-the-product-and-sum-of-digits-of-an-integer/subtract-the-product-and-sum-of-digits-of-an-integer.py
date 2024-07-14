class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        z=0
        y=1
        while n>0:
            z+=n%10
            y*=n%10
            n//=10
            
        return y-z