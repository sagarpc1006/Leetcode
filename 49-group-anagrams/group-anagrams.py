class Solution:
    def sortString(self,s):
        s1=list(s)
        s1.sort()
        return "".join(s1)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d={}
        for s in strs:
            key=self.sortString(s)
            if key in d:
                d[key].append(s)
            else :
                d[key]=[s]
        return list(d.values())
        

