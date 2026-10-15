class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dict1={}
        for i in range(len(numbers)):
            if ( target-numbers[i] in dict1):
                return [dict1[target-numbers[i]]+1,i+1]
            else :
                dict1[numbers[i]]=i

