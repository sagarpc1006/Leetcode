class Solution:
    def firstUniqChar(self, s: str) -> int:
        empty={}
        for ch in s:
            if ch in empty:
                empty[ch]+=1
            else :
                empty[ch]=1
        for i in range(len(s)):
            if empty[s[i]] == 1 :
                return i
        return -1

        