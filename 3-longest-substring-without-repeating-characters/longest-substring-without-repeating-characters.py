class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        count=0
        temp=0
        for i in range(len(s)):
            d[s[i]]=1
            for j in range(i+1,len(s)):
                if s[j] not in d:
                    d[s[j]]=1
                    temp+=1
                else :
                    break
            if temp>count:
                count=temp
            temp=0
            d={}
        if len(s)==0:
            return 0
        else :
            return count+1