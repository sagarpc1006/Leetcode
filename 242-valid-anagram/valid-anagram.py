class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c={}
        d={}
        if ( len(s) != len(t)):
            return False
        else :
            for ch in s:
                if ( ch in c) :
                    c[ch]=c[ch]+1
                else :
                    c[ch]=1
            for ch in t:
                if ( ch in d) :
                    d[ch]=d[ch]+1
                else :
                    d[ch]=1
            if (c==d):
                return True
            else :
                return False

            