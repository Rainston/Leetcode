class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
          return False
        rev=0
        y=x
        while(x > 0):
            pop=x%10
            rev=(rev*10)+pop
            x//=10
        if(y==rev):
            return True
        else:
            return False