class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
       if (dividend==-2**31 and divisor==-1):
          return 2**31-1
       if (dividend>0 and divisor>0) or(dividend<0 and divisor<0):
          return floor(dividend/divisor)
       else:
            return ceil(dividend/divisor)