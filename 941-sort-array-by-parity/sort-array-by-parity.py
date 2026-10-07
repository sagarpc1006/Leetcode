class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        x=-1
        temp=0
        for i in range(0,len(nums)):
            if nums[i] % 2 == 0:
                x=x+1
                temp=nums[x]
                nums[x]=nums[i]
                nums[i]=temp
        return  nums
        