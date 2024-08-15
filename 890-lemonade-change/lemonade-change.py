class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
     if bills[0]!=5:
        return False
     counti=0
     countj=0
     for i in bills:
        if i==5:
            counti+=1
        elif i==10:
            if counti>0:
             counti-=1
            else:
                return False
            countj+=1
        else:
            if counti>0 and countj>0:
             countj-=1
             counti-=1
            elif counti>2:
                counti-=3
            else:
                return False
     return True