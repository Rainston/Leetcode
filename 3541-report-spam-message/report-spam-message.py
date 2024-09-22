class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count=0
        bk=set(bannedWords)
        for i in range(len(message)):
                if message[i] in bk:
                    count+=1
        if count>=2:
            return True
        else:
            return False