class Solution:
    def isHappy(self, n: int) -> bool:
        v=set()
        def pow(n):
            z=0
            while n:
                y=n%10
                z+=y**2
                n//=10
            return z
        while n not in v:
            v.add(n)
            n=pow(n)
            if n==1:
                return True
        return False