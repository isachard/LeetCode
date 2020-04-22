class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        location = 0 
        for i in range(len(nums)):
            if nums[i] == 0 :
                location += 1
            else:
                if location > 0 :
                    nums[i-location] = nums[i]
                    nums[i] = 0
                    
        