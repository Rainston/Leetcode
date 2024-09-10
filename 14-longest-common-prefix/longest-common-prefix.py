class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ak=""
        for i in range(len(min(strs))):
            s=strs[0][i]
            for j in range(len(strs)):
                if strs[j][i]!=s:
                    return ak
            ak+=s
        return ak