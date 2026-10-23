class Solution:
    def sortString(self,s):
        s=list(s)
        s.sort()
        return "".join(s)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        d={}
        for s in strs:

            key=self.sortString(s)
            if key in d:
                d[key].append(s)
            else :
                d[key]=[s]
        return list(d.values())
        