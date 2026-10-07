class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        start = 1
        if  len(nums) <= 2:
            return len(nums)
        for i in range(2,len(nums)):
            if nums[i] != nums[start-1]:
                start=start+1
                nums[start]=nums[i]
        return start + 1
