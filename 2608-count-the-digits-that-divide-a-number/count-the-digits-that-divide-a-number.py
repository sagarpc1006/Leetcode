class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        hello=num
        while num>0:
            ans=num%10
            if (hello%ans==0):
                count+=1
            num//=10
        return count
            
        