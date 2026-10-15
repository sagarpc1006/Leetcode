class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            result=numbers[left] + numbers[right]
            if result == target:
                return [left+1,right+1]
            elif result>target:
                right-=1
            else :
                left+=1












        """dict1={}
        for i in range(len(numbers)):
            if ( target-numbers[i] in dict1):
                return [dict1[target-numbers[i]]+1,i+1]
            else :
                dict1[numbers[i]]=i
"""
