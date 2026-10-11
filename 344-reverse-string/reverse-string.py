class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=len(s)
        temp=0
        if ( l % 2==0):
            for i in range(int(l/2)):
                temp=s[i]
                s[i]=s[l-i-1]
                s[l-i-1]=temp
        else :
            for i in range(int(l/2-0.5)):
                temp=s[i]
                s[i]=s[l-i-1]
                s[l-1-i]=temp

       
            
        