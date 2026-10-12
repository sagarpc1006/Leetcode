class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        s=s.strip()
        l=len(s)
        for i in range(l):
            if ( s[l-i-1] == ' ' ):
                break
            else :
                count=count+1
        return count


        