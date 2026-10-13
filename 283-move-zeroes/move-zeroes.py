class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """count=0
        for i in range(len(nums)):
            if (nums[i] > 0 or nums[i]<0 ):
                temp=nums[count]
                nums[count]=nums[i]
                nums[i]=temp
                count=count+1"""
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums
        
        