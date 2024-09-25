class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n=len(s)
        a=['']*n
        for i in range(n):
            a[i]=s[(i+k)%n]
        return ''.join(a)
