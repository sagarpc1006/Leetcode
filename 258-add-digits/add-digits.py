class Solution:
    def addDigits(self, num: int) -> int:

        if num<=9:
            return num
        current_sum=0
        while num > 0:
            ans=num%10
            current_sum+=ans
            num//=10
        return self.addDigits(current_sum)   
        
        
        
        