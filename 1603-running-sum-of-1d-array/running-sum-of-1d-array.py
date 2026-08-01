class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum=0
        a=[]
        for i in range(0,n):
            for j in range(0,n):
                if j <= i :
                    sum = sum + nums[j]
            a.append(sum)
            sum = 0
        return a 

        
        