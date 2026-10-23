class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        d={}
        maxi=0
        while right < len(s):
            if s[right] in d:
                left=max(left,d[s[right]] + 1)
            maxi=max(maxi,right-left+1)
            d[s[right]]=right
            right+=1
        return maxi
 